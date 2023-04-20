from datetime import datetime as _datetime
from log_management import _get_log_file, create


def _log(level, msg):
    time = _datetime.strftime(_datetime.now(), '%Y-%d-%m %H:%M:%S')
    with open(_get_log_file(), 'a') as file:
        print(f'{time} [{level}]: {msg}', file=file)

def error(msg):
    _log('error', msg)
    
def warning(msg):
    _log('warning', msg)

def info(msg):
    _log('info', msg)
