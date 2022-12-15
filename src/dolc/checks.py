import argparse
import os


def check_dir(path: str) -> str:
    "A check!"
    if os.path.isdir(path):
        return path

    raise argparse.ArgumentTypeError(f"\033[31m{path}\033[0m is not a valid path!")


def check_folder_exists(dir: str):
    if os.path.isdir("docs"):
        raise OSError("\033[31mdocs\033[0m already exists!")

    os.mkdir("docs")
