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
            if cfg["user"]["is_generator"] == "True":
                # generate new work
                template_name = "template" + str(random.randint(1, int(cfg["app"]["template_count"]))) + random.choice([".docx", ".xlsx", ".pptx", ".pdf"])
                template_path = os.path.join(templates_dir, template_name)
                downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
                downloads_path = os.path.join(downloads_path, template_name)
                shutil.copyfile(template_path, downloads_path)
                time.sleep(1)
                selectLast = run_sikulix_script("sys_utils", "selectLastFromDownloads")
                if selectLast["status"] != "success":
                    continue
                time.sleep(1)
                run_sikulix_script("sys_utils", "cut")
                # Check or create todays archive subfolder
                create_todays_folder = run_sikulix_script("sys_utils", "check_or_create_folder", [
                    cfg["app"]["archive_path"] + "\\" + datetime.now().strftime("%Y-%m-%d")])
                if create_todays_folder["status"] != "success":
                    continue
                time.sleep(1)
                run_sikulix_script("sys_utils", "pasteClipboard")
            else:
                # Open and login into roundcube web
                roundcube_login = run_sikulix_script("roundcube_web", "main", [cfg["user"]["user_email"], cfg["user"]["user_password"], cfg["app"]["roundcube_url"]])
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
                    if download_attachment["status"] != "success":
                        continue
                    # work with attachment
                    time.sleep(1)
                    run_sikulix_script("edge_utils", "close_latest_tab")
                    time.sleep(1)
                    selectLast = run_sikulix_script("sys_utils", "selectLastFromDownloads")
                    if selectLast["status"] != "success":
                        continue
                    time.sleep(1)
                    run_sikulix_script("sys_utils", "cut")
                    # Check or create todays archive subfolder
                    create_todays_folder = run_sikulix_script("sys_utils", "check_or_create_folder", [cfg["app"]["archive_path"] + "\\" + datetime.now().strftime("%Y-%m-%d")])
                    if create_todays_folder["status"] != "success":
                        continue
                    time.sleep(1)
                    run_sikulix_script("sys_utils", "pasteClipboard")
                    extension = run_sikulix_script("sys_utils", "get_file_extension")
                    time.sleep(1)
                    run_sikulix_script("sys_utils", "set_sort_by_date")
                    time.sleep(1)
                    run_sikulix_script("sys_utils", "open_top_file")
                    time.sleep(1)
                    if extension["msg"] == ".docx":
                        # word doc
                        rand = random.randint(0, 1)
                        if rand == 0:
                            # export to pdf
                            run_sikulix_script("work_utils", "exportDocxToPdf")
                        else:
                            # export to pptx
                            run_sikulix_script("work_utils", "exportDocxToPptx")
                    elif extension["msg"] == ".xlsx":
                        # excel spreadsheet
                        rand = random.randint(0, 2)
                        if rand == 0:
                            # export to pdf
                            run_sikulix_script("work_utils", "exportXlsxToPdf")
                        elif rand == 1:
                            # export to pptx
                            run_sikulix_script("work_utils", "exportXlsxToPptx")
                        else:
                            # export to docx
                            run_sikulix_script("work_utils", "exportXlsxToDocx")
                # Send email onward
                time.sleep(1)
                roundcube_login = run_sikulix_script("roundcube_web", "main", [cfg["user"]["user_email"], cfg["user"]["user_password"], cfg["app"]["roundcube_url"]])
                if roundcube_login["status"] != "success":
                    continue
                time.sleep(1)
                run_sikulix_script("work_utils", "send_mail", [cfg["user"]["forward_email"], "Test subject", "Test body", "True"])
                time.sleep(1)
                run_sikulix_script("edge_utils", "close_latest_tab")


if __name__ == "__main__":
    main()