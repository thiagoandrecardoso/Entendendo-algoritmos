class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print(None)


my_list = DoublyLinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)

print("Lista original:")
my_list.display()

my_list.prepend(0)

print("\nLista após a inserção no início:")
my_list.display()

my_list.append(4)

print("\nLista após a inserção no final:")
my_list.display()
