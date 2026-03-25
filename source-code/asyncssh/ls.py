#!/usr/bin/env ptyhon3

import argparse
import asyncio
import asyncssh


async def main():
    parser = argparse.ArgumentParser(description="List files on a remote server using SSH")
    parser.add_argument("--host", help="The hostname or IP address of the remote server")
    parser.add_argument("-u", "--user", help="The username to use for SSH authentication")
    args = parser.parse_args()

    async with asyncssh.connect(args.host, username=args.user) as conn:
        result = await conn.run("ls -l", check=True)
        print(result.stdout)


if __name__ == '__main__':
    asyncio.run(main())
