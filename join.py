import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = str(record[1])
    value = record#We'll insert group into list of values
    # words = value.split()
    # for w in words:
      # mr.emit_intermediate(w, key)
    
    #words= value.split()
    
    mr.emit_intermediate(key, value)#Cool this creates correct intermediate key

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    
    #Recall that map fxn has completed for each line already (try a print statement in it if you don't believe it)
    #Now we'll iterate through elements in list_of_values starting from the second one, to see if they match our key/first element
    for i in range(1, len(list_of_values)):
       if key in list_of_values[i][1]:#Recall that for each element, first term ([i][1]) is the id/key for that entry; could also use 'key == list_of....[i][1]: '
            #If condition met, add first list and match and feed to mr.emit
            mr.emit(list_of_values[0]+list_of_values[i])
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
