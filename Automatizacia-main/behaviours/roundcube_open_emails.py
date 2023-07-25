import time
import yaml
import sys
import os


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
    # Open and login into roundcube web
    roundcube_login = run_sikulix_script("roundcube_web", "main", ["janko.binconf@gmail.com", "ethmyuouchknwcqo", cfg["app"]["roundcube_url"]])
    if roundcube_login["status"]!="success":
        sys.exit(1)

    time.sleep(4)

    # Read unread emails
    while True:
        open_unread_emails = run_sikulix_script("roundcube_web", "open_unread_emails")

        if open_unread_emails["msg"]=="Opened all unread messages":
            break

        elif open_unread_emails["msg"]=="Found phishing email":
            open_phishing_website = run_sikulix_script("roundcube_web", "open_phishing_website")
            if open_phishing_website["status"]!="success":
                continue
            phishing = run_sikulix_script("phishing_password_reset", "main", ["janko.binconf@gmail.com", "ethmyuouchknwcqo"])
            if phishing["status"]=="success":
                continue
            # Additional logic

        elif open_unread_emails["msg"]=="Found email attachment":
            download_attachment = run_sikulix_script("roundcube_web", "download_attachment")
            if download_attachment["status"]!="success":
                continue
            # Additional logic

    print("Finished all operations")

if __name__ == "__main__":
    main()