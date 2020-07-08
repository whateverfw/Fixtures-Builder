import pandas as pd

from src.common import build_json_fixture
from src.handle_output import write_to_json
from utils.file_handler import get_file_from_user_input, get_full_path_to_file
from utils.validators import validate_file


def json_main() -> None:
    file_name = get_file_from_user_input()
    validate_file(file_name)
    read_json(file_name)


def read_json(file_name: str) -> None:
    path_to_file = get_full_path_to_file(file_name)
    json_data = get_json_data(path_to_file)
    data = build_json_fixture(json_data)
    write_to_json(data)


def get_json_data(path_to_file: str) -> pd.DataFrame:
    return pd.read_json(path_to_file)