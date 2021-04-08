from unittest import TestCase

from fourth.Hash import Hash


class Hashtest(TestCase):
    def setUp(self):
        self.Hash = Hash()

    def test_getitem(self):
        m = {'Водоросли': 280,
             'Картофель': 260,
             'Лук-порей': 59,
             'Манго': 291,
             'Орехи грецкие': 266,
             'Салями': 225,
             'Специи': 283,
             'Сыр сливочный': 152,
             'Творог': 215,
             'Тофу': 142,
             'Хек': 248,
             'Чай черный': 118,
             'Чернила каракатицы': 95,
             'Шампиньоны': 101,
             'Финик': 104}
        for k, v in m.items():
            self.Hash.__setitem__(k, v)
        self.assertEqual(291,self.Hash.__getitem__('Манго'))
