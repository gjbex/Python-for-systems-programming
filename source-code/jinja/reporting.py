#!/usr/bin/env python

from argparse import ArgumentParser
from jinja2 import Environment, PackageLoader
import population
import random
import string
import sys


def generate_person():
    person = {
        'id':  ''.join(random.choices(string.ascii_letters, k=5)),
        'birthyear': random.randint(1950, 2015),
        'nr_friends': random.randint(0, 50),
    }
    return person

def main():
    arg_parser = ArgumentParser(description='generate random people')
    arg_parser.add_argument('n', type=int, default=5, nargs='?',
                            help='number of people to generate')
    arg_parser.add_argument('--format', choices=['html', 'md'],
                            default='md', help='output format, html or md')
    arg_parser.add_argument('--seed', type=int, default=1234,
                            help='seed for random number generator')
    options = arg_parser.parse_args()
    random.seed(options.seed)
    people = [generate_person() for _ in range(options.n)]
    environment = Environment(loader=PackageLoader('population', 'templates'),
                              trim_blocks=True, lstrip_blocks=True)
    template = environment.get_template('report.' + options.format)
    print(template.render(people=people))

if __name__ == '__main__':
    status = main()
    sys.exit(status)
