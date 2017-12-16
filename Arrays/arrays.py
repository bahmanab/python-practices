class Array(object):
    '''
        a class to implement a dynamic array
    '''
    def __init__(self,init_value):
        ''' Initialize the array with input and set size and capacity of the array. '''
        self.arr_size = len(init_value)
        self.arr_capacity = 16
        while self.arr_size > self.arr_capacity:
            self.arr_capacity *= 2
        self.arr_values = [a for a in range(self.arr_capacity)]
        self.arr_values[:self.arr_size] = init_value

    def size(self):
        ''' Return size of the array. '''
        return self.arr_size

    def capacity(self):
        ''' Return current capacity of the array. '''
        return self.arr_capacity

    def is_empty(self):
        ''' Check if the array is empty. '''
        return self.arr_size == 0

    def at(self, index):
        ''' Return an item from the array at the index location. '''
        if index >= self.arr_size: raise Exception('index out of bound.')
        return self.arr_values[index]

    def push(self, item):
        ''' Adds the element with the value item to the end of array. '''
        if self.size() == self.capacity(): self.__resize(2*self.size())
        self.arr_values[self.size()] = item
        self.arr_size += 1

    def insert(self, item, index):
        ''' Insert the item at the location index and shift everything from index to the  end one location to right. '''
        if self.size() == self.capacity(): self.__resize(2*self.size())
        for i in range(self.size(), index, -1):
            self.arr_values[i] = self.arr_values[i-1]
        self.arr_values[index] = item
        self.arr_size += 1

    def prepend(self, item):
        ''' Insert the item at the beginning of the array. '''
        self.insert(item, 0)

    def __resize(self, new_capacity):
        ''' adjust the capacity of the array. '''
        self.new_array = [a for a in range(new_capacity)]
        self.new_array[:self.size()] = self.arr_values[:]
        self.arr_values = self.new_array

    def pop(self):
        ''' remove the last item in the array and return its value. '''
        self.arr_size -= 1
        return self.arr_values[self.arr_size]

    def delete(self, index):
        ''' deletes the element at the location index and shift everythin from that location to end of array to left. '''
        for i in range(index, self.size()):
            self.arr_values[i] = self.arr_values[i+1]
        self.arr_size -= 1

    def __str__(self):
        ''' return an string representing the array. '''
        if self.size() == 0: return '[]'
        string = '['
        for i in range(self.size()):
            string += str(self.at(i)) + ','
        return string[:-1] + ']'


# some tests:
A = Array([2,5])
print('Size: ', A.size(), ' Capacity: ', A.capacity(), 'Is Empty? ', A.is_empty())
print(A,'\n')

A.pop()
A.pop()
print('Size: ', A.size(), ' Capacity: ', A.capacity(), 'Is Empty? ', A.is_empty())
print(A,'\n')

A.push(12)
print('Size: ', A.size(), ' Capacity: ', A.capacity(), 'Is Empty? ', A.is_empty())
print(A,'\n')

A.insert(-5, 1)
print('Size: ', A.size(), ' Capacity: ', A.capacity(), 'Is Empty? ', A.is_empty())
print(A, '\n')

A.prepend(0)
print('Size: ', A.size(), ' Capacity: ', A.capacity(), 'Is Empty? ', A.is_empty())
print(A, '\n')

for j in range(1,13):
    A.push(j)
    print('Size: ', A.size(), ' Capacity: ', A.capacity(), 'Is Empty? ', A.is_empty())
    print(A, '\n')

t = A.pop()
print('Poped the item: ', t)
print('Size: ', A.size(), ' Capacity: ', A.capacity(), 'Is Empty? ', A.is_empty())
print(A,'\n')

A.delete(4)
print('Deleted item at index 4!')
print('Size: ', A.size(), ' Capacity: ', A.capacity(), 'Is Empty? ', A.is_empty())
print(A,'\n')




