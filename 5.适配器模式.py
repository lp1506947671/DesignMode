#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


# 目标接口
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


# 带适配的类
class BankPay:
    @staticmethod
    def cost(money):
        print("银联支付%d元" % money)


# 类适配器多继承
class NewBankPay(Payment, BankPay):
    def pay(self, money):
        self.cost(money)


# 对象适配器组合
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


if __name__ == '__main__':
    b = NewBankPay()
    b.pay(60)

    b = PaymentAdapter(BankPay)
    b.pay(60)
