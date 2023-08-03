from sikuli import *
import os
import sys

# Custom modules
import logger
import edge_utils

script_name = "roundcube_web.py"
# Function declaration
def login(email, password):
    try:
        type(email)
        wait(0.5)
        type(Key.ENTER)
        wait(1)
        type(password)
        type(Key.ENTER)
    
        logger.log("info", "Logged in as: {email}".format(email=email), "success")
    except Exception as ex:
        logger.log("error", "Error while logging into roundcube as {email}".format(email=email), "failure", ex)

def open_unread_emails():
    try:
        if exists("1690925296596.png"):
            click(Pattern("1690925296596.png").targetOffset(4,26))
        if exists("1690925371195.png"):
            click(Pattern("1690925371195.png").targetOffset(128,28))
        while exists (Pattern("1689975173681.png").similar(0.60).targetOffset(0,-15)):
            click(Pattern("1689975173681.png").similar(0.60).targetOffset(0,-15))
            wait(10)
            scan_email()
            wait(0.5)
        logger.log("info", "Opened all unread messages", "success")
    except Exception as ex:
        logger.log("error", "Error opening unread emails", "failure", ex)
        
def scan_email():
    try:
        # Allow external files
        if exists("1689972567735.png"):
            click("1689972567735.png")
            wait(4)

        # Check for phishing link
        if exists("1689972936871.png"):
            logger.log("info", "Found phishing email", "success")
            exit(0)

        # Check for attachments
        if exists("1690925940672.png"):
            logger.log("info", "Found email attachment", "success")
            exit(0)

    except Exception as ex:
        logger.log("error", "Error while scanning emails", "failure", ex)

def download_attachment():
    try:
        click(Pattern("1690925940672.png").targetOffset(14,-2))
        wait("1690926649062.png")
        click("1690926649062.png")
        wait(20)
        logger.log("info", "Downloaded attachement file", "success")
    except FindFailed as ex:
        logger.log("error", "Error while downloading attachment file", "failure", ex)

def open_phishing_website():
    try:
        click("1689972936871.png")
        wait(1)
        type("l", Key.CTRL)
        wait(0.5)
        type(Key.RIGHT)
        wait(0.5)
        type(Key.ENTER)
        wait(2)
        logger.log("info", "Opened phishing website", "success")
    except FindFailed as ex:
        logger.log("error", "Error while opening phishing website", "failure", ex)


def open_mail():
    try:
        wait("1690923882783.png")
        click("1690923882783.png")
        logger.log("info", "Opened mail", "success")
    except Exception as ex:
        logger.log("error", "Error while opening mail", "failure", ex)

def filter_by_unread():
    try:
        if exists("1690923625911.png"):
            click("1690923625911.png")
            wait(10)
        logger.log("info", "Filtered by unread", "success")
    except Exception as ex:
        logger.log("error", "Error while filtering by unread", "failure", ex)


def open_top_email():
    try:
        wait("1690923882783.png")
        click(Pattern("1690923882783.png").targetOffset(79,4))
        wait(20)
        if exists("1690923955826.png"):
            scan_email()
        logger.log("info", "Opened top mail", "success")
    except Exception as ex:
        logger.log("error", "Error while opening top mail", "failure", ex)

def main(email, password, roundcube_url):
    try:
        edge_utils.open_edge()
        wait(2)
        edge_utils.search_by_url(roundcube_url)
        wait(4)
        login(email, password)
    except Exception as ex:
        logger.log("error", "Error while running main", "failure", ex)


def send_mail(recipient, subject, content, include_attachment):
    try:
        click("1690984872883.png")
        wait("1690984913880.png")
        click(Pattern("1690984962950.png").targetOffset(-105,0))
        wait(1)
        type(recipient)
        click(Pattern("1690984962950.png").targetOffset(-74,39))
        wait(1)
        type(subject)
        click(Pattern("1690985072427.png").targetOffset(11,39))
        wait(1)
        type(content)
        wait(1)
        if include_attachment == "True":
            click("1690985380051.png")
            click(Pattern("1690989162048.png").targetOffset(92,95))
            type("This PC")
            type(Key.ENTER)
            type("Local")
            type(Key.ENTER)
            click(Pattern("1690989162048.png").targetOffset(130,117))
            type("Archive")
            type(Key.ENTER)
            wait("1690989208186.png")
            click("1690989208186.png")
            wait("1690989256370.png")
            click("1690989256370.png")
            rightClick(Pattern("1690989162048.png").targetOffset(131,127))
            wait("1690989208186.png")
            click("1690989208186.png")
            wait("1690989312190.png")
            click("1690989312190.png")
            doubleClick(Pattern("1690989162048.png").targetOffset(179,130))
            doubleClick(Pattern("1690989162048.png").targetOffset(179,130))
            wait(10)
        click("1690984913880.png")
        wait(30)
        logger.log("info", "Succesfully sent mail", "success")
    except Exception as ex:
        logger.log("error", "Error while sending mail", "failure", ex)


if __name__ == "__main__":
    if len(sys.argv) < 1:
        logger.log("error", "No function name provided", "failure")
        sys.exit(1)

    function_name = sys.argv[1]

    # Args - email;password;roundcube_url
    if function_name == "main":
        email, password, roundcube_url = sys.argv[2].split(";")
        main(email, password, roundcube_url)
    # Args - email;password
    elif function_name == "login":
        email, password = sys.argv[2].split(";")
        login(email, password)
    elif function_name == "open_unread_emails":
        open_unread_emails()
    elif function_name == "scan_email":
        scan_email()
    elif function_name == "download_attachment":
        download_attachment()
    elif function_name == "open_phishing_website":
        open_phishing_website()
    elif function_name == "open_mail":
        open_mail()
    elif function_name == "filter_by_unread":
        filter_by_unread()
    elif function_name == "open_top_email":
        open_top_email()
    elif function_name == "send_mail":
        recipient, subject, content, include_attachment = sys.argv[2].split(";")
        send_mail(recipient, subject, content, include_attachment)
    else:
        logger.log("error", "Invalid function name", "failure")
        sys.exit(1)
