from fourth.HTML import HTML

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