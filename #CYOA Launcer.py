#CYOA Launcer
import subprocess
#find the path
CYOA_file = "D:\coding\DNDgame\chooseyourownadventure.py"

#launch the game
subprocess.Popen(f'start cmd /k python "{CYOA_file}"', shell=True)