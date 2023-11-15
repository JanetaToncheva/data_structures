# using a stack with a linked list means that each element being added to the stack will be appended
# as first to te linked list (head will point to it)

# in a nutshell top element of stack is the head of the linked list

# also, removing an element from top of the stack will mean
# removing the first element (the head) and moving the head to the next

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None  we don't really need a complete fully functioning linked list for this purpose
        # self.length = 0

    def __iter__(self):  # making the linked list iterable for ease of printing
        current = self.head
        while current:
            yield current
            current = current.next


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        to_print = [str(x.value) for x in self.linked_list]
        return "\n".join(to_print)

    def is_empty(self):
        if self.linked_list.head is None:
            return True
        else:
            return False

    def push(self, value):  # adding a value to the stack - appending at beginning
        node = Node(value)
        node.next = self.linked_list.head
        self.linked_list.head = node

    def pop(self):  # removes top element and returns it
        if self.is_empty():
            raise Exception("Empty stack")
        else:
            value_to_pop = self.linked_list.head.value
            self.linked_list.head = self.linked_list.head.next
            return value_to_pop

    def peek(self):  # return the top element but do not remove it
        if self.is_empty():
            raise Exception("Empty stack")
        else:
            return self.linked_list.head.value

    def delete(self):
        self.linked_list = None
        return True


test_stack = Stack()
print(test_stack.is_empty())
test_stack.push(10)
test_stack.push(20)
test_stack.push(30)
test_stack.push(40)
print(test_stack)
print("---------------")
print(test_stack.pop())
print("----------------")
print(test_stack)
