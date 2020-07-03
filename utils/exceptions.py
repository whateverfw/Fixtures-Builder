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
    def __init__(self, allowed_types) -> None:
        self.message = f'''
            This type is not supported.
            Should be one of the following {allowed_types}
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

