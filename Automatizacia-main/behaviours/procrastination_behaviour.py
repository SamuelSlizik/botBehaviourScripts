import os
from datetime import datetime
import time
import yaml
import sys
import random
import shutil

top_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(top_dir)
from script_handler import run_sikulix_script, loggerTmp

cfg=None
config_file = os.path.join(top_dir, "config.yml")
scripts_dir = os.path.join(top_dir, "sikulix_scripts")
templates_dir = os.path.join(top_dir, "templates")

# Read config
with open(config_file, "r") as stream:
    try:
        cfg = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(f"Error reading configuration from '{config_file}': {exc}")
        sys.exit(1)

def main():
    procrastination_time = random.uniform(cfg["user"]["procrastination_min_time"],
                                          cfg["user"]["procrastination_max_time"])
    start_time = datetime.now()

    # Open edge
    open_edge = run_sikulix_script("edge_utils", "open_edge")
    if open_edge["status"] != "success":
        return

    time.sleep(1)
    if random.uniform(0, 1) < cfg["user"]["procrastination_preference"]:
        # Procrastinate on youtube
        search_url = run_sikulix_script("edge_utils", "search_by_url", ["youtube.com"])
        if search_url["status"] == "success":
            time.sleep(3)
            start_procrast = run_sikulix_script("more_edge_utils", "start_edge_watch_youtube_shorts")
            if start_procrast["status"] == "success":
                while (datetime.now() - start_time).total_seconds() < procrastination_time and cfg["automatization_client"]["force_stop_behaviour"] == False:
                    procrast = run_sikulix_script("more_edge_utils", "edge_watch_youtube_shorts")
                    if procrast["status"] != "success":
                        break
    else:
        # Procrastinate on cats
        search_text = run_sikulix_script("edge_utils", "search_by_text", ["kittens"])
        if search_text["status"] == "success":
            time.sleep(3)
            start_procrast = run_sikulix_script("more_edge_utils", "start_edge_scroll_images")
            if start_procrast["status"] == "success":
                while (datetime.now() - start_time).total_seconds() < procrastination_time and cfg["automatization_client"]["force_stop_behaviour"] == False:
                    run_sikulix_script("more_edge_utils", "edge_scroll_images")

    time.sleep(1)
    close_tab = run_sikulix_script("edge_utils", "close_latest_tab")


if __name__ == "__main__":
    main()