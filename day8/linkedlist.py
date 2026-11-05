class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

node1 = Node(10,None)
node2 = Node(20, None)
node1.next_node = node2

node3 = Node(30, None)
node2.next_node = node3

current = node1

while current != None:
    print(current.value)
    current = current.next_node

