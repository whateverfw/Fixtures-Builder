import pandas as pd

from constants import PROJECT_ROOT


def csv_main(file: str) -> None:
    read_csv(file)


def read_csv(file: str) -> None:
    path_to_file = f'{PROJECT_ROOT}/{file}'
    delimiter = get_delimiter()
    data = pd.read_csv(path_to_file, delimiter=delimiter)


def get_delimiter() -> str:
    return input('Please enter delimiter in your csv file:')
