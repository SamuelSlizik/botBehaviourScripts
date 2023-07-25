from sikuli import *
import logger

def edge_scroll_images(time):
    try:
        click("1690286144726.png")
        wait("1690286179068.png")
        for i in range(time):
            sikuli.wheel(WHEEL_DOWN, 1)
            wait(1)
        logger.log("info", "Finished scrolling images", "success")
    except FindFailed as ex:
        logger.log("error", "Error while scrolling images", "failure", ex)



        