#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "点(%s,%s)" % (self.x, self.y)

    def draw(self):
        print(str(self))


class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "线段[%s,%s]" % (self.p1, self.p2)

    def draw(self):
        print(str(self))


class Picture(Graphic):
    def __init__(self, iterable):
        self.children = []
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print("-----复合图形-----")
        for g in self.children:
            g.draw()
        print("-----复合图形-----")
        print("\n")


if __name__ == '__main__':
    print("-----开始画点-----")
    p1 = Point(1, 2)
    p1.draw()
    p2 = Point(3, 4)
    p2.draw()
    p3 = Point(5, 6)
    p3.draw()
    p4 = Point(7, 8)
    p4.draw()
    print("-----结束画点-----")
    print("-----开始画线-----")
    l1 = Line(p1, p2)
    l1.draw()
    l2 = Line(p3, p4)
    l2.draw()
    print("-----结束画线-----")
    print("********pic1******")
    pic1 = Picture([p1, l2])
    pic1.draw()
    print("********pic2******")
    pic2 = Picture([p2, l2])
    pic2.draw()
    print("********pic3******")
    pic3 = Picture([pic1, pic2])
    pic3.draw()
