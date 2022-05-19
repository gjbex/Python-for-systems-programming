#!/usr/bin/env python

from argparse import ArgumentParser
import os
from pathlib import Path
import platform
import psutil
import pwd
import shlex
import sys
import time


class Metric:

    def __init__(self, name, action, is_active=True):
        self._name = name
        self._action = action
        self._is_active = is_active

    @property
    def name(self):
        return self.name

    def measure(self, process):
        return str(self._action(process))

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value):
        self._is_active = value

def get_username():
    '''Find the user name of the current process'''
    return pwd.getpwuid( os.getuid() ).pw_name


def find_ancestor(pid=None, username=None):
    '''Find the ancestor of the process with ID pid thatis owned by the user with
    the given user name'''
    if pid is not None and not psutil.pid_exists(pid):
        raise ValueError(f'PID {pid} does not exist')
    if username is None:
        username = get_username()
    process = psutil.Process(pid)
    parents = process.parents()
    for parent in reversed(parents):
        if parent.username() == username:
            return parent
    return process


def get_cmdline(process):
    return f'"{" ".join(shlex.quote(s) for s in process.cmdline())}"'


def get_affinity(process):
    affinities = process.cpu_affinity()
    return ';'.join(str(affinity) for affinity in affinities)


def get_read_open_files(process):
    open_files = list()
    try:
        for file in process.open_files():
            try:
                if 'r' == file.mode:
                    open_files.append(file.path)
            except:
                pass
    except:
        pass
    return ';'.join(open_files)


def get_write_open_files(process):
    open_files = list()
    try:
        for file in process.open_files():
            try:
                if 'r' != file.mode:
                    open_files.append(f'{file.path}:{Path(file.path).stat().st_size}')
            except:
                pass
    except:
        pass
    return ';'.join(open_files)


def define_actions(inactive=None):
    metrics = dict()
    metrics['time'] = Metric('time', lambda x: time.time())
    metrics['node'] = Metric('node', lambda x: platform.node())
    metrics['pid'] = Metric('pid', lambda x: x.pid)
    metrics['ppid'] = Metric('ppid', lambda x: x.ppid())
    metrics['cmd'] = Metric('cmd', lambda x: x.exe())
    metrics['cmdline'] = Metric('cmdline', lambda x: get_cmdline(x))
    metrics['cpu_percent'] = Metric('cpu_percent',
                                    lambda x: f'{x.cpu_percent(interval=None):.2f}')
    metrics['cpu_user'] = Metric('cpu_user', lambda x: x.cpu_times().user)
    metrics['cpu_sys'] = Metric('cpu_sys', lambda x: x.cpu_times().system)
    metrics['num_threads'] = Metric('num_threads', lambda x: x.num_threads())
    metrics['mem_perpent'] = Metric('mem_perpent', lambda x: f'{x.cpu_percent():.2f}')
    metrics['mem'] = Metric('mem', lambda x: x.memory_full_info().uss)
    metrics['affinity'] = Metric('affinity', lambda x: get_affinity(x))
    metrics['read_files'] = Metric('read_files', lambda x: get_read_open_files(x))
    metrics['write_files'] = Metric('write_files', lambda x: get_write_open_files(x))
    if inactive:
        for metric_name in inactive:
            metrics[metric_name].is_active = False
    return metrics


def status_header(metrics):
    return ','.join(metric_name for metric_name, metric in metrics.items()
                    if metric.is_active)


def process_status(process, metrics):
    '''Show properties of the specified process'''
    status = list()
    with process.oneshot():
        for metric in metrics.values():
            if metric.is_active:
                status.append(metric.measure(process))
    return ','.join(status)


def main():
    arg_parser = ArgumentParser(description='monitor processes')
    arg_parser.add_argument('--pid', type=int, help='parent process ID ot monitor')
    arg_parser.add_argument('--user', help='user of the processes to monitor')
    arg_parser.add_argument('--delta', type=float, default=60.0,
                            help='number of seconds between measurements')
    arg_parser.add_argument('--affinity', action='store_true',
                            help='monitor process affinity')
    arg_parser.add_argument('--files', action='store_true', help='monitor poen files')
    arg_parser.add_argument('--ancestor', action='store_true',
                            help='search for ancestor owned by use and report on all its decendants')
    arg_parser.add_argument('--output-file', help='name of file to store informatoin')
    options = arg_parser.parse_args()
    if options.ancestor:
        process = find_ancestor(options.pid, options.user)
    else:
        process = psutil.Process(options.pid)
    inactive = []
    if not options.affinity:
        inactive.append('affinity')
    if not options.files:
        inactive.append('read_files')
        inactive.append('write_files')
    metrics = define_actions(inactive)
    if options.output_file:
        file = open(options.output_file, 'w')
    else:
        file = sys.stdout
    try:
        with file:
            print(status_header(metrics), file=file)
            while True:
                process_info = [process_status(process, metrics)]
                for child_process in process.children(recursive=True):
                    process_info.append(process_status(child_process, metrics))
                print('\n'.join(process_info), file=file)
                time.sleep(options.delta)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    status = main()
    sys.exit(status)
