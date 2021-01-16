#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        pass


class FastStrategy(Strategy):
    def execute(self, data):
        print("用较快的策略处理%s"%data)


class SlowStrategy(Strategy):
    def execute(self, data):
        print("用较慢的策略处理%s"% data)


class Context:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


if __name__ == '__main__':
    d1 = "[....]"
    s1 = FastStrategy()
    s2 = SlowStrategy()
    context = Context(s1, d1)
    context.do_strategy()
    context.set_strategy(s2)
    context.do_strategy()
