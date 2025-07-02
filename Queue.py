
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None


    def isEmpty(self):
        return self.front is None

    def enqueue(self, data):
        newnode = node(data)
        if self.rear is None:
            self.front = self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return

        result = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
            return result

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.front.data
