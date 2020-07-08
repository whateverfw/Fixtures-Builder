from typing import List, Dict

from src.common import get_column_names, get_primary_key_start_value, get_model_name
from src.handle_output import write_to_json


def manual_main() -> None:
    column_names = get_column_names()
    objects_number = get_objects_number()
    data = get_data(column_names, objects_number)
    write_to_json(data)


def get_data(column_names: List[str], objects_number: int) -> List[Dict]:
    pk = get_primary_key_start_value()
    model = get_model_name()
    data = []
    for item in range(objects_number):
        fields = {}
        print(f'pk={pk}')
        print('---------------------')
        for row in column_names:
            fields[row] = input(f'{row}: ')
        print('---------------------')
        row = {
            'pk': pk,
            'model': model,
            'fields': fields,
        }
        pk += 1
        data.append(row)

    return data


def get_objects_number() -> int:
    return int(input('How much objects do you want to enter? [DEFAULT IS 1] '))
