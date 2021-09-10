#!/usr/bin/env python

import argparse


def amin():
    arg_parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
    arg_parser.add_argument('--foo', help='foo option')
    arg_parser.add_argument('--bar', help='bar optoin')
    arg_parser.add_argument('--flag', action='store_true',
                            help='flag option')
    options = arg_parser.parse_args()
    print(options)

if __name__ == '__main__':
    amin()
