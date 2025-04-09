from DataStructures.Tree import bst_node as bst
from DataStructures.Map import map_linear_probing as lp
from DataStructures.List import array_list as ar
from DataStructures.List import single_linked_list as sl
def new_map():
    root = {"root": None}
    return root

def get_node(root, key):
    result = None
    if root != None:
        if key == root["key"]:
            result = bst.get_value(root)
        elif key < root["key"]:
            result = get_node(root["left"], key)
        else:
            result = get_node(root["right"], key)
    return result

def get(my_bst, key):
    return get_node(my_bst["root"], key)

def insert_node(root, key, value):
    if root == None:
        root = bst.new_node(key, value)
    elif root["key"] == key:
        root["value"] = value
    else:
        if key <= root["key"]:
            root["left"] = insert_node(root["left"], key, value)
        elif key > root["key"]:
            root["right"] =  insert_node(root["right"], key, value)
    root["size"] = 1 + size_tree(root)
    return root

def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst 

def size_tree(root):
    counter = 0
    if root == None:
        return counter
    else:
        counter += size_tree(root["left"])
        counter += size_tree(root["right"])
    return counter

def size(my_bst):
    return size_tree(my_bst["root"])

