import json
import os
import string
from typing import Dict, List

MAIN_FOLDER = 'CustomLevels'  # Change this if you are using other folders.

# Change these to use different keys in info.dat
PREFIX = '_songName'
SUFFIX = '_levelAuthorName'

CONNECT = '-'  # This is used to connect prefix and suffix


def load_info(level_folder: str) -> Dict:
    """Return the information of the custom level in <level_folder>."""
    info_file = open(MAIN_FOLDER + f'/{level_folder}/info.dat')
    info = json.load(info_file)
    info_file.close()
    return info


def load_folders() -> List[str]:
    """Return all direct subfolders in <MAIN_FOLDER>"""
    things = os.listdir(MAIN_FOLDER)
    dirs = []
    for thing in things:
        if not os.path.isfile(MAIN_FOLDER + f'/{thing}'):
            dirs.append(thing)
    return dirs


def rename(level_folder: str) -> None:
    """Rename a custom level folder to the correct name."""
    prefix = load_info(level_folder)[PREFIX].strip()
    suffix = load_info(level_folder)[SUFFIX].strip()
    prefix = prefix.translate(str.maketrans('', '', string.punctuation))
    suffix = suffix.translate(str.maketrans('', '', string.punctuation))
    new_name = f'{prefix} {CONNECT} {suffix}'
    os.rename(MAIN_FOLDER + f'/{level_folder}',
              MAIN_FOLDER + f'/{new_name}')
    print(f"'{level_folder}' is renamed to '{new_name}'.")


if __name__ == '__main__':
    print(f"Directories in '{MAIN_FOLDER}' will be automatically renamed.")
    choice = input('Please confirm. [Y/N]').lower()
    if choice == 'y':
        print('')
        for folder in load_folders():
            rename(folder)
        print('')
        print(f"Directories in '{MAIN_FOLDER}' were renamed successfully.")
        print('Process done.')
    else:
        print("Process aborted.")
    print('\a')
    os.system("pause")

