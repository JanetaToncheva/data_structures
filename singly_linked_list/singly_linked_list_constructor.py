# The linked list relies on elements connected between them by pointers to previous element and next element
# Those elements + the connections between them we can call nodes and separate them in another object
# for the purposes of simplicity

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# One option is to create a linked list with one element in it by default
# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         # This will initialize an object linked list with only one element
#         # As it is just one element, the 'head' will point to the first element, which is one element
#         # And the 'tail' will point to the last element, which is also the same element as it's just one element
#         self.length = 1
#         # a counter to help us determine how many elements are in the list

# Another option is to create an empty linked list to begin with

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        # Overriding how to print the object when print(linked_list)
        current_node = self.head
        # starting from the first node which the head points to
        result = ''
        while current_node is not None:
            result += str(current_node.value)
            if current_node.next is not None:
                result += ' --> '
            current_node = current_node.next
        return result

    def append(self, value):
        """
        Will add an element at the end of the linked list and update the pointers accordingly
        """
        # When we create a node / element at the end of a linked list, this means that we now have a new tail
        # which should point to the new last element / node
        # and the previous element should point to the last (next pointer)

        new_node = Node(value)
        if self.head is None:  # means the linked list is empty
            self.head = new_node
            self.tail = new_node
        else:  # linked list has elements inside and was not empty before this append
            self.tail.next = new_node
            # the tail is a node and it has a 'next' property
            # since the tail is the previous last node, we need to make it not a last node anymore
            # the way to do that is to indicate that the previous last node now has a 'next' property
            # the previous last node's 'next' should point to the newly attached element
            self.tail = new_node
            # now the tail needs to be updated to the new node since we no longer want the tail to be
            # the previous last element as we have a new last element
        self.length += 1

    def prepend(self, value):
        """
        Will add an element at the beginning of the linked list and update the pointers accordingly.
        """

        # When creating an element at the beginning of a linked list, we attach it "first" so the head
        # will have to point to the newly attached first node / element
        # also the old head should now become the next of the new first element

        new_node = Node(value)
        if self.head is None:  # the linked list was empty when we started
            self.head = new_node
            self.tail = new_node
        else:  # the linked list has at least one element when we started
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def insert(self, value, index):
        """
        Insert an element / node at a specific location inside an already existing linked list
        """

        # We want a way to get an "index" from the user
        # which will be the place where the new element will be inserted
        # In order to insert successfully at this place, we need to update the pointers
        # The next pointer of the previous element should become the new element
        # The next pointer of the newly inserted element should become the element after it

        new_node = Node(value)

        if index > self.length - 1 or index < 0:
            print("No such index available")
            return None
        elif index == 0:  # want to insert at beginning
            self.prepend(new_node)  # want to insert at the end
        elif index == self.length - 1:
            self.append(new_node)
        else:
            current_node = self.head  # starting from head - loop through the nodes until we reach the desired position

            #                   (new node2)
            #                        |
            # (node0) ---> (node1) ---> (node2) ---> (node3)
            #
            # to get the end result
            #
            # (node0) ---> (node1) ---> (new node2) ---> (node3) ---> (node4)

            for _ in range(index - 1):
                # just looping through nodes using their next pointers until reached the desired position
                # if I want to insert an element at position 2
                # I need to get the next pointer of the newly inserted element
                # to point to the element that will now be after it
                # and then the previous element's next to point to the new element
                current_node = current_node.next

            # now that we have captured the necessary position, we want to update the next of the newly
            # inserted element to point to the element after it
            # and then the previous element's next to point to the new element

            new_node.next = current_node.next
            current_node.next = new_node
        self.length += 1

    def traverse(self):
        """
        Go through the linked list and print out all nodes
        """
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search(self, value):
        """
        Search for a node with given value
        Return True if value exists and False if it doesn't
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def get(self, index):
        """
        Search for value of a node located at given index
        :param index: index number you want to check
        :return: LinkedList object of the node at that index
        """
        current = self.head
        if index == -1:
            return self.tail
        elif index == 0:
            return self.head
        elif 0 < index < self.length:
            for _ in range(index):
                current = current.next
            return current
        else:
            return None

    def set_value(self, index, value):
        """
        Set the node at given index to given value
        :param index:
        :param value:
        :return True if successful, False if not
        """
        current = self.get(index=index)
        if current:
            current.value = value
            return True
        return False

    def pop_first(self):
        """
        Removes the first node of the linked list
        :return: Returns the first element that is now removed
        """
        # When removing the head, we need to also update the element after the old head to be the new head
        # Also, the old head's next pointer should go to None and decrease the length
        # If we have only one node in the linked list to begin with and we want to pop that out
        # we have to also update the tail too.
        # As long as we remove all references and pointers to the element we want to be popped
        # the Python garbage collector will delete it from memory

        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:  # if we had only one element before popping, we should have head and tail both None
            self.tail = None
            self.head = None
            return popped_node
        else:
            self.head = self.head.next
            popped_node.next = None

        self.length -= 1
        return popped_node

    def pop(self):
        """
        Removes last element of the linked list
        :return: returns last element that is now removed
        """
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:  # if we had only one element before popping, we should have head and tail both None
            self.tail = None
            self.head = None
            return popped_node
        else:
            temp = self.head
            for _ in range(self.length-2):
                temp = temp.next
            self.tail = temp
            temp.next = None

        self.length -= 1
        return popped_node

    def remove(self, index):
        """
        Remove a node at a specific index
        """

        # We get an "index" from the user which will be the element to be removed
        # In order to remove we need to update the pointers so that
        # the next pointer of the previous will point to the new next which is the one after the removed node
        # the next pointer of the removed will point to none

        if index == -1 or index == self.length - 1:
            self.pop()
        elif index == 0:
            self.pop_first()
        elif index < -1 or index > self.length - 1:
            return None
        else:
            previous_node = self.get(index-1)
            removed_node = previous_node.next
            previous_node.next = removed_node.next
            removed_node.next = None
            self.length -= 1
            return removed_node

    def delete_all(self):
        """
        Delete all nodes from a linked list
        :return: an empty linked list
        """
        self.head = None
        self.tail = None
        self.length = 0

        # Having head and tail point to nothing will make the other nodes to have no references pointing to them
        # besides each element's previous node's next pointer
        # But since the first node's pointer is the head and it points to None, this will break the link
        # and the garbage collector will remove the obsolete stuff from memory

    def reverse(self):
        """
        Reverses a linked list
        """
        # Original singly linked list: 1 -> 2 -> 3 -> 4 -> 5
        # Reversed singly linked list: 5 -> 4 -> 3 -> 2 -> 1
        # In reality we want to reverse the links between the elements
        # So this is good enough: 1 <- 2 <- 3 <- 4 <- 5

        current_node = self.head
        previous_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def find_middle(self):
        """
        Returns the middle node of the linked list
        """
        middle_node = self.head

        middle_index = self.length // 2

        for _ in range(middle_index):
            middle_node = middle_node.next

        return middle_node

    def find_middle2(self):
        # This returns the middle node using the fast-slow pointer or "tortoise and hare"

        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def remove_duplicates(self):
        """
        Removing duplicated values from a single linked list
        :return: The amended linked list without duplicates
        """
        # Example Original - 1 -> 2 -> 4 -> 3 -> 4 -> 2
        # Result - 1 -> 2 -> 4 -> 3

        if self.head is None:
            return

        node_values = set()  # set to store unique node values
        current_node = self.head
        node_values.add(current_node.value)

        while current_node.next:
            if current_node.next.value in node_values:  # duplicate found
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next

        self.tail = current_node

    def merge_two_sorted_lists(self, list1, list2):
        """
        You are given the heads of two sorted linked lists list1 and list2.
        Merge the two lists in a one sorted list.
        The list should be made by splicing together the nodes of the first two lists.
        Return the head of the merged linked list.

        Example 1:
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]
        Example 2:
        Input: list1 = [], list2 = []
        Output: []
        Example 3:
        Input: list1 = [], list2 = [0]
        Output: [0]

        Constraints:
        The number of nodes in both lists is in the range [0, 50].
        -100 <= Node.val <= 100
        Both list1 and list2 are sorted in non-decreasing order.
        """
        pass






























