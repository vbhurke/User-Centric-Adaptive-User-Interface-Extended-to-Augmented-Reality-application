import subprocess
import os
import time


script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the main script

# Run the "wf_dataprocessing.py" script
subprocess.call(["python", os.path.join(script_dir, "wf_dataprocessing.py")])

# Run the "wf_visualization.py" script
subprocess.call(["python", os.path.join(script_dir, "wf_visualization.py")])
