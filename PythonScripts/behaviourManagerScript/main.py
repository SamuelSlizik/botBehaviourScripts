import subprocess

command = ["C:\\sikulixide.jar", "-r", "C:\BotBehaviourScripts\checkTodaysFolder.sikuli"]

subprocess.run(command, check=True)

print("HELP")

input("Press Enter to continue...")