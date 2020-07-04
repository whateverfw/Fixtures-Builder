import sys
from typing import List

from utils.validators import validate_type, file_exists
from utils.helpers import get_file_extension
from utils.exceptions import InputError
from src.worker import execute_reader


def get_user_input() -> List[str]:
    return sys.argv


def validate_file(file: str) -> None:
    file_exists(file)
    file_extension = get_file_extension(file)
    validate_type(file_extension)


def handle_initial_data() -> str:
    try:
        script_name, file = get_user_input()
    except Exception:
        raise InputError
    validate_file(file)

    return file


def main() -> None:
    file = handle_initial_data()
    file_extension = get_file_extension(file)
    execute_reader(file, file_extension)


if __name__ == '__main__':
    main()
