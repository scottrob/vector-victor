class ShapeError(Exception):
    pass

def how_you_use_it(value,other):
    if len(value) != len(other):
        raise ShapeError()
    else:
        return True

def shape(value):
    return(len(value),)

def vector_add(value,other):
    if how_you_use_it(value,other):
        return[x+y for x,y in zip(value,other)]

def vector_sub(value,other):
    if how_you_use_it(value,other):
        return[x-y for x,y in zip(value,other)]
