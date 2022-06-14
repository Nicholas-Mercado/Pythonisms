import pytest
from pythonisms_ll.pythonisms_ll import LinkedList


def test_exists():
    assert LinkedList

def test_empty_head():
    linked = LinkedList()
    assert linked.head is None
    
def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"
    
def test_populated_head_next():
    linked = LinkedList()
    linked.insert("apple")
    linked.insert("orange")
    assert linked.head.value == "orange"
    
def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "NULL"

# add ability to be used in a for in loop

def test_for_in():
    
    ll = LinkedList()
    ll.insert("apple")
    ll.insert("apple2")
    ll.insert("apple3")
    ll.insert("apple4")
    
    apple_list = []
    
    for link in ll:
        apple_list.append(link)
        
    assert apple_list == ["apple4","apple3","apple2","apple"]
    
def test_for_in_then_do_something():
    
    ll = LinkedList()
    ll.insert("apple")
    ll.insert("apple2")
    ll.insert("apple3")
    ll.insert("apple4")
    
    apple_list = []
    
    for link in ll:
        link = link.upper()
        apple_list.append(link)
        
    assert apple_list == ['APPLE4', 'APPLE3', 'APPLE2', 'APPLE']
# add ability to be used in a list comprehension

def test_list_comprehension():
    
    ll = LinkedList(("apple4","apple3","apple2","apple"))
    
    upper_ll = [link.upper() for link in ll]
    
    assert upper_ll == ['APPLE4', 'APPLE3', 'APPLE2', 'APPLE']
    


# add ability to convert to a list or other collection type

def test_list__can_cast():

    food_list = ["apple","banana","cucumber"]

    foods = LinkedList(food_list)

    assert list(foods) == food_list
    
def test_can_range():
    range1 = range(1, 51)
    ll = LinkedList(range1)
    
    assert len(ll) == 50
    
def test_can_filter():
    
    ll = LinkedList(range(1,11))
    
    even = [num for num in ll if num % 2 == 0]
    
    assert even == [2, 4, 6, 8, 10]
    
def test_next():
    
    ll = LinkedList(("apple","apple3","apple2"))

    iterator = iter(ll)
    
    assert next(iterator) == "apple"
    assert next(iterator) == "apple3"
    
def stop_iter():
    ll = LinkedList(("apple","apple3","apple2"))
    iterator = iter(ll)

    with pytest.raises(StopIteration):
        while True:
            ll = next(iterator)
