# coding: utf-8
import unittest


from user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def test_signin(self):
        self.user.signin('atai.zh', '123456789')
        self.assertEqual(self.user.login, 'atai.zh')
        self.assertEqual(self.user.password, '123456789')

    def test_reset_password(self):
        self.user.password('987654321')
        self.assertEqual(self.user.password, '987654321')


if __name__ == '__main__':
    unittest.main()

