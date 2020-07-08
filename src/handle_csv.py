import pandas as pd

from src.handle_output import write_to_json
from src.common import build_json_fixture, get_column_names
from utils.file_handler import get_file_from_user_input, get_full_path_to_file
from utils.validators import validate_file


def csv_main() -> None:
    file_name = get_file_from_user_input()
    validate_file(file_name)
    read_csv(file_name)


def read_csv(file_name: str) -> None:
    path_to_file = get_full_path_to_file(file_name)
    delimiter = get_delimiter()
    csv_data = get_csv_data(path_to_file, delimiter)
    data = build_json_fixture(csv_data)
    write_to_json(data)


def get_csv_data(path_to_file: str, delimiter: str) -> pd.DataFrame:
    if input('Csv file contain columns headers? (Yes to confirm, any other key will mean No): ') == 'Yes':
        return pd.read_csv(path_to_file, sep=delimiter)

    column_names = get_column_names()
    return pd.read_csv(path_to_file, sep=delimiter, names=column_names, header=None)


def get_delimiter() -> str:
    return input('Please enter delimiter in your csv file: ')
