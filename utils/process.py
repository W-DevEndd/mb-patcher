import subprocess

def run(command: str):

    args = command.split()
    return subprocess.run(args)
