class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


# will initialize an empty csll
# THE DIFFERENCE BETWEEN SINGLE LINKED LIST AND CIRCULAR SINGLE LINKED LIST IS THAT
#     - IN SLL THE NEXT OF LAST ELEMENT POINTS TO NONE
#     - IN CSLL THE NEXT OF LAST ELEMENT POINTS TO HEAD
#     - IN BOTH CSLL AND SLL THE TAIL POINTS TO THE LAST ELEMENT, THERE IS NO DIFFERENCE HERE

class CircularSinglyLinkedList:
    def __init__(self):  # (self, value):
        # new_node = Node(value=value)
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        # a way to print that will override the print() statement
        current = self.head
        result = ''

        while current:  # this is an infinite loop and we rely on the break statement to interrupt the loop
            result += str(current.value)
            current = current.next
            if current == self.head:
                break
            result += ' --> '
        return result

    def append(self, value):
        new_node = Node(value=value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.length += 1

    def prepend(self, value):  # attaching a new node at the beginning of the list

        new_node = Node(value=value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node

        self.length += 1

    def insert(self, value, index):  # insert element at a given index

        """
        Inserts an element at given index
        If index is -1, inserts the element last
        Returns True if insertion is successful
        or Exception if not successful - non-existent index
        """

        new_node = Node(value=value)

        if self.length == 0:
            raise Exception("Empty list, use .append or .prepend methods.")

        if index >= self.length or index < -1:
            raise Exception("Index out of range")

        if index == -1 or index == self.length - 1:  # means to append last
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
            return True

        if index == 0:  # means to append first
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
            return True

        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = current

        self.length += 1

        return True

    def traverse(self):  # goes through the nodes and prints their values on the screen
        current = self.head

        while current:
            print(current)
            current = current.next
            if current == self.head:
                break

    def search(self, value):  # search for a specific value in the linked list
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next
            if current == self.head:
                break

        return False

    def get(self, index):  # return value of element at given index

        if index < -1 or index >= self.length:
            return None

        if index == 0:
            return self.head

        if index == -1 or index == self.length - 1:
            return self.tail

        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set(self, index, value):
        # set the value of an element at given list to be a given value
        current = self.get(index=index)

        if current:
            current.value = value
            return True

        return False

    def pop_first(self):
        # removing the first element and returning it
        popped_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node

        elif self.length == 0:
            raise Exception("Empty linked list")

        else:
            self.head = self.head.next
            popped_node.next = None
            self.tail.next = self.head
            self.length -= 1
            return popped_node

    def pop(self):
        # removing the last element and returning it

        popped_node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node

        elif self.length == 0:
            raise Exception("Empty linked list")
        else:
            current = self.head
            while current:
                current = current.next
                if current.next == self.head:
                    break
            self.tail = current
            self.tail.next = self.head
            popped_node.next = None
            self.length -= 1
            return popped_node

    def remove(self, index):
        # remove a node with specific index

        if index == 0:
            popped_node = self.head
            self.head = popped_node.next
            popped_node.next = None
            self.length -= 1
            return popped_node

        elif index < -1 or index >= self.length:
            raise Exception("Index out of range")

        elif index == -1:
            return self.pop()
        else:
            previous = self.get(index-1)
            popped_node = previous.next
            previous.next = popped_node.next
            popped_node.next = None
            self.length -= 1

        return popped_node

    def delete_all(self):
        if self.length == 0:
            return
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0





