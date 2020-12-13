#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print("花呗支付%d元" % money)
        else:
            print("支付宝余额支付%d元" % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元" % money)


class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()


class WechatPayFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()


# ---client----
pf = WechatPayFactory()
p = pf.create_payment()
p.pay(200)
