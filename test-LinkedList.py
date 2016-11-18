from linkedList import Node, LinkedList
import unittest


class LinkedlistTest(unittest.TestCase):

    def test_append_empty(self):
        mylist = LinkedList()
        mylist.append('a')
        assert mylist.head.data == 'a'
        assert mylist.tail.data == 'a'
        assert mylist.head == mylist.tail

    def test_append_two_nodes(self):
        mylist = LinkedList()
        mylist.append('a')
        mylist.append('b')
        assert mylist.head.data == 'a'
        assert mylist.tail.data == 'b'

    def test_append_many_nodes(self):
        mylist = LinkedList()

        mylist.append('a')
        mylist.append('b')
        mylist.append('c')
        mylist.append('d')
        mylist.append('e')
        assert mylist.head.data == 'a'
        assert mylist.tail.data == 'e'

    def test_my_find(self):
        mylist = LinkedList()
        mylist.append('a')
        mylist.append('b')
        mylist.append('c')
        assert mylist.find('b') == 1
        assert mylist.find('d') == -1

    # assert self.mylist.find(lambda data: data > 'b') == 'c'  # => 'c'
    # assert mylist.find(lambda data: data > 'b') == 'c'  # => 'c'

    def test_delete_to_empty(self):
        mylist = LinkedList()

        mylist.append('a')

        mylist.delete('a')
        # print (self.mylist.head.data)
        assert mylist.head is None
        assert mylist.tail is None

    def test_delete_all_nodes_bottom_top(self):
        mylist = LinkedList()

        mylist.append('a')
        mylist.append('b')
        mylist.delete('b')
        mylist.delete('a')

        assert mylist.head is None
        assert mylist.tail is None

    def test_delete_some_nodes(self):
        mylist = LinkedList()

        mylist.append('a')
        mylist.append('b')
        mylist.append('c')
        mylist.append('d')

        mylist.delete('d')
        mylist.delete('c')
        mylist.delete('a')

        assert mylist.head.data == 'b'
        assert mylist.tail.data == 'b'

    def test_delete_random_node(self):
        mylist = LinkedList()

        mylist.append('a')
        mylist.append('b')
        mylist.append('c')

        mylist.delete('b')

        assert mylist.head.data == 'a'
        assert mylist.tail.data == 'c'


if __name__ == '__main__':
    unittest.main()
