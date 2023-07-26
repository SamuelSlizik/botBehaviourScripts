import os
from datetime import datetime
import time
import yaml
import sys
import random

top_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(top_dir)
from script_handler import run_sikulix_script, loggerTmp

cfg=None
config_file = os.path.join(top_dir, "config.yml")
scripts_dir = os.path.join(top_dir, "sikulix_scripts")

# Read config
with open(config_file, "r") as stream:
    try:
        cfg = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(f"Error reading configuration from '{config_file}': {exc}")
        sys.exit(1)

def main():
    # Wait so all the systems have time to initialize
    sleep(60)

    # Check or create todays archive subfolder
    create_todays_folder = run_sikulix_script("sys_utils", "check_or_create_folder", [cfg["app"]["archive_path"]] + "\\" + datetime.now().strftime("%Y-%m-%d"))

    # Decide if the user procrastinates or works
    while True:
        if random.uniform(0, 1) < cfg["user"]["procrastination_chance"]:
            procrastination_time = random.uniform(cfg["user"]["procrastination_min_time"], cfg["user"]["procrastination_max_time"])

            # Open edge
            open_edge = run_sikulix_script("edge_utils", "open_edge")
            if open_edge["status"] != "success":
                continue

            sleep(1)

            if random.uniform(0, 1) < cfg["user"]["procrastination_preference"]:
                # Procrastinate on youtube
                search_url = run_sikulix_script("edge_utils", "search_by_url", ["youtube.com"])
                if search_url["status"] == "success":
                    sleep(10)
                    run_sikulix_script("more_edge_utils", "edge_watch_youtube_shorts", [procrastination_time])
            else:
                # Procrastinate on cats
                search_text = run_sikulix_script("edge_utils", "search_by_text", ["kittens"])
                if search_text["status"] == "success":
                    sleep(10)
                    run_sikulix_script("more_edge_utils", "edge_scroll_images", [procrastination_time])

            sleep(1)
            close_tab = run_sikulix_script("edge_utils", "close_latest_tab")
        else:
            #work

if __name__ == "__main__":
    main()