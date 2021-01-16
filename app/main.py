"""Flask application for the WS2801 controller."""

import argparse

from flask import Flask, jsonify, request
from ledpi_controller.controller import Controller
from ledpi_controller.yaml_processor import StateYamlProcessor, YamlProcessor

from app.server import Server

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", required=True)
parser.add_argument("-s", "--state", required=True)
args = parser.parse_args()


def create_app(config, state_file):
    leds = config.get("leds", 160)
    state_processor = StateYamlProcessor(state_file)
    controller = Controller(state_processor, leds)
    server = Server(controller)

    app = Flask(__name__)

    @app.route("/api/v1/state", methods=["GET", "POST"])
    def state_method():
        if request.method == "POST":
            json = request.get_json(force=True)
            server.set_state(json)

        return jsonify({"success": True, **server.get_state()})

    return app


# main()
if __name__ == "__main__":
    config = YamlProcessor(args.config).load()
    create_app(config, args.state).run(
        host="0.0.0.0", port=config.get("port", 80), debug=config.get("debug", False)
    )
