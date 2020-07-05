from typing import List, Tuple

import pandas as pd


from constants import PROJECT_ROOT
from utils.file_handler import get_file_from_user_input
from utils.validators import validate_file, validate_csv_data


def csv_main() -> None:
    file_name = get_file_from_user_input()
    validate_file(file_name)
    read_csv(file_name)


def read_csv(file_name: str) -> None:
    path_to_file = f'{PROJECT_ROOT}/{file_name}'
    delimiter = get_delimiter()
    csv_data = get_csv_data(path_to_file, delimiter)


def get_csv_data(path_to_file: str, delimiter: str) -> pd.DataFrame:
    if input('Csv file contain columns headers? (Yes to confirm, any other key will mean No): ') == 'Yes':
        return pd.read_csv(path_to_file, sep=delimiter)

    column_names = get_column_names()
    return pd.read_csv(path_to_file, sep=delimiter, names=column_names, header=None)


def get_delimiter() -> str:
    return input('Please enter delimiter in your csv file: ')


def get_column_names() -> List[str]:
    return input('Enter column names separated by space: ').split(' ')
