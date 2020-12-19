"""
There isn't a built-in data structure in Python that looks like a linked list. Thankfully, it's easy to
make classes that represent data structures in Python!

Here's the code for an Element, which will be a single unit in a linked list:
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


# Now lets set up a LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        """
        If the LinkedList already has a head, iterate through the next reference in every
        Element until you reach the end of the list. Set next for the end of the list to
        be the new_element. Alternatively, if there is no head already, you should just
        assign new_element to it and do nothing else:
        """

        # assign head to variable current
        current = self.head

        # if the head exists
        if self.head:
            # while there is a next node continue iterating by updating current with next node
            while current.next:
                current = current.next

            # when end is reached, make next node the node passed in
            current.next = new_node

        # otherwise if no head make node passed in the head
        else:
            self.head = new_node

    def get_position(self, position):
        """
        Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list.
        """
        # make a counter to keep track of where we are in linked list
        counter = 1

        # assign head to variable current
        current = self.head

        # if they ask for a position that doest exist return none
        if position < 1:
            return None

        # while there is something as current and counter is less than or eq to position
        # move along the linked list until the position matches counter
        while current and counter <= position:
            # once it matches, return that position
            if counter == position:
                return current

            # keep moving along linked list
            current = current.next

            # increment counter
            counter += 1

        # if code reaches here, position not found
        return None

    def insert(self, new_node, position):
        """
        Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
            the 2nd and 3rd elements.
        """
        # make a counter to keep track of where we are in linked list
        counter = 1

        # assign head to variable current
        current = self.head

        # if place to enter is not the head
        if position > 1:
            # while there is something in the current node
            while current and counter < position:
                # if you are at the node before the insert
                if counter == position - 1:
                    # make the new node's next be the current node's next value
                    new_node.next = current.next
                    # make the current node's next be the new node
                    current.next = new_node

                # move along the linked list
                current = current.next

                # update counter
                counter += 1

        # if position is 1 that means its the head
        elif position == 1:
            # makes the head the next node
            new_node.next = self.head
            # and make the new head, the new node
            self.head = new_node

    def delete(self, value):
        """Delete the first node with a given value."""
        # assign head to variable current
        current = self.head

        # make a variable for the previous pointer
        previous = None

        # while we are not at the node with value to be deleted and there
        # are still other nodes
        while current.value != value and current.next:
            # save the current node in the previous variable
            previous = current
            # and move forward in the linked list
            current = current.next

        # once we get to the value to be deleted
        if current.value == value:
            # if there was a previous node
            if previous:
                # make its next node be the current node's next
                previous.next = current.next
            else:
                # otherwise we are deleting the head and the next node becomes the head
                self.head = current.next

# Test cases
# Set up some Elements
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)