from typing import List, Dict

import pandas as pd


def get_primary_key_start_value() -> int:
    try:
        return int(input('Please input primary key value, which will be initial for fixture [DEFAULT IS 1]: '))
    except ValueError:
        return 1


def get_model_name() -> str:
    return input('Please input your model name [e.g. app.model]: ')


def get_column_names() -> List[str]:
    return input('Enter column names separated by space: ').split(' ')


def build_json_fixture(original_data: pd.DataFrame) -> List[Dict]:
    pk = get_primary_key_start_value()
    model = get_model_name()
    data = []
    for _, row in original_data.iterrows():
        fields = {}
        for header in original_data.columns:
            fields[header] = row[header]
        row = {
            'pk': pk,
            'model': model,
            'fields': fields
        }
        pk += 1
        data.append(row)

    return data
