import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    
    key = record[0]#Just uses first name (of 2 name list) as key
    
    #We'll add a 1 every time a name appears for every record
    #This will be the second arg in the mr.emit_intermediate fxn
    mr.emit_intermediate(key, 1)

def reducer(key, interm_val):
    # key: word
    # value: list of occurrence counts
    #print key, apple
    total= (key,sum(interm_val))
    
    #print type(total)

    mr.emit(total)
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
