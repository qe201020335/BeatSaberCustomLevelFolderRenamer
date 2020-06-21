import json
import os
import string
from typing import Dict, List

MAIN_FOLDER = 'CustomLevels'


def load_info(level_folder: str) -> Dict:
    info_file = open(MAIN_FOLDER + f'/{level_folder}/info.dat')
    info = json.load(info_file)
    info_file.close()
    return info


def load_folders() -> List[str]:
    things = os.listdir(MAIN_FOLDER)
    dirs = []
    for thing in things:
        if not os.path.isfile(MAIN_FOLDER + f'/{thing}'):
            dirs.append(thing)
    return dirs


def rename(level_folder: str) -> None:
    lvl_name = load_info(level_folder)['_songName'].strip().\
        translate(str.maketrans('', '', string.punctuation))
    lvl_author = load_info(level_folder)['_levelAuthorName'].strip().\
        translate(str.maketrans('', '', string.punctuation))
    new_name = f'{lvl_name} - {lvl_author}'
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

