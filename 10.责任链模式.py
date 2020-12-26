#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


# 抽象处理者
class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass


# 具体处理者
class GeneralManager(Handler):

    def handle_leave(self, day):
        if day <= 10:
            print("总经理批准%d天" % day)
        else:
            print("你还是辞职吧")


class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day < 7:
            print("部门经理批准%s天" % day)
        else:
            print("部门经理职权不够")
            self.next.handle_leave(day)


class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print("项目主管批准%d" % day)
        else:
            print("项目主管职权不够")
            self.next.handle_leave(day)


if __name__ == '__main__':
    a = ProjectDirector()
    a.handle_leave(10)
