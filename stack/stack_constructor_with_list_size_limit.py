class Stack:
    def __init__(self, maximum_size):
        self.max_size = maximum_size
        self.list = []

    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def is_empty(self):
        if not self.list:
            return True
        else:
            return False

    def is_full(self):  # checks if the stack is full based on the defined max_size when creating the stack
        if len(self.list) == self.max_size:
            return True
        else:
            return False

    def push(self, value):  # adds an element to the stack
        if self.is_full():
            raise Exception("Stack at maximum capacity")
        else:
            self.list.append(value)
        return True

    def pop(self):  # removes top (last) element from the stack and returns it
        if self.is_empty():
            raise Exception("Empty stack")
        else:
            return self.list.pop()

    def peek(self):  # returns the last element from the stack (top one) but does not remove it
        if self.is_empty():
            raise Exception("Empty stack")
        else:
            return self.list[-1]

    def delete(self):
        self.list = None


test_stack = Stack(maximum_size=10)
print(f"Empty: {test_stack.is_empty()}")
print(f"Full: {test_stack.is_full()}")
test_stack.push(10)
test_stack.push(20)
test_stack.push(30)
test_stack.push(40)
test_stack.push(50)
test_stack.push(60)
print(f"Empty after adding elements: {test_stack.is_empty()}")
print(test_stack)





