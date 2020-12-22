#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class BankPay:
    @staticmethod
    def cost(money):
        print("银联支付%d元" % money)


# 适配器类
class NewBankPay(Payment, BankPay):
    def pay(self, money):
        self.cost(money)


# 组合
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


if __name__ == '__main__':
    # b = NewBankPay()
    # b.pay(60)

    b = PaymentAdapter(BankPay)
    b.pay(60)