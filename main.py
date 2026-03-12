from utils.setup import init, clean
import sys

init()
if (len(sys.argv) > 1):
    if (sys.argv[1] == "clean"): clean()