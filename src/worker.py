from src.handle_csv import csv_main

GO_TO_NEXT_STAGE = {
    '.csv':  csv_main
}


def execute_reader(file: str, file_extension: str) -> None:
    GO_TO_NEXT_STAGE[file_extension](file)
