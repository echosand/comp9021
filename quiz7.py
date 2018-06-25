import sys
from random import seed, randrange

from linked_list_adt import *
from extended_linked_list import ExtendedLinkedList


def collect_references(L, length):
    node = L.head
    references = set()
    for i in range(length):
        references.add(id(node))
        node = node.next_node
    return references

