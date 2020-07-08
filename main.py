import sys
from typing import List

from src.worker import execute_reader
from utils.validators import validate_input_mode
from utils.exceptions import InputError


def get_user_input() -> List[str]:
    return sys.argv


def handle_initial_data() -> str:
    try:
        script_name, input_mode = get_user_input()
    except Exception:
        raise InputError
    validate_input_mode(input_mode)

    return input_mode


def main() -> None:
    input_mode = handle_initial_data()
    execute_reader(input_mode)


if __name__ == '__main__':
    main()
