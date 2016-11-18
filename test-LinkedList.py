from linkedList import Node, LinkedList
import unittest


class LinkedlistTest(unittest.TestCase):
    mylist = LinkedList()

    mylist.append('a')
    mylist.append('b')
    mylist.append('c')

    def test_head(self):
        assert self.mylist.head.data == 'a'  # => 'a'

    def test_tail(self):
        assert self.mylist.tail.data == 'c'  # => 'c'

    def test_my_find(self):
        assert self.mylist.find('b') == 1
        assert self.mylist.find('d') == -1

    # assert self.mylist.find(lambda data: data > 'b') == 'c'  # => 'c'
    # assert mylist.find(lambda data: data > 'b') == 'c'  # => 'c'

    # def test_delete(self):
    #     self.mylist.delete('a')
    #     print (self.mylist.head.data)
    #     assert self.mylist.head.data == 'b'  # => 'b'

if __name__ == '__main__':
    unittest.main()
