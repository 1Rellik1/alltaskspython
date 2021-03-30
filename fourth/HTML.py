import contextlib


class HTML():
    s = ""

    @contextlib.contextmanager
    def body(self):
        print("<body>")
        yield
        print("</body>")

    @contextlib.contextmanager
    def div(self):
        print("<div>")
        yield
        print("</div>")

    def p(self, text):
        print("<p>" + text + "</p>")
