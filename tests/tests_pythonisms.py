import pytest
from pythonisms_ll.pythonisms_ll import LinkedList


def test_exists():
    assert LinkedList

def test_instantiate():
    assert LinkedList()

def test_empty_head():
    linked = LinkedList()
    assert linked.head is None
    
def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"
    
def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    linked.insert("orange")
    assert linked.head.value == "orange"
    
def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "NULL"

