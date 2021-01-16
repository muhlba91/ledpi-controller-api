"""Tests for the Server class."""
import sys
from unittest.mock import MagicMock, patch

import pytest

sys.modules["adafruit_ws2801"] = MagicMock()
sys.modules["board"] = MagicMock()

from app.server import Server


class TestServer:
    @pytest.fixture
    def ctrl(self):
        with patch("ledpi_controller.controller.Controller") as mock_controller:
            mock_controller.is_on.return_value = True
            mock_controller.rgb_hex_color.return_value = "value"
            mock_controller.get_leds.return_value = 160
            mock_controller.brightness.return_value = 1.0
            yield mock_controller

    @pytest.fixture
    def server(self, ctrl):
        yield Server(ctrl)

    def test_init(self, server):
        assert server.controller is not None

    def test_get_state(self, server):
        assert server.get_state() == {
            "state": "on",
            "rgb_color": "value",
            "leds": 160,
            "brightness": 1.0,
        }

    def test_set_state_turn_on(self, ctrl, server):
        server.set_state(
            {
                "state": "on",
                "rgb_color": "#ffffff",
                "brightness": 0.5,
            }
        )
        assert ctrl.set_rgb_color.called
        assert ctrl.set_brightness.called
        assert ctrl.turn_on.called

    def test_set_state_turn_off(self, ctrl, server):
        server.set_state(
            {
                "state": "off",
                "rgb_color": "#ffffff",
                "brightness": 0.5,
            }
        )
        assert ctrl.set_rgb_color.called
        assert ctrl.set_brightness.called
        assert ctrl.turn_off.called

    def test_set_state_partial(self, ctrl, server):
        server.set_state(
            {
                "rgb_color": "#ffffff",
                "brightness": 0.5,
            }
        )
        assert ctrl.set_rgb_color.called
        assert ctrl.set_brightness.called
        assert not ctrl.turn_off.called
        assert not ctrl.turn_on.called
