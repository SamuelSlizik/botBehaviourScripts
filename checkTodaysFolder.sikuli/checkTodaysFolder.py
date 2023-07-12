import os
from datetime import datetime

archivePath = "C:\\Archive"
date = datetime.now().strftime("%Y-%m-%d")

todaysFolderPath = archivePath + "\\" + date
doubleClick("1689158399441.png")
wait("1689158871982.png")
if (not os.path.isdir(todaysFolderPath)):
        rightClick(Pattern("1689158871982.png").targetOffset(54,126))
        wait("1689159094707.png")
        click(Pattern("1689159094707.png").targetOffset(-41,95))
        wait("1689159275778.png")
        click(Pattern("1689159275778.png").targetOffset(-54,-11))
        wait("1689159337691.png")
        type(date + Key.ENTER)
        
click("1689160215495.png")