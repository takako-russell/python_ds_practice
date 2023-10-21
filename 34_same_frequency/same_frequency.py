def create_hash(vals):
    counter ={}

    for n in vals:
        counter[n] = counter.get(n,0) +1

    return counter


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return create_hash(str(num1)) == create_hash(str(num2))
