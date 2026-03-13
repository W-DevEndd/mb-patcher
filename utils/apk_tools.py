import zipfile, shutil
from pathlib import Path

def check(apk_p: Path):
    if not zipfile.is_zipfile(apk_p): raise ValueError("The files is not zip.")

def extract(apk_p: Path, member: str, dest_dir: Path):
    check(apk_p)
    with zipfile.ZipFile(apk_p) as apk:
        with apk.open(member, "r") as src:
            dest_dir.mkdir(parents=True, exist_ok=True)
            with open(dest_dir / Path(member).name, "wb") as dst:
                shutil.copyfileobj(src, dst)

def add(apk_p: Path, file: Path, to_member: str):
    check(apk_p)
    with zipfile.ZipFile(apk_p, "w") as apk:
        apk.write(file, to_member)

def sign(apk_p: Path):
    check(apk_p)

    if not shutil.which("apksigner"):
        raise RuntimeError("\n".join([
            "apksigner is not installed in system or not executable.",
            "Open https://developer.android.com/studio or use package manager to install",
        ]))

    # ...
