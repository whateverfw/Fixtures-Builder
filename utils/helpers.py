from pathlib import Path


def get_file_extension(file: str) -> str:
    return Path(file).suffix


