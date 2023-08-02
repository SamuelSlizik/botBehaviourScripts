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
    time.sleep(5)

    force_procrastinate = False

    # Decide if the user procrastinates or works
    while True:
        if random.uniform(0, 1) < cfg["user"]["procrastination_chance"] or force_procrastinate:
            force_procrastinate = False
            procrastination_time = random.uniform(cfg["user"]["procrastination_min_time"], cfg["user"]["procrastination_max_time"])

            # Open edge
            open_edge = run_sikulix_script("edge_utils", "open_edge")
            if open_edge["status"] != "success":
                continue

            time.sleep(1)
            if random.uniform(0, 1) < cfg["user"]["procrastination_preference"]:
                # Procrastinate on youtube
                search_url = run_sikulix_script("edge_utils", "search_by_url", ["youtube.com"])
                if search_url["status"] == "success":
                    time.sleep(3)
                    run_sikulix_script("more_edge_utils", "edge_watch_youtube_shorts", [str(procrastination_time)])
            else:
                # Procrastinate on cats
                search_text = run_sikulix_script("edge_utils", "search_by_text", ["kittens"])
                if search_text["status"] == "success":
                    time.sleep(3)
                    run_sikulix_script("more_edge_utils", "edge_scroll_images", [str(procrastination_time)])

            time.sleep(1)
            close_tab = run_sikulix_script("edge_utils", "close_latest_tab")
        else:
            # Open and login into roundcube web
            roundcube_login = run_sikulix_script("roundcube_web", "main", ["janko.binconf@gmail.com", "ethmyuouchknwcqo", cfg["app"]["roundcube_url"]])
            if roundcube_login["status"] != "success":
                continue

            time.sleep(4)

            # Read unread email
            open_unread_emails = run_sikulix_script("roundcube_web", "open_unread_emails")

            if open_unread_emails["msg"] == "Opened all unread messages":
                force_procrastinate = True
                run_sikulix_script("edge_utils", "close_latest_tab")

            elif open_unread_emails["msg"] == "Found phishing email" and random.uniform(0, 1) < cfg["user"]["phishing_success_chance"]:
                open_phishing_website = run_sikulix_script("roundcube_web", "open_phishing_website")
                if open_phishing_website["status"] == "success":
                    phishing = run_sikulix_script("phishing_password_reset", "main", ["janko.binconf@gmail.com", "ethmyuouchknwcqo"])

            elif open_unread_emails["msg"] == "Found email attachment":
                download_attachment = run_sikulix_script("roundcube_web", "download_attachment")
                if download_attachment["status"] == "success":
                    # work with attachment
                    time.sleep(1)
                    run_sikulix_script("edge_utils", "close_latest_tab")
                    time.sleep(1)
                    selectLast = run_sikulix_script("sys_utils", "selectLastFromDownloads")
                    if selectLast["status"] == "success":
                        time.sleep(1)
                        run_sikulix_script("sys_utils", "cut")
                        # Check or create todays archive subfolder
                        create_todays_folder = run_sikulix_script("sys_utils", "check_or_create_folder", [
                            cfg["app"]["archive_path"] + "\\" + datetime.now().strftime("%Y-%m-%d")])
                        if create_todays_folder["status"] == "success":
                            time.sleep(1)
                            run_sikulix_script("sys_utils", "pasteClipboard")
                            extension = run_sikulix_script("sys_utils", "get_file_extension")
                            print(extension["msg"])


if __name__ == "__main__":
    main()