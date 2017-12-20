from node import Node

class LinkedList(object):
    def __init__(self, init_value = None):
        '''
        Initialize an empty list or a list with values provided in the init_value
        :param init_value: a list of initial values for corresponding consequtive nodes.
        '''
        if init_value is None or len(init_value) == 0:
            self.head = self.tail = None
        else:
            init_nodes = []
            # initialize a list of nodes with the values in init_value
            for value in init_value:
                init_nodes.append(Node(value))
            # setup the connection between nodes
            for i in range(len(init_nodes) - 1):
                init_nodes[i].set_next_node(init_nodes[i + 1])
            self.head = init_nodes[0]
            self.tail = init_nodes[-1]

    def size(self):
        ''' Returns the size of the linked-list. '''
        if self.head is None: return 0
        n = 0
        current = self.head
        while current.next_node() is not None:
            n += 1
            current = current.next_node()
        return n + 1

    def empty(self):
        ''' Returns True if the list is empty and False otherwise. '''
        return self.head is None

    def value_at(self, index):
        ''' Returns the value at index. '''
        current = self.head
        for i in range(index):
            current = current.next_node()
        return current.value()

    def push_front(self, value):
        ''' Adds an element to the front of the list. '''
        new_node = Node(value, self.head)
        if self.tail is None:  # zero length list
            self.tail = new_node
        self.head = new_node

    def pop_front(self):
        ''' Delete an element from the front of the list and returns its value. '''
        head, value = self.head, self.head.value()
        if self.head == self.tail:  # when there is only one elemnt in the list
            self.tail = head.next_node()
        self.head = head.next_node()
        del head
        return value

    def push_back(self, value):
        ''' Adds an element to the end of the list. '''
        new_node = Node(value)
        if self.tail is None:  # zero length list
            self.tail = self.head = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node

    def pop_back(self):
        ''' Deletes an element from the ened of the list and returns its value. '''
        if self.head == self.tail:
            return self.pop_front()
        new_tail = self.head
        while new_tail.next_node() != self.tail:
            new_tail = new_tail.next_node()
        value = self.tail.value()
        del self.tail
        self.tail = new_tail
        self.tail.set_next_node(None)
        return value

    def front(self):
        ''' Returns the value of the first element of the list. '''
        return self.head.value()

    def back(self):
        ''' Returns the value of the last element of the list. '''
        return self.tail.value()

    def insert(self, index, value):
        ''' Inserts a new element with value at location index. '''
        current = self.head
        if current is None:
            if index == 0:
                self.push_front(value)
                return
            else:
                raise Exception('index out of bound.')
        for i in range(index - 1):
            current = current.next_node()
        new_node = Node(value, current.next_node())
        current.set_next_node(new_node)
        if new_node.next_node() is None: self.tail = new_node  # update the tail if inserting at the end of the list

    def erase(self, index):
        ''' Erases the element at location index. '''
        if self.head == self.tail and index > 0:
            raise Exception('index out of bound.')
        if self.head == self.tail or index == 0:
            self.pop_front()
            return

        current = self.head
        # find the node before location index
        for i in range(index - 1):
            current = current.next_node()

        next_node = current.next_node().next_node()
        node_to_delete = current.next_node()
        del node_to_delete
        current.set_next_node(next_node)

    def value_n_from_end(self, n):
        ''' Returns the value of the n-th element from the end of the list. '''
        size = self.size()
        current = self.head
        for i in range(size - n):
            current = current.next_node()
        return current.value()

    def reverse(self):
        ''' Reverses the list. '''
        current = self.head
        nodes = [current]
        while current.next_node() is not None:
            current = current.next_node()
            nodes.append(current)
        self.head = nodes[-1]
        self.tail = nodes[0]
        for i in range(len(nodes) - 1, 0, -1):
            nodes[i].set_next_node(nodes[i - 1])
        nodes[0].set_next_node(None)

    def remove_value(self, value):
        ''' Remove all elements with the value from the list. '''
        while self.head.value() == value:
            self.pop_front()
        previous = self.head
        current = self.head.next_node()
        while current is not None:
            if current.value() == value:
                previous.set_next_node(current.next_node())
                if current.next_node() is None: # update tail if deleting last element
                    self.tail = previous
                del current
            else:
                previous = current
            current = previous.next_node()

    def __str__(self):
        ''' Prepares a string representation of the values in the link-list'''
        current = self.head
        if current is None: return '[]'
        string = '['
        while current is not None:
            string += str(current.value()) + ', '
            current = current.next_node()
        return string[:-2] + ']'
