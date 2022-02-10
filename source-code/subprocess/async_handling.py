#!/usr/bin/env python

from datetime import datetime
import subprocess
import sys
import time

class Result:

    def set(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


def execute(cmd, result):
    process = subprocess.Popen(cmd,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)
    for stderr_line in iter(process.stderr.readline, ''):
        yield stderr_line.strip()
    stdout, stderr = process.communicate()
    return_code = process.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)
    else:
        result.set(stdout)

result = Result()
for stderr_line in execute(['bash', 'process.sh'], result):
    print(f'{datetime.now()}: {stderr_line}')
print(f'result:\n{result.value}')
