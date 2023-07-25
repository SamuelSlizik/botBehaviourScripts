from sikuli import *
import os
import logger

def check_or_create_folder(path):
    try:
        splitPath = pathath.split("\\")
        if (splitPath[0] == "C:"):
            splitPath.pop(0)
        if (not exists("1689173481864.png")):
            click("1689157571730.png")
            wait("1689173481864.png")
        
        click("1689173481864.png")
        doubleClick("1689174926315.png")
        partialPath = "C:"
        
        for pathPiece in splitPath:
            partialPath += "\\" + pathPiece
            if (not os.path.isdir(partialPath)):
                logger.log("info", "Created new folder: {path}".format(path=partialPath), "success")
                if (not exists("1690288251385.png")):
                    click("1690288271258.png")
                    wait("1690288251385.png")
                click("1690288251385.png")
                type(pathPiece)
                type(Key.ENTER)
            else:
                type(pathPiece)
            wait(1)
            type(Key.ENTER)
        logger.log("info", "Finished checking folder: {path}".format(path=path), "success")
    except FindFailed as ex:
        logger.log("error", "Error while checking folder: {path}, on level: {subPath}".format(path=path, subPath=partialPath), "failure", ex)
        