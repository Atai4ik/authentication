# coding: utf-8

import hashlib


class User():

    login = None
    password = None
    firts_name = None
    last_name =  None
    is_active = True

    def signin(self, login, password):
        if len(login) > 6:
            self.login = login
        if len(password) > 8:
            self.password = password
        elif password is None:
            self.password = hashlib.md5(self.login)[:8]
        self.is_active = True
        return (self.login, self.password, self.is_active)

    def reset_password(self, login):
        pass

    def is_active(self):
        pass

    def change_profile_detail(self, firts_name, last_name):
        pass

    def check_password(self, unverfied_password):
        pass

    def send_confirmation_password(self):
        pass

