import re


def create(file_name):
    with open('.cl_logger.txt', 'w') as file:
        print(f'file = {file_name}', file=file)

def _get_log_file():
    with open('.cl_logger.txt', 'r') as file:
        for line in file:
            if match := re.match('file = (.+)', line):
                return match[1]
