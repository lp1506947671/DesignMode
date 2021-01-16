#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


# 抽象者
class Shape(metaclass=ABCMeta):
    # 聚合关联关系:与颜色进行关联
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


# 细化抽象
class Rectangle(Shape):
    name = "长方形"

    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    name = "圆形"

    def draw(self):
        self.color.paint(self)


# 实现者
class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass


# 具体实现者
class Red(Color):
    def paint(self, shape):
        print("红色的%s" % shape.name)


class Black(Color):
    def paint(self, shape):
        print("黑色的%s" % shape.name)


if __name__ == '__main__':
    rect = Rectangle(Red())
    rect.draw()
