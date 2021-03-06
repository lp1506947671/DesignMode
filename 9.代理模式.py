#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


# 抽象实体
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


# 实体
class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, "r")
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, "w")
        f.write(content)
        f.close()


# 虚拟代理
class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        pass


# 保护代理
class ProtectedProxy(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        raise PermissionError("无写入权限")


if __name__ == '__main__':
    subj1 = RealSubject("new")
    print(subj1.get_content())

    subj2 = VirtualProxy("new")
    print(subj2.get_content())

    subj3 = ProtectedProxy("new")
    print(subj3.set_content("a"))