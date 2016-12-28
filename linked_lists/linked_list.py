class cell:
    '''
    Class that represents the linked list
    '''

    def __init__(self, value=None, child=None):
        self.value = value
        self.child = child

    def __str__(self):
        return str(self.value)


def iterate(top):
    '''
    Creates a generator object over the linked list.
    '''
    while top is not None:
        yield top.value
        top = top.child


def find_value(top, target):
    '''
    Looks for a value in the linked list and returns the node that contains
    that value. Returns None if the value is not in the list.
    '''
    while top is not None:
        if top.value == target:
            return top
        top = top.child
    return


def find_cell_before(top, target):
    '''
    Looks for a value in the linked list an returns the parent node of the node
    that contains that value. Returns None if the value is not in the list.
    Returns a sentinel cell if the target value is at the first cell. The
    sentinel is a cell with a None value and points to the top of the list.
    '''
    if top is None:
        return
    if top.value == target:
        return cell(None, top)
    while top.child is not None:
        if top.child.value == target:
            return top
        top = top.child
    return
