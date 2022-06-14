class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        current = self.head
        self.head = Node(value, current)
        
    def __str__(self):
        null = 'NULL'
        if self.head is None:
            return null
        current = self.head
        output = ''
        while current:
            output += '{ ' + str(current.value) + ' }' + ' -> '
            current = current.next
        print(output + null)
        return output + null


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
