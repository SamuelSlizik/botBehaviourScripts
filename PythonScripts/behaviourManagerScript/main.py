import subprocess

command = ["java", "-jar", "C:/sikulixide.jar", "-r", "C:/BotBehaviourScripts/checkTodaysFolder.sikuli"]

subprocess.run(command, check=True)

input("Press Enter to continue...")