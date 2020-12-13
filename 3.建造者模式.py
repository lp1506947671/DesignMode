#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta


class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s,%s,%s,%s" % (self.face, self.body, self.arm, self.leg)


class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass


class SexyGirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_body(self):
        self.player.body = "好的身体"

    def build_face(self):
        self.player.face = "好的脸蛋"

    def build_arm(self):
        self.player.arm = "好的手臂"

    def build_leg(self):
        self.player.leg = "好的腿"


class MonsterBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_body(self):
        self.player.body = "不好的身体"

    def build_face(self):
        self.player.face = "不好的脸蛋"

    def build_arm(self):
        self.player.arm = "不好的手臂"

    def build_leg(self):
        self.player.arm = "不好的腿"


class PlayerDirector:
    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player


# client
builder = SexyGirlBuilder()
director = PlayerDirector()
p = director.build_player(builder)
print(p)
