import sys
from random import seed, randrange
from binary_tree_adt import *

# Possibly define some functions

def max_diff_in_consecutive_leaves(tree):
    L=findleaves(tree)
    if len(L)==0 or len(L)==1:
        return 0
    else:
        L1=[]
        for i in range(len(L)-1):
            L1.append(abs(L[i+1]-L[i]))
        return max(L1)

    
def findleaves(tree):
    if tree.value is None:
        return []
    values=findleaves(tree.left_node)
    values.extend(findleaves(tree.right_node))
    if tree.left_node.value is None and tree.right_node.value is None:
        values.append(tree.value)
    return values



provided_input = input('Enter two integers, the second one being positive: ')
try:
    arg_for_seed, nb_of_nodes = provided_input.split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, nb_of_nodes = int(arg_for_seed), int(nb_of_nodes)
    if nb_of_nodes < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = randrange(1000000)
    tree.insert_in_bst(datum)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
print('The maximum difference between consecutive leaves is: ', end = '')
print(max_diff_in_consecutive_leaves(tree))
           
