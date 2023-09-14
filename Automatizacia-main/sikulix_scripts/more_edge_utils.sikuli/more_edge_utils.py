from sikuli import *
import logger
import random


def start_edge_scroll_images():
    try:
        wait("1690286144726.png")
        click("1690286144726.png")
        wait("1690286179068.png")
        logger.log("info", "Finished start scrolling images", "success")
    except Exception as ex:
        logger.log("error", "Error while start scrolling images", "failure", ex)


def edge_scroll_images():
    wheel(WHEEL_DOWN, 1)
    wait(5)
    

def old_edge_scroll_images(time):
    try:
        convertedTime = float(time)
        wait("1690286144726.png")
        click("1690286144726.png")
        wait("1690286179068.png")
        for i in range(int(convertedTime / 5)):
            wheel(WHEEL_DOWN, 1)
            wait(5)
        logger.log("info", "Finished scrolling images", "success")
    except Exception as ex:
        logger.log("error", "Error while start scrolling images", "failure", ex)


def start_edge_watch_youtube_shorts():
    try:
        wait(3)
        if exists("1693470944627.png"):
            click("1693470944627.png")
            wheel(WHEEL_DOWN, 10)
            wait("1693471040281.png")
            click("1693471040281.png")
            wait(10)
        wait("1690290587338.png")
        click("1690290587338.png")
        wait("1690290670091.png")
        logger.log("info", "Finished start watching youtube shorts", "success")
    except Exception as ex:
        logger.log("error", "Error while watching youtube shorts", "failure", ex)


def edge_watch_youtube_shorts():
    try:
        watch = random.uniform(10.0, 20.0)
        wait(watch)
        click("1690290670091.png")    
        logger.log("info", "Finished watching youtube shorts", "success")
    except Exception as ex:
        logger.log("error", "Error while watching youtube shorts", "failure", ex)


def old_edge_watch_youtube_shorts(time):
    try:
        convertedTime = float(time)
        wait("1690290587338.png")
        click("1690290587338.png")
        wait("1690290670091.png")
        watchTime = 0
        while watchTime < convertedTime:
            watch = random.uniform(10.0, 60.0)
            watchTime += watch
            wait(watch)
            click("1690290670091.png")
        logger.log("info", "Finished watching youtube shorts", "success")
    except Exception as ex:
        logger.log("error", "Error while watching youtube shorts", "failure", ex)
        

if __name__ == "__main__":
    if len(sys.argv) < 1:
        logger.log("error", "No function name provided", "failure")
        sys.exit(1)

    function_name = sys.argv[1]

    if function_name == "old_edge_scroll_images":
        time = sys.argv[2]
        old_edge_scroll_images(time)
    elif function_name == "old_edge_watch_youtube_shorts":
        time = sys.argv[2]
        old_edge_watch_youtube_shorts(time)
    elif function_name == "edge_scroll_images":
        edge_scroll_images()
    elif function_name == "edge_watch_youtube_shorts":
        edge_watch_youtube_shorts()
    elif function_name == "start_edge_scroll_images":
        start_edge_scroll_images()
    elif function_name == "start_edge_watch_youtube_shorts":
        start_edge_watch_youtube_shorts()