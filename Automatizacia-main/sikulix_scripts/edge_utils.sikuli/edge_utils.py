from sikuli import *
import sys

# Custom modules
import logger

# Open Microsoft Edge
def open_edge():
    try:
        type(Key.WIN)
        wait(1)
        type("Microsoft Edge")
        wait(5)#wait(Pattern("1690732958740.png").similar(0.66))
        type(Key.ENTER)
        if exists(Pattern("1690005339642.png").similar(0.80)):
           click("1690005339642.png")
        logger.log("info", "Finished opening Edge", "success")
    except FindFailed as ex:
        logger.log("error", "Error while opening edge", "failure", ex)
        sys.exit(1)

def search_by_text(text):
    try:
        click("1689842566067.png")
        type(text)
        type(Key.ENTER)
        logger.log("info", "Finished searching by text: {text}".format(text=text), "success")
    except Exception as ex:
        logger.log("error", "Error while searching by text: " +text, "failure", ex)

def search_by_url(url):
    try:
        type("l", Key.CTRL)
        type(url)
        wait(1)
        type(Key.ENTER)

        logger.log("info", "Finished searching by url: {url}".format(url=url), "success")
    except Exception as ex:
        logger.log("error", "Error while searching by url: {url}".format(url=url), "failure", ex)

def close_latest_tab():
    type("w", KeyModifier.CTRL)

if __name__ == "__main__":
    if len(sys.argv) < 1:
        logger.log("error", "No function name provided", "failure")
        sys.exit(1)

    function_name = sys.argv[1]

    if function_name == "open_edge":
        open_edge()
    # Args - text
    elif function_name == "search_by_text":
        text=sys.argv[2]
        search_by_text(text)
    # Args - url
    elif function_name == "search_by_url":
        url=sys.argv[2]
        search_by_url(url)
    elif function_name == "close_latest_tab":
        close_latest_tab()
    else:
        logger.log("error", "Invalid function name", "failure")
        sys.exit(1)
