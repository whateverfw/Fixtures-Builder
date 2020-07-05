from pathlib import Path


def get_file_extension(file: str) -> str:
    return Path(file).suffix


def get_file_from_user_input() -> str:
    return input('Please input name of your file: ')



