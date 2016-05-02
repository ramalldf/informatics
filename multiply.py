import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    '''This fxn will organize the sparse matrix data from matrix.json into a dictionary where the keys will be the coordinates for matrix C (resulting matrix from multiplying matrix A and B).'''
    
    N= 5#Assumption about length of B
    L= 5#Assumption about length of A
    
    #We'll initialize the values matrix for our key i,k (i,k because resulting element in matrix c from A(i,j) * B(j,k) is C(i,k)
    val= []
    
    #Sort data from matrix 'a'
    if record[0] == 'a':
    #Since in matrix multiplication we use row, col value from same row for all columns of new matrix, we'll make copies of our columns and append the value of our 'a' cell appropriately (k times if length of matrix B is N)
        for k in range(0,N):
            i= record[1]#Make the i coordinate the same as i for matrix A
            #k just equals k
            val= record#We'll append all values from record to our value list
            
            #print 'A: ', i,k, val
            mr.emit_intermediate((i,k), val)
         #Above works!
    
    #Now we'll do the same thing we did for matrix A for matrix B
    elif record[0] == 'b':
        for i in range(0,N):
            k= record[2]
            val= record
            mr.emit_intermediate((i,k), val)
    
def reducer(id, val):
    '''This fxn will allow us to perform the sum(A[i,k]*B[i,k]) operation for each element in matrix C. We'll do a few for loops to make sure we organize our A matrix data and B matrix data appropriately. Then we'll perform the multiplication and sum operations and format the data to look like 'multiply.json' solution ([i,k,val]).'''
    
    #Initialize placeholder variables
    subtot=[]

    varA= 0
    varB= 0
    
    def getVal(val,strname):
        '''Makes a list of all variables in val that came from matrix strname '''
        listA= []
        for item in range(0,len(val)):
            if val[item][0] == strname:
                listA.append(val[item])
        return listA
    #Separate data from matrices A and B
    allA= getVal(val,'a')
    allB= getVal(val,'b')
    
    #For all possible values of i (corresponding to coord j, shared by both matrices), if there are any values with keys that match i, append to a new list matchA (or matchB for matrix B)
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
        total.append(matchA*matchB)#Multiplication step, append to list to sum
        #print id, i, 'sum:', matchA*matchB
    #print 'Total: ', sum(total)
    finalOut= (id[0],id[1],sum(total))#Get sum and insert into list w/coordinates of matrix C
    mr.emit(finalOut)#Output is this new list
        
    



# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
