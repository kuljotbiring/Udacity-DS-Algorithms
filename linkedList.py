"""
There isn't a built-in data structure in Python that looks like a linked list. Thankfully, it's easy to
make classes that represent data structures in Python!

Here's the code for an Element, which will be a single unit in a linked list:
"""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


# Now lets set up a LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """
        If the LinkedList already has a head, iterate through the next reference in every
        Element until you reach the end of the list. Set next for the end of the list to
        be the new_element. Alternatively, if there is no head already, you should just
        assign new_element to it and do nothing else:
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element