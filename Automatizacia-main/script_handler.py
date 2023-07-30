import os
import subprocess
import logging
import logging.config
import sys
import time

import yaml
import json

cfg=None
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

loggerTmp = logging.getLogger("autoconfig")
stdoutLogger = logging.StreamHandler(stream=sys.stdout)
stdoutLogger.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
loggerTmp.addHandler(stdoutLogger)

def run_sikulix_script(script_name: str, function_name: str = "main", script_args: list[str] = None) -> str:
    """
    Executes sikulix script with sikulix ide.

    script_name
            Name of the script in the sikulix_scripts folder without file extension.
    function_name
            Name of the function inside the script to call
    script_args
            Array of arguments for the sikulix function, for needed arguments check the sikulix script
    return
            Returns last line from log
    """

    script_name=script_name+".sikuli"
    script_path=os.path.join(scripts_dir, script_name)

    # Convert script_args list into a string with a delimiter (':')
    script_args = ";".join(script_args) if script_args else ""

    # Create command
    command = f'java -jar {cfg["app"]["sikulix_ide"]} -r {script_path} --args {function_name} {script_args}'

    # Run sikulix script
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    line_dict = None
    for line in iter(lambda: process.stdout.readline(), b""):
        line = line.strip().decode("utf-8")

        # Filter object output
        if line.startswith("{") and line.endswith("}"):
            try:
                line_dict = line.strip()
                line_dict = line_dict.replace("'", "\"")
                print(line_dict, type(line_dict))
                line_dict = json.loads(line_dict)
                match line_dict["level"]:
                    case "info":
                        loggerTmp.info(msg=line_dict["msg"])
                    case "error":
                        loggerTmp.error(msg=line_dict["msg"])

            except json.JSONDecodeError:
                print("Invalid JSON format:", line)
                continue
        
        # Push output into console
        sys.stdout.buffer.write((line + "\n").encode("utf-8")) 

    return line_dict