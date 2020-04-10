#!/usr/bin/env python

from glob import glob
import os
from pathlib import Path
import sys


if __name__ == '__main__':
    if 'DATA_DIR' in os.environ:
        data_dir = Path(os.environ['DATA_DIR'])
        print(f"### info: looking for data in '{data_dir}'", file=sys.stderr)
        total = 0.0
        for data_file in data_dir.glob('*.txt'):
            with open(data_file, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        total += float(line)
                    except ValueError as error:
                        print(f'### warning: {error}', file=sys.stderr)
        print(f'total = {total}')
    else:
        print('### error: DATA_DIR not set', file=sys.stderr)
