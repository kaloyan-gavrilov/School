class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        self.__data = new_data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, new_next):
        self.__next = new_next


class LinkedList:
    def __init__(self):
        self.__head = None

    def __iter__(self):
        current_node = self.__head
        while current_node:
            yield current_node.data
            current_node = current_node.next

    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Index must be >= 0")
        current_node = self.__head
        counter = 0
        while current_node:
            if counter == index:
                return current_node.data
            counter += 1
            current_node = current_node.next
        raise IndexError("Index out of range")

    def __setitem__(self, index, data):
        if index < 0:
            raise IndexError("Index must be >= 0")
        current_node = self.__head
        counter = 0
        while current_node:
            if counter == index:
                current_node.data = data
                return
            counter += 1
            current_node = current_node.next
        raise IndexError("Index out of range")

    def append(self, data):
        new_node = Node(data)
        if not self.__head:
            self.__head = new_node
            return
        last_node = self.__head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, index, data):
        if index < 0:
            print("Index must be >= 0")
            return
        new_node = Node(data)
        if index == 0:
            new_node.next = self.__head
            self.__head = new_node
            return
        current_node = self.__head
        for _ in range(index - 1):
            if current_node is None:
                print("Index out of range.")
                return
            current_node = current_node.next
        if current_node is None:
            print("Index out of range.")
            return
        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, data):
        current_node = self.__head
        if current_node is None:
            print("List is empty.")
            return
        if current_node.data == data:
            self.__head = current_node.next
            return
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
        print("Element not in list")

    def pop(self, index=None):
        if index is None:
            if self.__head is None:
                print("List is empty.")
                return
            data = self.__head.data
            self.__head = self.__head.next
            return data
        if index < 0:
            print("Index must be a >= 0")
            return
        if index == 0:
            if self.__head is None:
                print("List is empty.")
                return
            data = self.__head.data
            self.__head = self.__head.next
            return data
        current_node = self.__head
        for _ in range(index - 1):
            if current_node is None or current_node.next is None:
                print("Index out of range.")
                return
            current_node = current_node.next
        if current_node.next is None:
            print("Index out of range.")
            return
        data = current_node.next.data
        current_node.next = current_node.next.next
        return data

    def clear(self):
        self.__head = None

    def index(self, data):
        current_node = self.__head
        index = 0
        while current_node:
            if current_node.data == data:
                return index
            current_node = current_node.next
            index += 1
        print("Element not in list")
        return -1

    def sort(self):
        if self.__head is None:
            print("List is empty.")
            return
        values = []
        current_node = self.__head
        while current_node:
            values.append(current_node.data)
            current_node = current_node.next
        values.sort()
        self.clear()
        for value in values:
            self.append(value)

    def reverse(self):
        prev_node = None
        current_node = self.__head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.__head = prev_node

    def display(self):
        current_node = self.__head
        while current_node:
            if current_node.next is None:
                print(current_node.data)
            else:
                print(current_node.data, end=" -> ")
            current_node = current_node.next
        if self.__head is None:
            print("List is empty.")


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(25)
linked_list.append(3)
linked_list.append(17)
linked_list.append(24)

print("\nOriginal list:")
linked_list.display()

print("\n-------------\n")

linked_list.insert(1, 4)
print("After inserting 4 at index 1:")
linked_list.display()

print("\n-------------\n")

linked_list.remove(4)
print("After removing 4:")
linked_list.display()

print("\n-------------\n")

linked_list.pop(2)
print("After popping element 2:")
linked_list.display()

print("\n-------------\n")

linked_list.sort()
print("After sorting:")
linked_list.display()

print("\n-------------\n")

linked_list.reverse()
print("After reversing:")
linked_list.display()

print("\n\nTest na iteriraneto\n\n")

print("Original list:")
for item in linked_list:
    print(item, end=" -> ")
print("None")

linked_list[1] = 10
print("After setting index 1 to 10:")
for item in linked_list:
    print(item, end=" -> ")
print("None")

print("Element at index 0:", linked_list[0])

# Create your own implementation of the "List" data structure you already used in Python.
# Let your list support the following methods:
# myList.append(x) - Adds the X element to the list.
# myList.insert(i, x) - Adds the element X to the list at index I.
# myList.remove(x) - Removes the first occurrence of element X.
# myList.pop([i]) - Removes the I-th element
# myList.clear() - Clears the entire list.
# myList.index(x) - Returns the index of the first occurrence of element X
# myList.sort() - Sorts the list.
# myList.reverse() - Rearranges the list backwards.
# Make your list iterable.
# Implement an operator to index your list (myList[5] = 10)
# Make sure there is good error handling for each function of the class.
