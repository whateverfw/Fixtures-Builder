from pathlib import Path

from constants import PROJECT_ROOT


def get_file_extension(file: str) -> str:
    return Path(file).suffix


def get_file_from_user_input() -> str:
    return input('Please input name of your file: ')


def get_full_path_to_file(file_name: str) -> str:
    return f'{PROJECT_ROOT}/{file_name}'
