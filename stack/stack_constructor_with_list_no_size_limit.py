# Implementing stack with Python list - stack will have no size limit
# Easier, slower due to memory allocation as consecutive blocks for all elements
# As size of stack grows, performance will get worse

class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    # to print them out from last element at the top to first element at the bottom

    def is_empty(self):
        if not self.list:
            return True
        else:
            return False

    def push(self, value):  # to add element to the stack
        self.list.append(value)
        return True

    def pop(self):  # remove the top element from the stack and return it
        # the top element of the stack is the last element of the list
        if self.is_empty():
            raise Exception("Empty stack")
        else:
            return self.list.pop()

    def peek(self):  # check which is the last (top) element and return it
        if self.is_empty():
            raise Exception("Empty stack")
        else:
            return self.list[-1]

    def delete(self):
        self.list = None







test_stack = Stack()
test_stack.push(4)
test_stack.push(5)
test_stack.push(3)
print(test_stack)
print("---------------------")
test_stack.pop()
print(test_stack)
print("---------------------")
print(test_stack.peek())

