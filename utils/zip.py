from _typeshed import StrPath
import os
import zipfile
from pathlib import Path


def extract(zip_file: StrPath, menber: zipfile.ZipInfo | str, destination_dir: StrPath):
    if not os.path.isfile(zip_file): raise FileExistsError(f"The path {zip_file} is not a file")
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
            zip_ref.extract(menber, path=destination_dir)
            print(f"Extracted {menber} fron {zip_file} to {destination_dir}")

def add(zip_file: StrPath, file_target: StrPath, to_menber: StrPath):
    if not os.path.isfile(zip_file): raise FileExistsError(f"The path {zip_file} is not a file")
    with zipfile.ZipFile(zip_file, "a") as zip_ref:
        zip_ref.write(file_target, arcname=to_menber)