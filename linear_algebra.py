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

def vector_sum(*args):
    lengthy = [len(z) for z in args]
    if max(lengthy) != min(lengthy):
        raise ShapeError
    return[sum(x) for x in zip(*args)]

def dot(*args):
    return[sum(x, 0) * (x, 1) for x in args]

def vector_multiply(value,other):
    product = [x*x for x in (value,other)]
    return product

def vector_mean(value,other):
    return[x for x in (value,other)]
    pass

def magnitude(value,other):
    (value**2 + other**2)**.5
    pass
