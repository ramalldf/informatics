'''All of the functions here have been verified to work correctly'''

def countVowels(s):
    '''From EdX6.00.1x: Week2 PS1.1 Assume s is a string of lower 
    case characters. Write a program that counts up the number 
    of vowels contained in the string s. Valid vowels are: 
    'a', 'e', 'i', 'o', and 'u'. 
    This function takes a given word, lowers its case and 
    compares it to a list of vowels to see if the characters
    in s are vowels then adds 1 to a counter if they are, finally
	printing the count at the end'''
    ref= ['a','e','i','o','u']
    count= 0
    s= s.lower()
    for i in range(0,len(s)):#Iterate through s
        print s[i]#Prints character
        if s[i] in ref:#Check if character in list of vowels
            count +=1#Add to count everytime if finds vowel
    print 'Number of vowels: ', count
##########################################################

def countBob(s):
    '''From EdX6.00.1x: Week2 PS1.2
    Assume s is a string of lower case
    characters. Write a program that prints
    the number of times the string 'bob'
    occurs in s.'''
    s= s.lower()#Lower case of word
    pattern= 'bob'#Define pattern
    count= 0#Initialize count
    for i in range(0,len(s)):#Iterate through s
        comp= s[i:i+3]#Make new subset of s to compare against pattern
        #if pattern in comp:#This works too but less certain on limits
        if comp == pattern:#If subset equals pattern add 1
            count += 1#Add to count
    return count
    
    
def iterPower(base,exp):
    '''From EdX6.00.1x: Week3: L5 Problem 1
    First  way of solving exponiation of base. Have zero and 1 base cases
    with iterative steps'''
    tot= base
    if exp== 0:
        return 1 
    else:
        for i in range(1,exp):
            print i
            tot= tot*base
    return tot    
    

    def recurPower(base,exp):
    '''From EdX6.00.1x: Week3: L5 Problem 2
    second  way of solving exponiation of base. Have zero and 1 base cases
    with recursive step'''
    if exp== 0:#Base case
        return 1 
    elif exp ==1:
        return base
    else:
        return tot*recurPower(base,exp-1)
        
def recurPowerNew(base,exp):
    '''From EdX6.00.1x: Week3: L5 Problem 3
    Use third way of solving this equation. Have zero and 1 base cases
    but also odds and evens: odds is same as regular recursion, evens
    is (base squared)^exp/2'''
    if exp== 0:#Base case
        return 1 
    elif exp ==1:
        return base
    else:
        if exp%2 ==0:
            return recurPowerNew(base*base,exp/2)
        else:
            return base*recurPowerNew(base,exp-1)
            
def gcdIter(a,b):
    '''From EdX6.00.1x: Week3: L5 Problem 4
    Given positive integers a,b find the
    greatest common denominator (largest integer 
    that divides each of them without remainder. 
    Write an iterative function, gcdIter(a, b), 
    that implements this idea. One easy way to do 
    this is to begin with a test value equal to t
    he smaller of the two input arguments, and 
    iteratively reduce this test value by 1 until
    you either reach a case where the test divides 
    both a and b without remainder, or you reach 1.)'''
    
    testVal= min(a,b)#Find the min of both and set as test value
    while testVal > 0:#Know it has to be positive
        if (a%testVal ==0 and b%testVal == 0):#Set conditions for correct answer
            return testVal
        elif testVal == 1:#Set condition for test value = 1
            return 1
        else:#Set condition for test val not correct and decreasing by 1
            testVal -=1
            
            
def gcdRecur(a,b):
    '''From EdX6.00.1x: Week3: L5 Problem 5
    A clever mathematical trick (due to Euclid) 
    makes it easy to find greatest common divisors.
    Suppose that a and b are two positive integers:
    If b = 0, then the answer is a, Otherwise, 
    gcd(a, b) is the same as gcd(b, a % b). Write a 
    function gcdRecur(a, b) that implements this idea 
    recursively. This function takes in two positive 
    integers and returns one integer.'''
    
    if b == 0:
        return a
    else:
        return gcdRecur(b,a%b)
        
def lenIter(aStr):
    '''From EdX6.00.1x: Week3: L5 Problem 6
    Write an iterative function, lenIter, which 
    computes the length of an input argument 
    (a string), by counting up the number of 
    characters in the string.'''
    
    count= 0
    for i in aStr:
        count+=1
    return count
    
def lenRecur(aStr):
    '''From EdX6.00.1x: Week3: L5 Problem 7 
    write a recursive function, lenRecur, which computes 
    the length of an input argument (a string), by counting up
    the number of characters in the string. Function here doesn't have
    to initialize a variable total. You could also return 0 for base case
    and return 1+lenRecur(aStr[1::]) and you'd get same answer btw'''
    
    total= 0#Initialize counter
    if aStr == '':#Base case: If string empty, return counter
        return total
    else:
        total +=1 #Add one to counter
        #print aStr, total
        return total + lenRecur(aStr[1::]) 
        #For final line, return total + output of lenRecur on shortened aStr
        #(which at most basic form should be +1 sequentially)
        
def isIn(char,aStr):
    '''From EdX6.00.1x: Week3: L5 Problem 8
    Checks if a character char is in a string aStr using recursion
    '''
    
    aStr= sorted(aStr)#First step is to sort
    mid= len(aStr)/2#Second step is to find mid character
    if len(aStr) == 0:#Base case 1 (no characters)
        return False
    elif len(aStr) <= 2:#Base case 2 (two characters, no mid)
        print 'No half for two', aStr
        if char == aStr[0] or char == aStr[1]:
            return True
        else:
            return False
        return isIn(char,aStr[:1])
    elif aStr[mid] == char:
        print 'Found it'
        return True
    elif char < aStr[mid]:
        print 'char is lower', aStr[mid], aStr
        return isIn(char,aStr[:mid+1])
        #return isIn(char,aStr[:mid]) #also works
    elif char > aStr[mid]:
        print 'char is higher', aStr[mid], aStr
        return isIn(char,aStr[mid:])#Be careful with extra colons! To span in slice just use one colon!
        #return isIn(char,aStr[mid+1:])#also works
    else:#This would be condition for not present, but never gets here
        print 'Not here!'
        return False
        
def ndigits(x):
    '''From EdX6.00.1x: Week3: Code grader
    Write a function called ndigits, 
    that takes an integer x (either positive or 
    negative) as an argument. This function 
    should return the number of digits in x'''
    new= abs(x)
    if new==0:
        return 0
    else:
        return 1+ndigits(new/10)