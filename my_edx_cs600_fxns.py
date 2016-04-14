#The following are functions that I wrote during the coursework for edx 6.00.1x intro to cs and programming using python

def iterPower(base, exp):
    '''
    L5 Prob 1 (validated): Code calculates powers using a for loopbase: int or float. 
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    tot= base
    if exp==0:
        tot=1
    else:
        for i in range(1,exp):
            tot= tot*base
    return tot
    
