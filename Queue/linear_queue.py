class node:
    def __init__(self, value):
        self.data = value
        self.next = None
class LQueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self):
        while True:
            nw = int(input("enter the node press 1 to stop: "))
            nn = node(nw)
            if nw == 1:
                break
            if self.rear:
                self.rear.next = nn
                self.rear = nn
            else:
                self.rear = self.front = nn
    def see (self):
        temp = self.front
        while temp:
            print(temp.data, end = "->")
            temp = temp.next

que = LQueue()
que.enqueue()
que.see()

