from Function import *
from time import sleep


def login_daido1(self):
    sleep(3)
    Login.login_action(self, "daido1")
    Logout.logout(self)


def login_daido2(self):
    sleep(3)
    Login.login_action(self, "daido2")
    Logout.logout(self)


def login_daido3(self):
    sleep(3)
    Login.login_action(self, "daido3")
    Logout.logout(self)


def login_admin(self):
    sleep(3)
    Login.login_action(self, "admin")