#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


# 抽象观察者
class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, notice):
        ...


# 抽象发布者
class Notice(metaclass=ABCMeta):

    def __init__(self):
        self.staff_list = []

    def attach(self, staff):
        self.staff_list.append(staff)

    def detach(self, staff):
        self.staff_list.remove(staff)
        staff.company_info = None

    def notify(self):
        for item in self.staff_list:
            item.update(self)  # 注意点1:item和self


# 抽象发布者
class Company(Notice):
    """
      1.继承Notice通知类,实现对那些需要通知的员工进行增删改查
      2.定义自己需要发布的信息
      3.每设置一次信息就需要通知一次所有的在公司的员工
      """

    def __init__(self, company_info=None):
        super(Company, self).__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter  # 注意点2
    def company_info(self, data):
        self.__company_info = data
        self.notify()


# 具体观察者
class ChineseStaff(Observer):

    def __init__(self):
        self.company_info = None

    def update(self, notice: Company):
        self.company_info = notice.company_info


class ForeignStaff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice: Company):
        self.company_info = f"翻译为英文:{notice.company_info}"


if __name__ == '__main__':
    staff1 = ChineseStaff()
    staff2 = ChineseStaff()
    staff3 = ForeignStaff()

    company = Company()
    company.attach(staff1)
    company.attach(staff2)
    company.attach(staff3)
    print("begin")
    print(staff1.company_info)
    print(staff2.company_info)
    print(staff3.company_info)
    print("end")
    company.company_info = "公司明天放假"
    print(staff1.company_info)
    print(staff2.company_info)
    print(staff3.company_info)
    company.detach(staff1)
    company.company_info = "公司明天发工资"
    print(staff1.company_info)
    print(staff2.company_info)
    print(staff3.company_info)
