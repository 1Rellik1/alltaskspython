class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print("ok")

    def back(self):
        print(self.items[len(self.items) - 1])

    def pop(self):
        print(self.items.pop())

    def size(self):
        print(len(self.items))

    def clear(self):
        self.items.clear()
        print("ok")


s = Stack()
while True:
    command = input()
    if command == "exit":
        print("bye")
        break
    if command[:4] == "push":
        number = command[5:]
        s.push(number)
    elif command == "clear":
        s.clear()
    elif command == "pop":
        s.pop()
    elif command == "back":
        s.back()
    elif command == "size":
        s.size()
