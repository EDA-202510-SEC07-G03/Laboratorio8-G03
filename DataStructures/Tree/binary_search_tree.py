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

def contains(my_bst, key):
    result = get(my_bst, key)
    if result is None:
        return False
    else:
        return True  

def key_set_tree(root):
    list_retorno = sl.new_list()
    if root == None:
        return list_retorno
    else:
        sl.add_last(list_retorno, root["key"])
        key_set_tree(root["left"])
        key_set_tree(root["right"])
    return list_retorno

def key_set(my_bst):
    return key_set_tree(my_bst["root"])

def value_set_tree(root):
    list_retorno = sl.new_list()
    if root == None:
        return list_retorno
    else:
        sl.add_last(list_retorno, root["value"])
        value_set_tree(root["left"])
        value_set_tree(root["right"])
    return list_retorno

def value_set(my_bst):
    return value_set_tree(my_bst["root"])

def get_min_node(root):
    result = None
    if root != None:
        result = root["key"]
        get_min_node(root["left"])
    return result

def get_min(my_bst):
    return get_min_node(my_bst["root"])

def get_max_node(root):
    result = None
    if root != None:
        result = root["key"]
        get_max_node(root["right"])
    return result

def get_max(my_bst):
    return get_max_node(my_bst["root"])

def keys_range(root, key_i, key_f, list_key):
    if root == None:
        return list_key
    else:
        if key_i <= root["key"] <= key_f:
            sl.add_last(list_key, root["key"])
        keys_range(root["left"], key_i, key_f, list_key)
        keys_range(root["right"], key_i, key_f, list_key)
    return list_key

def keys(my_bst, key_i, key_f):
    list_keys = sl.new_list()
    return keys_range(my_bst["root"], key_i, key_f, list_keys)

def values_range(root, value_i, value_f, list_value):
    if root == None:
        return list_value
    else:
        if value_i <= root["value"] <= value_f:
            sl.add_last(list_value, root["value"])
        values_range(root["left"], value_i, value_f, list_value)
        values_range(root["right"], value_i, value_f, list_value)
    return list_value

def values(my_bst, value_i, value_f):
    list_values = sl.new_list()
    return values_range(my_bst["root"], value_i, value_f, list_values)

        
            
