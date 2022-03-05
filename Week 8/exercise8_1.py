exList = ["this", "is", "a", "list"]

def chop(lst):
    del lst[0]
    del lst[-1]

def middle(lst):
    newList = lst[1:]
    del newList[-1]
    return newList



print("Middle of list: ", middle(exList))
