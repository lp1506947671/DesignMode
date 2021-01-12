#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import abstractmethod, ABCMeta


# ---------------抽象产品角色---------------
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


# ---------------具体产品角色---------------
class AliPay(Payment):
    def __init__(self, use_hua_bei=False):
        self.use_hua_bei = use_hua_bei

    def pay(self, money):
        if self.use_hua_bei:
            print("花呗支付%d元" % money)
        else:
            print("支付宝余额支付%d元" % money)


class WeChatPay(Payment):
    def pay(self, money):
        print("微信支付%d元" % money)


# ---------------抽象工厂---------------
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


# ---------------具体工厂---------------
class AliPayFactory(PaymentFactory):
    def create_payment(self):
        return AliPay()


class WeChatPayFactory(PaymentFactory):
    def create_payment(self):
        return WeChatPay()


if __name__ == '__main__':
    # ---client----
    pf = WeChatPayFactory()
    p = pf.create_payment()
    p.pay(200)
