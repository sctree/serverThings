import subprocess

robots = ["robot1.py", "robot2.py"]

for robot in robots:
    subprocess.run(["python3", robot])