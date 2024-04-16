#!/usr/bin/env python

import argparse


def dump_options(options, pos_args=None, exclude=None):
    options_dict = vars(options)
    with open('rerunnable_cla.txt', 'w') as file:
        for key, value in options_dict.items():
            if ((exclude is None or key not in exclude) and
                (pos_args is None or key not in pos_args)):
                if isinstance(value, bool):
                    if value:
                        print(f'--{key}', file=file)
                else:
                    print(f'--{key}\n{value}', file=file)
        if pos_args is not None:
            for key in pos_args:
                print(options_dict[key], file=file)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        fromfile_prefix_chars='@',
        description='application that saves its command line options and can be rerun'
    )
    arg_parser.add_argument('--number', type=int, default=1,
                            help='number of messages to write')
    arg_parser.add_argument('--type', choices=('hello', 'bye'), default='hello',
                            help='message type')
    arg_parser.add_argument('--verbose', action='store_true',
                            help='verbose output')
    arg_parser.add_argument('name', help='person to message')
    options = arg_parser.parse_args()
    dump_options(options, pos_args=('name', ))
    if options.verbose:
        print(f'printing {options.number} messages')
    for _ in range(options.number):
        print(f'{options.type} {options.name}')
