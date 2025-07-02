class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.top = None

  def push(self, data):
    new_node = Node(data)
    new_node.next = self.top
    self.top = new_node

  def pop(self):
    if self.top is None:
      return None
    popped = self.top.data
    self.top = self.top.next
    return popped

  def peek(self):
    if self.top is None:
      return None
    return self.top.data


class Queue:
  def __init__(self):
    self.front = None
    self.rear = None

  def enqueue(self, data):
    new_node = Node(data)
    if self.rear is None:
      self.front = self.rear = new_node
    else:
      self.rear.next = new_node
      self.rear = new_node

  def dequeue(self):
    if self.front is None:
      return None
    result = self.front.data
    self.front = self.front.next
    if self.front is None:
      self.rear = None
    return result


def is_palindrome_using_stack(s: str) -> bool:
  teststack = Stack()
  testqueue = Queue()

  for i in s:
    teststack.push(i)
    testqueue.enqueue(i)

  for _ in range(len(s)):
    if teststack.pop() != testqueue.dequeue():
      return False
  return True


print(is_palindrome_using_stack("racecar"))
print(is_palindrome_using_stack("hello"))
