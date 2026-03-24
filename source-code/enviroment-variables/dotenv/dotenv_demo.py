#!/usr/bin/env python3

from dotenv import load_dotenv
import os


def main():
    # Check whether the environment variable is already set
    if 'MY_SECRET' in os.environ:
        print('MY_SECRET is already set in the environment.')
    else:
        # Load environment variables from .env file
        print('Loading environment variables from .env file...')
        load_dotenv()

    # Access an environment variable
    secret_key = os.getenv('MY_SECRET')

    if secret_key:
        print(f'MY_SECRET: {secret_key}')
    else:
        print('MY_SECRET not found in environment variables.')


if __name__ == '__main__':
    main()
