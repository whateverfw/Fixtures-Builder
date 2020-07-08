class InputError(Exception):
    def __init__(self) -> None:
        self.message = f'''
            Expected 2 arguments, got 1
            You should run script via: <script_name> <file_name>
            e.g. >> main.py somename.csv
            '''

    def __str__(self) -> str:
        return self.message


class FileTypeError(Exception):
    def __init__(self, allowed_extensions) -> None:
        self.message = f'''
            This type is not supported.
            Should be one of the following {allowed_extensions}
        '''

    def __str__(self) -> str:
        return self.message


class ModeTypeError(Exception):
    def __init__(self, allowed_modes) -> None:
        self.message = f'''
            This input mode is not supported.
            Should be one of the following {allowed_modes}
        '''

    def __str__(self) -> str:
        return self.message


class MissingFileError(Exception):
    def __init__(self, file) -> None:
        self.message = f'''
            File {file} was not found in project directory.
            Remember that file should be placed in the same directory as <main.py>
        '''

    def __str__(self) -> str:
        return self.message


class InvalidColumnsAmountError(Exception):
    def __init__(self, user_columns_count, data_columns_count) -> None:
        self.message = f'''
            Number of columns that you specified - {user_columns_count} is greater than
            number of columns in csv file - {data_columns_count}
        '''

    def __str__(self) -> str:
        return self.message
