import ast
import os
from ast import ClassDef
from ast import FunctionDef
from typing import Any
from typing import Dict
from typing import List
from typing import Union


def find_file_structure(dir):
    file_structure: Dict[str, Any] = {}

    for root, _, files in os.walk(dir):
        current_dir = file_structure

        for subdir in root.split(os.path.sep)[1:]:
            current_dir = current_dir.setdefault(subdir, {})

        for file in files:
            if not file.endswith(".py"):
                continue

            current_dir[file] = None

    return remove_empty_folders(file_structure)


def remove_empty_folders(file_struct):
    for k, v in list(file_struct.items()):
        if isinstance(v, dict) and not v:
            del file_struct[k]
        elif isinstance(v, dict):
            remove_empty_folders(v)
    return file_struct


def find_objects(files: List[Any]) -> Dict[str, List[Union[FunctionDef, ClassDef]]]:
    objects = {}
    for file in files:
        fp = open(file)
        objects[file] = [
            obj
            for obj in ast.parse(fp.read()).body
            if isinstance(obj, (ast.FunctionDef, ast.ClassDef))
        ]
        fp.close()

    return objects


def find_docstrings(files):
    pass
