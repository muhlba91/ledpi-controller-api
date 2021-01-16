"""Server handler."""
from ledpi_controller.controller import Controller


class Server:
    """Server to handle requests."""

    def __init__(self, controller: Controller):
        self.controller = controller

    def get_state(self):
        """Get the current state."""
        return {
            "state": "on" if self.controller.is_on() else "off",
            "rgb_color": self.controller.rgb_hex_color(),
            "leds": self.controller.get_leds(),
            "brightness": self.controller.brightness(),
        }

    def set_state(self, state: dict):
        """Set a new state."""
        if "rgb_color" in state:
            self.controller.set_rgb_color(state["rgb_color"])

        if "brightness" in state:
            self.controller.set_brightness(state["brightness"])

        if "state" in state:
            state = state["state"]
            if state == "on":
                self.controller.turn_on()
            elif state == "off":
                self.controller.turn_off()
