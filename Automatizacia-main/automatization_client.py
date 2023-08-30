import os
import socket
import logging
import logging.config
import sys
import yaml
import json
import requests
import time

cfg = None
parent_dir = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(parent_dir, "config.yml")
scripts_dir = os.path.join(parent_dir, "sikulix_scripts")

# Read config
with open(config_file, "r") as stream:
    try:
        cfg = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(f"Error reading configuration from '{config_file}': {exc}")
        sys.exit(1)

# Configure logger
if "logging" in cfg.keys():
    try:
        # Create the log folder if it does not exist
        log_folder_path = cfg["logging"]["handlers"]["file"]["filename"]
        log_folder = os.path.dirname(log_folder_path)
        try:
            if not os.path.exists(log_folder):
                os.makedirs(log_folder)
        except Exception as ex:
            print(f"Can't create log folder {log_folder}: {ex}")
        # Ignore possible logger issue and start the autoconfig anyway
        logging.config.dictConfig(cfg["logging"])
    except Exception as ex:
        log_folder = None
        print(f"Exception raised while creating logger: {ex}")
        sys.exit(2)

# Create the default logger to stdout and to the default log file
log_file = os.path.join(log_folder, "app.log") if log_folder else None

logging.basicConfig(
    filename=log_file,
    filemode="a",
    format=cfg["logging"]["formatters"]["simple"]["format"],
    datefmt=cfg["logging"]["formatters"]["simple"]["datefmt"],
    level=logging.DEBUG
)


def main():
    hostname = socket.gethostname()
    while True:
        request = requests.get(
            f"{cfg['automatization_client']['caldera_agent']}/{hostname}", headers={"Accept": "application/json"})
        headers = request.headers
        print(request._content)
        content_type = headers.get("Content-Type")

        if content_type.startswith("application/json"):
            print(request.json())
        elif content_type.startswith("text/plain"):
            print(request.text)
        else:
            print(f"Unknown Content-Type: {content_type}")

        time.sleep(10)


if __name__ == "__main__":
    main()
