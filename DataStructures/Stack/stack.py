from DataStructures.List import single_linked_list as all

def new_stack ():
    
    new_stack = all.new_list()
    return new_stack 

def push (my_stack, element):
    all.add_last(my_stack, element)
    return my_stack 

def pop ():
    