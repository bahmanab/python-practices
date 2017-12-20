from linked_list import LinkedList

# some initial tests

print('Initialize A with 1, 2, 4, 8:')
A = LinkedList([1, 2, 4, 8])
print(A, '\n')

print('Erase element at index 2:')
A.erase(2)
print(A, '\n')

print('Push_back(3):')
A.push_back(3)
print(A, '\n')

print('Push_front(2):')
A.push_front(2)
print(A, '\n')

print('Insert 5 at index 1:')
A.insert(1,5)
print(A, '\n')

print('Value 4 from end:', A.value_n_from_end(4), '\n')

print('Reverse the list:')
A.reverse()
print(A, '\n')

print('Remove all elements with value 2:')
A.remove_value(2)
print(A, '\n')

print('Erase element at index 0:')
A.erase(0)
print(A, '\n')

print('A =', A, 'has a size of', A.size(), '\n')

print('Test the code with lists of lenght zero and one:')
print('Initialize B:')
B = LinkedList([1])
print(B, '\n')

print('Pop_front:')
B.pop_front()
print(B, '\n')

print('Push_back 2:')
B.push_back(2)
print(B, '\n')

print('Pop_back:')
B.pop_back()
print(B, '\n')

print('Insert 3 at index 0:')
B.insert(0, 3)
print(B, '\n')

print('Insert 6 at index 1:')
B.insert(1, 6)
print(B, '\n')

print('Pop_back:')
B.pop_back()
print(B, '\n')

print('B =', B, 'has a size of', B.size())