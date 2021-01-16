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
    """集成对抽象观察者的更新"""

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
    """
    1.继承Notice通知类,实现对那些需要通知的员工进行增删改查
    2.定义自己需要发布的信息
    3.每设置一次信息就需要通知一次所有的在公司的员工
    """

    def __init__(self, company_info=None):
        super().__init__()
        # 定义要发布的信息
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        """每设置一次公司消息就要通知员工"""
        self.__company_info = info
        # 通知每一个公司员工
        self.notify()


# 具体观察者
class Staff(Observer):
    def __init__(self):
        # 定义要接收的信息
        self.company_info = None

    def update(self, notice):
        # 更新公司消息
        self.company_info = notice.company_info


if __name__ == '__main__':
    n1 = StaffNotice("")
    s1 = Staff()
    s2 = Staff()
    n1.attach(s1)
    n1.attach(s2)
    print("begin")
    print(s1.company_info)
    print(s2.company_info)
    print("end")
    print("公司通知大家")
    n1.company_info = "公司今年业绩非常好,给大家发奖金"
    print(s1.company_info)
    print(s2.company_info)
    print("删除员工s1")
    n1.detach(s1)
    n1.company_info = "明天放假"
    print(s1.company_info)
    print(s2.company_info)
