class C32:
    def __init__(self):
        self.state = 'A'

    def mass(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'E'
            return 2
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'D'
            return 7
        elif self.state == 'E':
            self.state = 'F'
            return 8
        else:
            raise RuntimeError

    def play(self):
        if self.state == 'C':
            return (5)
        else:
            raise RuntimeError

    def boost(self):
        if self.state == 'B':
            self.state = 'C'
            return (1)
        elif self.state == 'C':
            self.state = 'E'
            return (4)
        elif self.state == 'D':
            self.state = 'E'
            return (6)
        else:
            raise RuntimeError
