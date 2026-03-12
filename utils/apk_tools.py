import zipfile, shutil
from pathlib import Path

def check(apk_p: Path):
    if not zipfile.is_zipfile(Path): raise ValueError("The files is not zip.")

def extract(apk_p: Path, member: str, dest_dir: Path):
    check()
    with zipfile.ZipFile(apk_p) as apk:
        with apk.open(member, "r") as src:
            dest_dir.mkdir(parents=True, exist_ok=True)
            with open(dest_dir / Path(member).name, "wb") as dst:
                shutil.copyfileobj(src, dst)

def add(apk_p: Path, file: Path, to_member: str):
    check()
    with zipfile.ZipFile(apk_p, "w") as apk:
        apk.write(file, to_member)