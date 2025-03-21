#this script is for initializing the robots based on which robot is selected

import subprocess

def run_robot_script(robot_type):
    script_map = {
        "robot1": "robot1.py",
        "robot2": "robot2.py",
    }

    script_to_run = script_map.get(robot_type)

    if script_to_run:
        print(f"Running {script_to_run} for {robot_type}...")
        subprocess.run(["python", script_to_run])
    else:
        print("Robot script not found.")

robot_type = "robot1" #example. this is currently hardcoded
run_robot_script(robot_type)