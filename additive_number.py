
def isAdditiveNumber(num):
    """A valid additive sequence should contain at least three numbers. 
    Except for the first two numbers, 
    each subsequent number in the sequence must be the sum of the preceding two.
    Numbers in the additive sequence cannot have leading zeros, 
    so sequence 1, 2, 03 or 1, 02, 3 is invalid.

    >>> num = "123"
    >>> isAdditiveNumber(num)
    True
    >>> num = "1023"
    >>> isAdditiveNumber(num)
    False
    >>> isAdditiveNumber("1203")
    False
    >>> isAdditiveNumber("1123581321")
    True
    """
    def isAdditive(num, first, second):
        if len(num) == 0:
            return True
        for i in range(1, len(num) + 1):
            if len(num[:i]) > 1 and num[:i][0] == "0":
                continue
            n0 = int(num[:i])
            if first + second == n0 and isAdditive(num[i:], second, n0):
                return True
        return False
            
    for i in range(1, (len(num) + 1)//2):
        for j in range(i+1, len(num)):
            astr = num[:i]
            bstr = num[i:j]
            if (len(astr) > 1 and astr[0] == "0") or (len(bstr) > 1 and bstr[0] == "0"):
                continue
            a = int(astr)
            b = int(bstr)
            if isAdditive(num[j:], a, b):
                return True
    return False
                        

def _test():
    import doctest
    doctest.testmod()
    
if __name__ == "__main__":
    _test()