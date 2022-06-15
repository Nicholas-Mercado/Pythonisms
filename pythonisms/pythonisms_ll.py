class LinkedList:
    '''
    Methods:
    insert --> adds node to front of list
    '''
    def __init__(self, collection=None):
        self.head = None
        self.length = 0
        if collection:
            for item in reversed(collection):
                self.insert(item)

    def insert(self, value):
        current = self.head
        self.head = Node(value, current)
        self.length += 1
        
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
    
    def __len__(self):
        return self.length
    
    def __eq__(self , other):
        return list(self) == list(other)
    
    def __getitem__(self, idx):
        
        for i, item in enumerate(self):
            if i == idx:
                return item

        raise IndexError
    


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


