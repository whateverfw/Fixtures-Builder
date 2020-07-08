from os import path
from typing import Tuple, List

import pandas as pd

from utils.exceptions import FileTypeError, MissingFileError, ModeTypeError, InvalidColumnsAmountError
from utils.file_handler import get_file_extension


def file_exists(file_name) -> None:
    if not path.exists(file_name):
        raise MissingFileError(file_name)


def validate_extension(file_extension: str) -> None:
    allowed_extensions = ['.csv', '.json', '.xlsx', ]
    if file_extension not in allowed_extensions:
        raise FileTypeError(allowed_extensions)


def validate_file(file_name: str) -> Tuple[str, str]:
    file_exists(file_name)
    file_extension = get_file_extension(file_name)
    validate_extension(file_extension)
    return file_name, file_extension


def validate_input_mode(input_mode) -> None:
    allowed_modes = ['manual', 'csv', 'json', 'excel', 'sql']
    if input_mode not in allowed_modes:
        raise ModeTypeError(allowed_modes)
