class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self):
        while True:
            nw = int(input("enter node (1 to stop): "))

            if nw == 1:
                break

            nn = Node(nw)
            nn.next = self.top
            self.top = nn

    def push2(self, nn):
        nn.next = self.top
        self.top = nn

    def pop(self):
        if self.isempty():
            print("empty")
        else:
            temp = self.top
            print("element deleted", temp.data)
            self.top = self.top.next
            temp.next = None

    def see(self):
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next

    def reverse(self, stack2):
        temp = self.top
        while temp:
            stack2.push2(Node(temp.data))
            temp = temp.next


stack = Stack()
stack2 = Stack()

stack.push()

print("Original stack:")
stack.see()

stack.reverse(stack2)

print("Reversed stack:")
stack2.see()