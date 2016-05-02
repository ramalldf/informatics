import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    #I can't do stuff from A and B simultaneously because with matrix.json, I'm loading one row (element from matrix) at a time. Mapper will be loading the data into a dictionary.
    
    N= 5#Assumption about length of B
    L= 5#Assumption about length of A
    
    val= []
    
    if record[0] == 'a':
        for k in range(0,N):
            i= record[1]
            
            # id= (record[1],k)# (i,k)
            # Aval= record[3]
            val= record#val= [record[0],record[3]]
            
            #print 'A: ', i,k, val
            mr.emit_intermediate((i,k), val)
         #Above works!
   
    elif record[0] == 'b':
        for i in range(0,N):
            k= record[2]

            # id= (record[1],k)# (i,k)
            # Aval= record[3]
            val= record#[record[0],record[3]]
            
            #print 'B: ', i,k, val
            mr.emit_intermediate((i,k), val)
    
    #print (i,k), val
    #print (i,k), val
    #I think second argument should be same for both right? How do you create a dictionary
    
    #At the end of this, I need to outpuut a PAIR. This pair will be loaded in the reducer and multiplied. The output from this pair product will be the content required for every cell in the final matrix.
def reducer(id, val):
    
    
    subtot=[]
    tot= []
    #varA= []
    #varB= []
    #j = id[1]
    varA= 0
    varB= 0
    
    def getVal(val,strname):
        #print val
        listA= []
        for item in range(0,len(val)):
            if val[item][0] == strname:
                listA.append(val[item])
        return listA
    allA= getVal(val,'a')
    allB= getVal(val,'b')
    
    total= []
    for i in range(0,5):
        matchA= 0
        matchB= 0
        for item in range(0,len(allA)):
            if allA[item][2] == i:
                matchA = allA[item][3]
        for item2 in range(0,len(allB)):
            if allB[item2][1] == i:
                matchB = allB[item2][3]
        total.append(matchA*matchB)
        #print id, i, 'sum:', matchA*matchB
    #print 'Total: ', sum(total)
    finalOut= (id[0],id[1],sum(total))
    mr.emit(finalOut)
        
    



# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
