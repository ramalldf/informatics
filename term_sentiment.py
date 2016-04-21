import sys
import json

#==Build AFINN-111 dictionary from sent_file

def tweet_text(tweet_file):
    '''This function will open a tweet file and return the text from each tweet '''  
    tweet_index= 0#Initialize a counter to keep track of tweet we're on
    tweet_list= []
    for line in tweet_file:
            tweet_index= tweet_index+1
            dataDict= json.loads(line)#Loads first 'line2', which is actually the first json object
            tweet= dataDict['text']#Do the same thing for the tweets
            ##try: print tweet
            ##except: pass
            tweet_list.append(tweet)
                
    return tweet_list

def approxSentiment(tweet, scoreDict):
    '''This fxn takes a tweet, converts it to a string, then
    splits it into a list of terms. We then use the AFINN-111 
    sentiment dictionary to assign scores to all the terms. If there's a match, 
    it assigns that match score. If it's not a match, it assigns the average of matched terms
    in the tweet (if any exist). If no matches exist in the tweet, non-matches will be
    assigned a 0.'''
    #Initialize score for 
    
    split_tweet= tweet.encode('utf-8').split()
    
    #Now we'll find any matches and append their scores to a 'matches' list
    matches= [scoreDict[item] for item in split_tweet if item in scoreDict.keys()]
    
    
    for i in range(0,len(split_tweet)):
        #print 'Term: ', split_tweet[i], ', In dict?: ', split_tweet[i] in scoreDict.keys()
        if split_tweet[i] in scoreDict.keys():
            print split_tweet[i], scoreDict[split_tweet[i]]
            
        else:
            if len(matches) > 0:
                print split_tweet[i], float(sum(matches))/len(matches)
            else: print split_tweet[i], 0
   
def main():
    
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])#Open twitterstream file
    
    #Create dictionary for sentiment
    afinnfile = sent_file
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #==Reading files and cleaning them==
    text = tweet_text(tweet_file)#Generate list of tweets
    
    #Clean up lists to format items and remove items with 'None' objects
    cleanTweet= [text[i] for i in range(0,len(text[0])) if text[0][i] is not None]
    
    #==Now we'll take the contents of the cleaned tweets and score them==
    #Iterate through list of clean tweets, printing out each term and its approximate sentiment
    for i in range(0,len(cleanTweet)):
        tweet_sent= approxSentiment(cleanTweet[i],scores)

if __name__ == '__main__':
    main()
