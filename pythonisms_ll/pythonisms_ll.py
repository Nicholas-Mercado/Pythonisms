class LinkedList:
    '''
    Methods:
    insert --> adds node to front of list
    '''
    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection):
                self.insert(item)

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
    
    def __iter__(self):
        
        def generator():
            
            current = self.head
            while current:
                yield current.value
                current = current.next

        return generator()


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


