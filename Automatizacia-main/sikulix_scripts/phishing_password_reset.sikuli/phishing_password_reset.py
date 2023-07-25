from sikuli import  *
import sys

# Custom modules
import logger
import edge_utils

def enter_email(email):
    try:
        type(Key.TAB)
        wait(0.5)
        type(email)
        wait(0.5)
        type(Key.ENTER)
        logger.log("info", "Entered phish email credentials", "success")
    except Exception as ex:
        logger.log("error", "Error while entering phish email credentials", "failure", ex)

def enter_password(password):
    try:
        type(Key.TAB)
        type(Key.TAB)
        wait(0.5)
        type(password)
        wait(0.5)
        type(Key.ENTER)
        logger.log("info", "Entered phish password credentials", "success")
    except Exception as ex:
        logger.log("error", "Error while entering phish password credentials", "failure", ex)

def main(email, password):
    try:
        enter_email(email)
        wait(2)
        enter_password(password)    
        wait(3)
        logger.log("info", "Entered phishing credentials", "success")

        # Microsoft page
        edge_utils.close_latest_tab()
    except Exception as ex:
        logger.log("error", "Error while running main", "failure", ex)

if __name__ == "__main__":
    if len(sys.argv) < 1:
        logger.log("error", "No function name provided", "failure")
        sys.exit(1)

    function_name = sys.argv[1]

    # Args - email, password
    if function_name == "main":
        email, password = sys.argv[2].split(";")
        main(email, password)
    else:
        logger.log("error", "Invalid function name", "failure")
        sys.exit(1)
