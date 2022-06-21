'''
make a command line calculator

DIFFICULTY = MEDIUM
TOPICS = strings, variables, lists

your task is to write a command line calculator
this task is easy since we can use the eval function to do most of the legwork
however, we need to parse possible invalid user input. This is your task

return None if invalid input. Otherwise return the result
'''

def calculate(s):
    '''
    >>> calculate("1+3")
    4
    >>> calculate("1+3*4/3")
    5.0
    >>> calculate("(1+3)*5")
    20
    >>> calculate("-----1")
    -1
    >>> calculate("-+-1")
    1
    >>> calculate(\'print("bad guy coming to hack")\')
    '''
    # TODO = fill in this function 
    
   legal = "+-/*%0123475367"
    
    #for i in s:
        
    for i in range(0, len(s)):
        check = 0
        if (s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/' or
            s[i] == '(' or s[i] == ')' or s[i].isdigit() == True):
            check = 1
        else:
            break
    if check == 0:
        return None
    else:
        return eval(s)
        
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
