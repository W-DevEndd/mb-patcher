from pathlib import Path
from utils import zip_tools
from utils.init import init

init()

zip_tools.extract(
    Path("/data/data/com.termux/files/home/Downloads/Minecraft PE 1.26.3.1 v8a.apk"),
    "lib/arm64-v8a/libminecraftpe.so",
    Path(".out/"),
)