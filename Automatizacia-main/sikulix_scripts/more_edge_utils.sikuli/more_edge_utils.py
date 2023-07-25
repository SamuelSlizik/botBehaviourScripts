from sikuli import *
import logger
import random

def edge_scroll_images(time):
    try:
        wait("1690286144726.png")
        click("1690286144726.png")
        wait("1690286179068.png")
        for i in range(time):
            sikuli.wheel(WHEEL_DOWN, 1)
            wait(1)
        logger.log("info", "Finished scrolling images", "success")
    except FindFailed as ex:
        logger.log("error", "Error while scrolling images", "failure", ex)


def edge_watch_youtube_shorts(time):
    try:
        wait("1690290587338.png")
        click("1690290587338.png")
        wait("1690290670091.png")
        watchTime = 0;
        while (watchTime < time):
            watch = random.uniform(10.0, 60.0)
            watchTime += watch
            wait(watch)
            click("1690290670091.png")
        logger.log("info", "Finished watching youtube shorts", "success")
    except FindFailed as ex:
        logger.log("error", "Error while watching youtube shorts", "failure", ex)
        
        