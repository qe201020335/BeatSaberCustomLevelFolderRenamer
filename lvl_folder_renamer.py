import json
import os
import string
from typing import Dict, List

MAIN_FOLDER = 'CustomLevels'  # Change this if you are using other folders.

# Change these to use different keys in info.dat
PREFIX = '_songName'
SUFFIX = '_levelAuthorName'

CONNECT = '-'  # This is used to connect prefix and suffix

FORCED = False


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


def rename(level_folder: str) -> int:
    """Rename a custom level folder to the correct name."""
    prefix = load_info(level_folder)[PREFIX].strip()
    suffix = load_info(level_folder)[SUFFIX].strip()
    prefix = prefix.translate(str.maketrans('', '', string.punctuation))
    suffix = suffix.translate(str.maketrans('', '', string.punctuation))
    new_name = f'{prefix} {CONNECT} {suffix}'.strip()
    if new_name != level_folder or FORCED:
        os.rename(MAIN_FOLDER + f'/{level_folder}',
                  MAIN_FOLDER + f'/{new_name}')
        print(f"'{level_folder}' is renamed to '{new_name}'.")
        return 1
    return 0


def main() -> None:
    """Main function."""
    print(f"Directories in '{MAIN_FOLDER}' will be automatically renamed.")
    print('Forced rename is', FORCED)
    choice = input('Please confirm. [Y/N]').lower()
    processed = 0
    renamed = 0
    if choice == 'y':
        print('')
        for folder in load_folders():
            renamed += rename(folder)
            processed += 1
        print('')
        print('Process done.')
    else:
        print("Process aborted.")
    print(f'{processed} directories processed, {renamed} renamed.')
    print('\a')
    os.system("pause")


if __name__ == '__main__':
    main()
