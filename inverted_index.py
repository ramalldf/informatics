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
    key = record[0]
    value = record[1]
    words = value.split()
    #So parsing is complete, now need to change next step (original in ##) to add a second argument to mr.emit_intermediate that incorporates the key instead of a 1
    ## for w in words:
      ## mr.emit_intermediate(w, 1)
    for w in words:
        mr.emit_intermediate(w,key)
    
    

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    # # total = 0
    # # for v in list_of_values:
      # # total += v
    # # mr.emit((key, total))
    
    total = []
    for v in list_of_values:
        total.append(v)
    total= list(set(total))
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
