#!/usr/bin/python3
"""
Python function that adds two numbers

    -- a and b must be integers or floats, otherwise raise a TypeError 
    exception with the message "a must be an integer or b must be an integer"

    -- a and b must be first casted to integers if they are floats

    -- b is set to a default value of 98 if a value is not provided
    
    -- Returns an integer: the addition of a and b


"""
def add_integer(a, b=98):
    """
    Returns sum of a and b
    

    - Args :
        a: int or float
        b: int or float, default 98
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
