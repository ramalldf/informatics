import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
'''This script will allow us to load the DNA sequence data and trim the last 10 bases from the sequence'''
def mapper(record):
    '''Very straight forward loading of key:value'''
    key = record[0]
    value = record[1]
    
    mr.emit_intermediate(key, value)

def reducer(key, value):
    # key: word
    # value: list of occurrence counts
    value= str(value)
    last= len(value[0])
    #print 'Longest is: ', last
    newSeq= str(value[0:last-10+1])
    newSeq= newSeq.encode('utf-8')
    print type(newSeq)
    newSeq2= newSeq[3:len(newSeq)-4]#We're using these '3' and '4' because currently our string includes the quotation marks so accounting for those to just isolate the base sequence.
    print len(mr.result)

    
    if newSeq2 not in mr.result:#Only adding original values to results list.
        mr.emit(newSeq2)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
