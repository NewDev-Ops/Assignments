class Node:
  def __init__(self, data):
    self.data = data  # This aspect will be the data
    self.next = None  # This aspect will be the pointer


# Testing

# Insertion
NodeNew = Node(23)
NodeNew2 = Node(46)

# Next will reference that location (Look for the location)
NodeNew.next = NodeNew2
Shorter = NodeNew.next.data

# This will print what is in NodeNew.next.data
print(Shorter)

# Printing the entire list part
print('\n')
print("Printing the entire list")
testinglist = NodeNew

while testinglist is not None:
  print(testinglist.data)
  testinglist = testinglist.next
