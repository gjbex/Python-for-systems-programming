#!/usr/bin/env python

import fire


class Hello:
    '''Hello group of commands, there is a to and a everyone
    command
    '''

    def __init__(self, name):
        self.name = name

    def to(self, name=None):
        if name is None:
            if self.name is None:
                return 'No one to say hello to'
            else:
                return f'Hello to {self.name}'
        else:
            return f'Hello {name}'

    def everyone(self):
        return 'hello to everyone'


class Bye:
    '''Bye group of commands, there is a to and a no_one
    command
    '''

    def __init__(self, name):
        self.name = name

    def to(self, name=None):
        if name is None:
            if self.name is None:
                return 'No one to say bye to'
            else:
                return f'Bye to {self.name}'
        else:
            return f'Bye {name}'

    def no_one(self):
        return f'Bye to no one'


class Sayer:
    '''Class to make the hello and bye groups available, it
    also has its own to command, as well as the info command
    '''

    def __init__(self, hello_name=None, bye_name=None):
        self.hello = Hello(hello_name)
        self.bye =  Bye(bye_name)

    def to(self):
        return 'Do you want to say hello or bye?'

    def info(self):
        return 'This is version 0.1beta'


if __name__ == '__main__':
    fire.Fire(Sayer)
