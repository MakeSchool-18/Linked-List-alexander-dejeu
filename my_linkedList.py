class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        # If the head is None then this is first item being added
        if self.head is None:
            self.head = Node(value, None)
            self.tail = self.head
        # If the head and tail equal eachother then there should only be one
        # element.
        elif self.head == self.tail:
            self.tail = Node(value, None)
            self.head.next = self.tail
        # All other cases should just update the old and new tail data
        else:
            new_tail = Node(value, None)
            self.tail.next = new_tail
            self.tail = new_tail

    def find(self, value):
        current_node = self.head

        if current_node.data == value:
            return 1

        while current_node.next is not None:
            if current_node.data == value:
                return 1
            current_node = current_node.next

        return -1
        # if current_node.next

    def delete(self, value):
        # Find the Node
        current_node = self.head
        if self.head.data == value and self.head == self.tail:
            self.head = current_node.next
            self.tail = self.head
            return 1

        if self.head.data == value:
            self.head = current_node.next
            return 1

        while current_node.next is not None:
            if current_node.next.data == value:
                if current_node.next == self.tail:
                    self.tail = current_node
                    current_node.next = current_node.next.next
                    return 1
                current_node.next = current_node.next.next
                # TODO: How to free memory in python?

                return 1
            current_node = current_node.next

        return -1

        pass
