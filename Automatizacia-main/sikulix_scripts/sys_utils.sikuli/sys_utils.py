from sikuli import *
import os
import logger

# CTRL + SHIFT + 6 = file explorer view details
def set_sort_by_date():
    try:
        click("1689242090615.png")
        wait("1689242100443.png")
        click("1689242100443.png")
        wait("1689242125333.png")
        click("1689242125333.png")
        logger.log("info", "Finished setting sort by date", "success")
    except Exception as ex:
        logger.log("error", "Error while setting sort by date", "failure", ex)


def open_top_file():
    try:
        doubleClick(Pattern("1690984136705.png").targetOffset(159,211))
        wait(30)
        logger.log("info", "Finished opening top file", "success")
    except Exception as ex:
        logger.log("error", "Error while opening top file", "failure", ex)


def get_file_extension():
    type(Key.F2)
    wait(0.5)
    type(Key.RIGHT)
    wait(0.5)
    for i in range(20):
        type(Key.RIGHT, Key.SHIFT)
        wait(0.1)
    copy()
    escape()
    clipboard_content = Env.getClipboard()
    logger.log("info", "{clipboard}".format(clipboard=clipboard_content), "success")


def check_or_create_folder(path):
    try:
        splitPath = path.split("\\")
        if splitPath[0] == "C:":
            splitPath.pop(0)
        if not exists("1689173481864.png"):
            if not exists("1689157571730.png"):
                type("e", Key.WIN)
            else:
                click("1689157571730.png")
            wait("1689173481864.png")
        
        click("1689173481864.png")
        doubleClick("1689174926315.png")
        partialPath = "C:"
        
        for pathPiece in splitPath:
            partialPath += "\\" + pathPiece
            if not os.path.isdir(partialPath):
                logger.log("info", "Created new folder: {path}".format(path=partialPath), "success")
                if not exists("1690288251385.png"):
                    click("1690288271258.png")
                    wait("1690288251385.png")
                click("1690288251385.png")
                wait(1)
                type(pathPiece)
                type(Key.ENTER)
            else:
                type(pathPiece)
            wait(1)
            type(Key.ENTER)
        logger.log("info", "Finished checking folder: {path}".format(path=path), "success")
    except Exception as ex:
        logger.log("error", "Error while checking folder: {path}, on level: {subPath}".format(path=path, subPath=partialPath), "failure", ex)


def altf4():
    type(Key.F4, KeyModifier.ALT)


def selectFile(path):
    try:
        if not os.path.exists(partialPath):
            raise Exception("File {file} doesn't exist!".format(file=path))
        
        splitPath = path.split("\\")
        if splitPath[0] == "C:":
            splitPath.pop(0)

        item = splitPath.pop()
        
        if not exists("1689173481864.png"):
            if not exists("1689157571730.png"):
                type("e", Key.WIN)
            else:
                click("1689157571730.png")
            wait("1689173481864.png")
        
        click("1689173481864.png")
        doubleClick("1689174926315.png")
        partialPath = "C:"
        
        for pathPiece in splitPath:
            partialPath += "\\" + pathPiece
            type(pathPiece)
            wait(1)
            type(Key.ENTER)

        type(item)
        wait(1)
        
        logger.log("info", "Finished selecting file: {path}".format(path=path), "success")
    except Exception as ex:
        logger.log("error", "Error while selecting file: {path}, on level: {subPath}".format(path=path, subPath=partialPath), "failure", ex)


def escape():
    type(Key.ESC)


def copy():
    type("c", Key.CTRL)


def cut():
    type("x", Key.CTRL)


def pasteClipboard():
    # TODO: add recognition of duplicate files
    type("v", Key.CTRL)


def rename(name):
    wait(1)
    type(Key.F2)
    wait(1)
    type(name)
    wait(1)
    type(Key.ENTER)
    wait(1)


def selectLastFromDownloads():
    try:
        if (not exists("1689157669910.png")):
            if not exists("1689157571730.png"):
                type("e", Key.WIN)
            else:
                click("1689157571730.png")
            wait("1689157669910.png")
        doubleClick("1689157669910.png")
        wait("1689157796776.png")
        click(Pattern("1689157796776.png").targetOffset(10,65))
        logger.log("info", "Finished selecting last file from downloads", "success")
    except Exception as ex:
        logger.log("error", "Error while selecting last file from downloads", "failure", ex)


if __name__ == "__main__":
    if len(sys.argv) < 1:
        logger.log("error", "No function name provided", "failure")
        sys.exit(1)

    function_name = sys.argv[1]

    if function_name == "get_file_extension":
        get_file_extension()

    elif function_name == "check_or_create_folder":
        path = sys.argv[2]
        check_or_create_folder(path)

    elif function_name == "selectFile":
        path = sys.argv[2]
        selectFile(path)

    elif function_name == "altf4":
        altf4()

    elif function_name == "copy":
        copy()

    elif function_name == "cut":
        cut()

    elif function_name == "escape":
        escape()

    elif function_name == "pasteClipboard":
        pasteClipboard()

    elif function_name == "selectLastFromDownloads":
        selectLastFromDownloads()

    elif function_name == "set_sort_by_date":
        set_sort_by_date()

    elif function_name == "open_top_file":
        open_top_file()

    elif function_name == "rename":
        name = sys.argv[2]
        rename(name)

    else:
        logger.log("error", "Invalid function name", "failure")
        sys.exit(1)
        