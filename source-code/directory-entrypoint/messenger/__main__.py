import argparse
import messenger
import sys


arg_parser = argparse.ArgumentParser(description='say something to the user')
arg_parser.add_argument('--hello', action='store_true', help='say hello')
arg_parser.add_argument('--bye', action='store_true', help='say bye')
arg_parser.add_argument('name', help='name to talk to')
options = arg_parser.parse_args()

if options.hello:
    messenger.say_hello(options.name)
if options.bye:
    messenger.say_bye(options.name)
if not (options.hello or options.bye):
    print(f"don't know what  to say to {options.name}", file=sys.stderr)
    sys.exit(1)
