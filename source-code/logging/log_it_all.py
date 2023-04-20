#!/usr/bin/env python

from argparse import ArgumentParser
import logging
import math
from pathlib import Path
import sys


def do_stuff(n):
    if n < 0:
        logging.error(f'can not do stuff for {n}')
        return 1
    for i in range(n):
        logging.info(f'doing stuff {i}')
        print(f'doing {i}: {math.sqrt(i):.4f}')
        logging.info(f'done stuff {i}')
    return 0


def main():
    arg_parser = ArgumentParser(description='example for logging facility')
    arg_parser.add_argument('--log', dest='log_file',
                            help='name of log file')
    arg_parser.add_argument('--info', action='store_true',
                            help='set log level to info')
    arg_parser.add_argument('--new_log', action='store_true',
                            help='overwrite existing log file')
    arg_parser.add_argument('--n', type=int, default=1,
                            help='number of times to do stuff')
    options = arg_parser.parse_args()
    format_str = '%(asctime)s:%(levelname)s:%(message)s'
    if options.info:
        level = logging.INFO
    else:
        level = logging.WARNING
    if options.new_log:
        filemode = 'w'
    else:
        filemode = 'a'
    if options.log_file:
        log_file = Path(options.log_file)
        exists = log_file.exists()
        logging.basicConfig(level=level, filename=options.log_file,
                            filemode=filemode, format=format_str)
    else:
        exists = False
        logging.basicConfig(level=level, format=format_str)
    if exists:
        logging.warning('overwriting existing log file')
    logging.info('application started')
    logging.info('logger initialized')
    status = do_stuff(options.n)
    logging.info('application ended')
    return status

if __name__ == '__main__':
    status = main()
    sys.exit(status)
