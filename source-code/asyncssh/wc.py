#!/usr/bin/env python3

'''Run ``wc -`` on a remote host and stream a local file to its stdin.'''

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

import asyncssh


def parse_args() -> argparse.Namespace:
    '''Parse command-line options.'''
    parser = argparse.ArgumentParser(
        description='Do wc on a remote server.',
    )
    parser.add_argument(
        '--host',
        required=True,
        help='Host name to connect to.',
    )
    parser.add_argument(
        '--user',
        required=True,
        help='User name to connect as.',
    )
    parser.add_argument(
        'file_name',
        type=Path,
        help='File to do word count on.',
    )
    return parser.parse_args()


async def run_remote_wc(
    host: str,
    user: str,
    file_name: Path,
) -> int:
    '''Run ``wc -`` remotely and send the file content to its stdin.'''
    async with asyncssh.connect(host, username=user) as connection:
        process = await connection.create_process('wc -')

        with file_name.open(encoding='utf-8') as input_file:
            for line in input_file:
                process.stdin.write(line)

        process.stdin.write_eof()

        stdout, stderr = await process.communicate()

    for line in stdout.splitlines():
        print(line)

    for line in stderr.splitlines():
        print(line, file=sys.stderr)

    return process.returncode


async def main() -> int:
    '''Parse arguments and execute the remote word count.'''
    args = parse_args()
    return await run_remote_wc(args.host, args.user, args.file_name)


if __name__ == '__main__':
    raise SystemExit(asyncio.run(main()))
