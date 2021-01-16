#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Cpu:

    @staticmethod
    def run():
        print("CPU开始运行")

    @staticmethod
    def stop():
        print("CPU停止运行")


class Disk:
    @staticmethod
    def run():
        print("硬盘开始运行")

    @staticmethod
    def stop():
        print("硬盘停止运行")


class Memory:

    @staticmethod
    def run():
        print("硬盘开始运行")

    @staticmethod
    def stop():
        print("硬盘停止运行")


# Facade
class Computer:
    def __int__(self):
        self.cpu = Cpu()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


if __name__ == '__main__':
    computer = Computer()
    computer.run()
    computer.stop()
