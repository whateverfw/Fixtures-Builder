from src.handle_csv import csv_main
from src.handle_manual import manual_main
from src.handle_json import json_main


GO_TO_NEXT_STAGE = {
    'manual': manual_main,
    'csv':  csv_main,
    'json': json_main,
}


def execute_reader(input_model: str) -> None:
    GO_TO_NEXT_STAGE[input_model]()
