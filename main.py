import sys
from typing import List
from pathlib import Path

from utils.validators import validate_type, file_exists
from utils.exceptions import InputError
from file_handler import FileHandler

file_handler = FileHandler()


def get_user_input() -> List[str]:
    return sys.argv


def handle_initial_data() -> None:
    try:
        script_name, file = get_user_input()
    except Exception:
        raise InputError
    file_exists(file)
    file_extension = Path(file).suffix
    validate_type(file_extension)


def main() -> None:
    handle_initial_data()


if __name__ == '__main__':
    main()
