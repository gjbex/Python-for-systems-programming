#!/usr/bin/env python
import fire


class Job:

    _nodes: int
    _ntasks: int

    def __init__(self, nodes=1, ntasks=1):
        self.nodes = nodes
        self.ntasks = ntasks

    @property
    def nodes(self):
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        self._nodes = nodes
        return self


    @property
    def ntasks(self):
        return self._ntasks

    @ntasks.setter
    def ntasks(self, ntasks):
        self._ntasks = ntasks
        return self

    def print(self):
        return f'nodes={self.nodes} ntasks={self.ntasks}'

if __name__ == '__main__':
    fire.Fire(Job)
