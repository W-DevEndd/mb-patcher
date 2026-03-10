
import os, shutil
from pathlib import Path

config = ".config.py"
inp = Path(".inp")
out = Path(".out")

def init():
    os.makedirs(out, exist_ok=True)
    os.makedirs(inp, exist_ok=True)

    if not os.path.isfile(config):
        shutil.copyfile(Path("resources") / "config.py", config)