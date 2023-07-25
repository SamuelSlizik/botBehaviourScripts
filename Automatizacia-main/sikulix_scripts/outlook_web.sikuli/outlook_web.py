from sikuli import *
import sys

# Custom modules
import logger
import edge_utils

# Function declaration
def login(email, password):
    try:
        type(email)
        wait(0.5)
        type(Key.ENTER)
        wait(3)
        type(password)
        wait(0.5)
        type(Key.ENTER)
        if exists("1689844929770.png"):
            click("1689844951354.png")
            wait(0.5)
            click("1689844984139.png")

        logger.log("info", "Logged into outlook web as user: {email}".format(email=email), "success")
    except Exception as ex:
        logger.log("error", "Error while logging into outlook", "failure", ex)

def main(email, password, outlook_url):
    try:
        edge_utils.open_edge()
        wait(1)
        edge_utils.search_by_url(outlook_url)
        wait(3)
        login(email, password)
        logger.log("info", "Finished outlook main", "success")
    except Exception as ex:
        logger.log("error", "Error while running main", "failure", ex)

if __name__ == "__main__":
    if len(sys.argv) < 1:
        logger.log("error", "No function name provided", "failure")
        sys.exit(1)

    function_name = sys.argv[1]

    # Args - email;password;outlook_url
    if function_name == "main":
        email, password, outlook_url = sys.argv[2].split(";")
        main(email, password, outlook_url)
    elif function_name == "login":
        email, password = sys.argv[2].split(";")
        login(email, password)