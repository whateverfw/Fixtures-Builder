from os import path

from utils.exceptions import FileTypeError, MissingFileError


def file_exists(file) -> None:
    if not path.exists(file):
        raise MissingFileError(file)


def validate_type(file_type) -> None:
    allowed_types = ['.csv', '.json', '.xlsx', ]
    if file_type not in allowed_types:
        raise FileTypeError(allowed_types)
