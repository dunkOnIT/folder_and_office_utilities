import json
from decouple import config
from pathlib import Path
from typing import Union

def create_folders_from_json(root_path: Union[str, Path, None], json_source_path: Union[str, Path]):
    """Takes as input a root folder and a path to a JSON file containing a folder structure, and creates
    the folder structure from the JSON file inside the root path."""

def create_folders_from_list(root_path: Union[Path, None], folders_to_create: list[str]) -> None:
    """Creates a folder for each string in folders_to_create at the root_path"""

    for folder in folders_to_create:
        if root_path is None: # If no root path is specified, create folders at the current directory
            Path(folder).mkdir()
        else: # If a root path is specified, create a directory at the location of the root directory
            root_path.joinpath(folder).mkdir()


def main():
    create_folders_from_list(Path("Investors"), json.loads(config("INVESTOR_NAMES")))

if __name__ == "__main__":
    main()