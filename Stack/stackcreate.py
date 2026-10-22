class node:
    def __init__(self,value):
        self.data = value
        self.next = None
class stack:
    def __init__(self):
        self.top = None
    def isempty(self):
        return self.top is None
    def push(self):
        while True:
            nw = int(input("enter the value of node | press 1 to stop: "))
            if nw == 1:
                break
            nn = node(nw)
            nn.next = self.top
            self.top = nn
    def pop(self):
        if self.isempty():
            print("stack is empty ")
        else:
            temp = self.top
            print("poped element" , temp.data) #top most element
            self.top = self.top.next #down element
            temp = None
            
    def see(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("stack contains: ")
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next
st = stack()
st.push()
st.see()
st.pop()
st.see()