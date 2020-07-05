import json
from typing import List


def write_to_json(data: List) -> None:
    output_file_name = get_output_file_name()
    with open(f'{output_file_name}.json', 'w') as json_fixtures:
        json.dump(data, json_fixtures)


def get_output_file_name() -> str:
    return input(
        'What output file name should be? (Do not specify .json extension [e.g. countries, not countries.json] \n'
    )
