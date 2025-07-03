class Node:  # Better name than CircularList
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None


class CircularDoublyLinkedList:  # Rename to match test
  def __init__(self):
    self.start = None

  def insert_at_end(self, value):  # Rename
    new_node = Node(value)
    if self.start is None:
      new_node.next = new_node
      new_node.prev = new_node
      self.start = new_node
    else:
      last = self.start.prev
      last.next = new_node
      new_node.prev = last
      new_node.next = self.start
      self.start.prev = new_node

  def insert_at_beginning(self, value):  # Rename
    self.insert_at_end(value)
    self.start = self.start.prev

  def remove_by_value(self, value):  # Rename
    if self.start is None:
      print("The list is empty")
      return
    current = self.start
    while True:
      if current.data == value:
        if current.next == current:
          self.start = None
        else:
          current.prev.next = current.next
          current.next.prev = current.prev
          if current == self.start:
            self.start = current.next
        print(f"Removed: {value}")
        return
      current = current.next
      if current == self.start:
        print(f"Value '{value}' not found")
        break

  def show_list_forward(self):  # Rename
    if self.start is None:
      print("The list is empty")
      return
    current = self.start
    values = []
    while True:
      values.append(str(current.data))
      current = current.next
      if current == self.start:
        break
    print(" -> ".join(values))

  def show_list_backward(self):  # Rename
    if self.start is None:
      print("The list is empty")
      return
    last = self.start.prev
    current = last
    values = []
    while True:
      values.append(str(current.data))
      current = current.prev
      if current == last:
        break
    print(" <- ".join(values))
