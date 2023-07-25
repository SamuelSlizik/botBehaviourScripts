folderPath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\114.0.1823.79\\ResiliencyLinks\\edge_feedback"
splitPath = folderPath.split("\\")
if (splitPath[0] == "C:"):
    splitPath.pop(0)
if (not exists("1689173481864.png")):
    click("1689157571730.png")
    wait("1689173481864.png")
    
click("1689173481864.png")
doubleClick("1689174926315.png")
click(Pattern("1689175742833.png").targetOffset(93,-2))

for pathPiece in splitPath:
    place = findText(pathPiece)
    if (place):
        doubleClick(place)
        click(Pattern("1689175742833.png").targetOffset(93,-2))