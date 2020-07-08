from typing import List


def get_primary_key_start_value() -> int:
    try:
        return int(input('Please input primary key value, which will be initial for fixture [DEFAULT IS 1]: '))
    except ValueError:
        return 1


def get_model_name() -> str:
    return input('Please input your model name [e.g. app.model]: ')


def get_column_names() -> List[str]:
    return input('Enter column names separated by space: ').split(' ')


