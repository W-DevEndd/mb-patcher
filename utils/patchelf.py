from pathlib import Path
import subprocess, os

def executable():
    if os.access("patchelf"):
        return 0
    else:
        raise RuntimeError()


def add_needed(dependacy: Path, target: Path):
    return subprocess.run(
        ["patchelf", "--add-needed", str(dependacy), str((target))]
    )