import os
import subprocess

def run_command(command):
    # Replace 'command' with the actual command to be executed
    output = subprocess.check_output(command, stderr=subprocess.STDOUT).decode('utf-8')
    print(f"Command Output:\n{output}")
    
# Example usage of the function
run_command("ls -l")
