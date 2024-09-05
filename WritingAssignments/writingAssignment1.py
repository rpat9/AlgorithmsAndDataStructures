# Chapter-1: R-1.2: Write a short Python function, is even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.

def isEven(k):
    if k & 1 == 0:  # Checks last digit of binary number
        return True
    return False

print(isEven(11)) # Output --> False
print(isEven(12)) # Output --> True

# R-1.4: Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.

def sumOfSquares(n):
    if n < 0: n = abs(n) # Accounts for negative numbers
    
    sum = 0
    
    while n > 0:
        n-=1
        sum+=n**2
    
    return sum

print(sumOfSquares(5)) # Output --> 30

# C-1.15: Write a Python function that takes a sequence of numbers (separated by space) and determines if all the numbers are different from each other (that is, they are distinct).

def isDistinct(sequence): # The datatype of the parameter is String
    numbers = sequence.split()
    
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i]) # Convert to integers
    
    mySet = {nums for nums in numbers} # Putting same values in set
    
    if len(mySet) == len(numbers):  print('They are distinct!')
    else: print('They are not distinct!')
    
isDistinct('1 2 3 4') # Output --> They are distinct!
isDistinct('1 2 2 3') # Output --> They are not distinct!

# C-1.24: Write a short Python function that counts the number of vowels in a given character string.

def countVowels(anyString):
    vowelCount = 0
    vowelString = 'aeiou'

    for character in anyString:
        if character.lower() in vowelString:  # Accounts for uppercase letters by converting them to lower before counting
            vowelCount+=1
    
    return vowelCount

print(countVowels('vowEl')) #Output --> 2

# C-1.17: Had we implemented the scale function (page 25) as follows, does it work properly? 
# The code will have an issue. This is because the val variable is defined in the loop and will not affect the values in the 'data'. To make it work, we need to add a line which will update values in 'data'.