import unittest
from src.lab4.task2 import *


class IndexTestCase(unittest.TestCase):
    def test_general(self):
        group1 = Group(0, 18)
        group2 = Group(19, 25)

        user1 = User("Исигами Сэнку", 18)
        user2 = User("Касэки", 60)

        self.assertTrue(group1.is_user_can_join(user1))
        self.assertFalse(group2.is_user_can_join(user1))

        self.assertFalse(group1.is_user_can_join(user2))
        self.assertFalse(group2.is_user_can_join(user2))
