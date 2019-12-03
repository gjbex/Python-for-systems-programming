#!/usr/bin/env python

from argparse import ArgumentParser
from configparser import ConfigParser
from pathlib import Path
import random
import sys


def generate_data(n, a=0, b=1):
    return [random.randint(a, b) for _ in range(n)]

def main():
    arg_parser = ArgumentParser(add_help=False)
    arg_parser.add_argument('--conf',
                            help='configuration file to use')
    arg_parser.add_argument('--verbose', action='store_true',
                            help='verbose output')
    options, remaining_options = arg_parser.parse_known_args()
    system_conf = Path.cwd() / 'etc' / 'my_app.conf'
    cfg = ConfigParser()
    cfg['defaults'] = {'n': '1', 'a': '0', 'b': '6'}
    if options.verbose:
        print('application default values:', file=sys.stderr)
        cfg.write(sys.stderr)
    if system_conf.exists():
        cfg.read('etc/my_app.conf')
        if options.verbose:
            print('system configuration file values:', file=sys.stderr)
            cfg.write(sys.stderr)
    else:
        print(f'missing configuration file {system_conf}', file=sys.stderr)
    if options.conf:
        cfg.read(options.conf)
        if options.verbose:
            print('user configuration file values:', file=sys.stderr)
            cfg.write(sys.stderr)
    cfg_opts = dict(cfg['defaults'])
    arg_parser_cl = ArgumentParser(description='test application',
                                   parents=[arg_parser])
    arg_parser_cl.set_defaults(**cfg_opts)
    arg_parser_cl.add_argument('n', type=int, nargs='?',
                               help='number of random values to generate')
    arg_parser_cl.add_argument('--a', type=int, help='smallest value')
    arg_parser_cl.add_argument('--b', type=int, help='largest value')
    arg_parser_cl.parse_args(remaining_options, options)
    if options.verbose:
        print('final options:', file=sys.stderr)
        print(f'n = {options.n}\na = {options.a}\nb = {options.b}', end='\n\n',
              file=sys.stderr)
    values = generate_data(options.n, a=options.a, b=options.b)
    print('\n'.join(str(value) for value in values))
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
