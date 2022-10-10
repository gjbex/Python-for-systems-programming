#!/usr/bin/env python

import fire


class Hello:

    def __init__(self, name):
        self.name = name

    def say(self):
        return f'Hello {self.name}'

class Bye:

    def __init__(self, name):
        self.name = name

    def say(self):
        return f'Bye {self.name}'


class Sayer:

    def __init__(self, hello_name, bye_name):
        self.hello = Hello(hello_name)
        self.bye =  Bye(bye_name)

    def say(self):
        return f'Bla, bla'

if __name__ == '__main__':
    fire.Fire(Sayer)
