import sys
import json

'''This script will take one argument, the text file output of a twitter stream, and print out the frequency of each unique term from a tweet''' 

def term_list(tweet_file_raw):
    '''This function will open a tweet file, split the content of each 
    tweets text into a list and append the lists of multiple lists into a master list '''
    
    
    total_terms= []
    for line in tweet_file_raw:
        try:#We'll try our entire process for all objects that are tweets and not 'delete' objects (which have no 'text' field)
            
            tweet_index= tweet_index+1
            dataDict= json.loads(line)#Loads first 'line2', which is actually the first json object
            tweet= dataDict['text'].split()#Split text object into a list of terms            
            total_terms.append(tweet)
            
        except:#If not, then:
            print 'Has no text, skip entry'
            continue
    #Now we'll take the contents of the list of lists and return a single list with all the items in one list
    one_list= [item.encode('utf-8') for sublist1 in total_terms for item in sublist1 if len(item)>1]
    return one_list    
    
def main():

    tweet_file = open(sys.argv[1])#Open twitterstream file
    
    #Call function to get list of terms in twitter stream
    one_list= term_list(tweet_file)
    uniqueList= set(one_list)#Filters list to include only unique terms
    uniqueList= list(uniqueList)#Turn the unique set back into a list

    #We'll initialize a list full of zero integers that we'll add to anytime we find an occurrence of our terms
    #We'll then zip this zero list to our list of unique terms, and turn that into a dictionary
    size= len(uniqueList)
    scoreList= [0.0]*size
    uniqueScore= dict(zip(uniqueList,scoreList))
    
    #Now we'll go through the term list we compiled and update (add 1) to the score on our dictionary whenever we find a previous occurrence
    for item in one_list:
        if item in uniqueScore.keys():
            uniqueScore[item] += 1
        else:
            print 'Nothing to see here'
            continue
        #Now we'll print the unique term and its calculated frequency relative to the original list of terms from the twitterstream
        print item, uniqueScore[item]/len(one_list)

if __name__ == '__main__':
    main()
