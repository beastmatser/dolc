import argparse

from dolc.checks import check_dir
from dolc.checks import check_folder_exists
from dolc.retrieve import find_file_structure
from dolc.synthese import create_docs


def main():
    """
    The main function of dolc
    """
    parser = argparse.ArgumentParser(
        prog="dolc",
        description="Turn your documented python code into markdown files.",
    )
    parser.add_argument(
        "dir",
        type=check_dir,
        help="The package you want to generate markdown for.",
    )
    args = parser.parse_args()
    check_dir(args.dir)
    check_folder_exists(args.dir)
    create_docs(find_file_structure(args.dir))
