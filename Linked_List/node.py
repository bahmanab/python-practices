class Node(object):
    '''
        Node object for a singly linked-list which keep a value, reference to the next node.
        It provide set_value and set_next_node methods for settings those properties and
        value() and next_node() for getting those values.
    '''
    def __init__(self, value, next_node = None):
        self.__value = value
        self.__next_node = next_node

    def set_value(self, value):
        self.__value = value

    def set_next_node(self, next_node):
        self.__next_node = next_node

    def next_node(self):
        return self.__next_node

    def value(self):
        return self.__value


