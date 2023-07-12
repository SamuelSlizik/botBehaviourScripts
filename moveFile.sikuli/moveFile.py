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
click("1689157571730.png")
wait("1689157669910.png")
click("1689157669910.png")
wait("1689157796776.png")
click(Pattern("1689157796776.png").targetOffset(10,65))
rightClick(Pattern("1689157796776.png").targetOffset(10,65))
wait("1689162068181.png")
click(Pattern("1689162068181.png").targetOffset(-80,10))
click("1689160215495.png")
doubleClick("1689158399441.png")
wait("1689158871982.png")
doubleClick(Pattern("1689158871982.png").targetOffset(19,64))
wait("1689162297972.png")
rightClick(Pattern("1689162297972.png").targetOffset(44,78))
wait("1689162365910.png")
click(Pattern("1689162365910.png").targetOffset(-66,-5))
