#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


# 抽象观察者
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):
        pass


# 抽象发布者
class Notice:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def notify(self):
        for obs in self.observers:
            obs.update(self)


# 具体发布者
class StaffNotice(Notice):

    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()


# 具体观察者
class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


if __name__ == '__main__':
    n1 = StaffNotice("初始化公司信息")
    s1 = Staff()
    s2 = Staff()
    n1.attach(s1)
    n1.attach(s2)
    n1.company_info = "公司今年业绩非常好,给大家发奖金"
    print(s1.company_info)
    print(s2.company_info)
    n1.detach(s1)
    n1.company_info = "明天放假"
    print(s1.company_info)
    print(s2.company_info)
