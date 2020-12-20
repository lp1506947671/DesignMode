#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ````````````````````````单例模式```````````````````````````````````


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            # 调用父类的三种方式
            # cls._instance = super().__new__(cls)
            # cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance = object.__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, a):
        self.a = a


# ````````````````````````装饰器写单例模式```````````````````````````````````


def single_ton1(cls):
    instance = {}

    def wrapper(*args, **kwargs):
        if cls not in instance.keys():
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper


@single_ton1
class MyClass1:
    def __init__(self, a):
        self.a = a


# ````````````````````````工作中的应用```````````````````````````````````

# 服务器函数
class MyClass2:
    def __init__(self, a):
        self.a = a

    def my_print2(self, b):
        print("result:%s" % (self.a + b))


# 客户端函数


def single_ton2(cls):
    my_instance = {}

    def wrapper(*args, **kwargs):
        name = kwargs.get("db_name")
        if name not in my_instance.keys():
            my_instance[name] = cls(*args, **kwargs)
        return my_instance[name]

    return wrapper


@single_ton2
class MyClass3:
    def __init__(self, db_name):
        self.db_connect = MyClass2(db_name)

    def my_print3(self, sql):
        print("MyClass2", id(self.db_connect))
        self.db_connect.my_print2(sql)


def my_func(db_name, sql):
    a = MyClass3(db_name=db_name)
    print("MyClass3", id(a))
    a.my_print3(sql=sql)


if __name__ == '__main__':
    my_func(db_name="10", sql="1")
    my_func(db_name="11", sql="2")
