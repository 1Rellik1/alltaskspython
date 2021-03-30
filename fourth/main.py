from fourth.HTML import HTML
from fourth.Hash import Hash

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

table = Hash()
for k, v in m.items():
    table.__setitem__(k, v)
print(table.__getitem__('Манго'))
for k, v in m.items():
     print(k+"   "+str(table.__getitem__(k)))

html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
            with html.div():
                html.p('Xtndthnf строка.')
        with html.div():
            html.p('Третья строка.')
