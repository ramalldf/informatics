import sys
import json

#Dictionary for state abbreviations
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
#==Build AFINN-111 dictionary from sent_file
def findState(txtString):
    '''Function takes a the location string and splits into two to get the state'''
    try:
        parseStr= txtString.split(', ')
        return parseStr[1]
    except:
        pass#print 'None'
def tweet_state(tweet_file):
    '''This function will open a tweet file, split the content of each 
    tweets text into a tweet list and a location list. '''  
    tweet_index= 0#Initialize a counter to keep track of tweet we're on
    loc_list= []#Initialize lists
    tweet_list= []
    for line in tweet_file:
            tweet_index= tweet_index+1
            dataDict= json.loads(line)#Loads first 'line2', which is actually the first json object
            if "user" in dataDict.keys():#Look for 'user' field
                userField= dataDict["user"]#Dump contents into userField and location objects and append to list     
                location= userField["location"]
                loc_list.append(location)
                
                tweet= dataDict['text']#Do the same thing for the tweets
                tweet_list.append(tweet)
    return loc_list, tweet_list
def singleTweetSent(tweet,sentiment_file):
    '''This fxn takes a tweet, converts it to a string, then
    splits it into a list of terms. We then use the AFINN-111 
    sentiment dictionary, and assign scores to all the terms
    and take their sum to get a cumulative tweet sentiment score'''
    #Create dictionary for sentiment
    afinnfile = sentiment_file
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    
    tweet_score= []
    split_tweet= tweet.encode('utf-8').split()
    for i in range(0,len(split_tweet)):
        if split_tweet[i] in scores.keys():
            tweet_score.append(scores[split_tweet[i]])
        else:
            tweet_score.append(0)
    
    return sum(tweet_score)    
def main():
    
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])#Open twitterstream file
    
    #==Reading files and cleaning them==
    stateTweets = tweet_state(tweet_file)#Generate list of states and corresponding tweets
    
    #Clean up lists to format items and remove items with 'None' objects
    cleanState= [stateTweets[0][i] for i in range(0,len(stateTweets[0])) if stateTweets[0][i] is not None]
    cleanTweet= [stateTweets[1][i] for i in range(0,len(stateTweets[0])) if stateTweets[0][i] is not None]
    
    #==Now we'll take the contents of the cleaned states/tweets and score them==
    #This extracts the state location from a tweet and calculates the corresponding tweet sentiment for it
    #Point of hw is to find the average value for each state so we'll need to keep track of ALL values for all states
    #We'll initialize a state:score dictionary, we'll calculate the averages later
    stateList= []#We'll keep these for reference
    sentimentList= []
    stateScoreDict= {key: list() for key in states}#Initialize dictionary of states and scores with dict comprehension
    for i in range(0,len(cleanState)):
        state= findState(cleanState[i])#Split line into (city, state) and recover state string if available
        if state in states.keys():#Search for state abbrev. in dictionary keys list
            state= str(state.upper())
            tweet_sent= singleTweetSent(cleanTweet[i],sent_file)#Recovers tweet text
            stateList.append(state)#Appends state and tweets to respective lists
            sentimentList.append(tweet_sent)
            stateScoreDict[state].append(tweet_sent)#Append tweet sentiment score to list of scores for appropriate state
    #==Consolidate scores to average score and find max score
    #The final step is to consolidate the values of our score dictionary into a new dictionary
    #with average sentiment scores for each state (that had at least one score)
    stateScoreAvg= {key: (float(sum(stateScoreDict[key]))/len(stateScoreDict[key])) for key in stateScoreDict if len(stateScoreDict[key]) > 0}
    #Then we'll find the max score in our new dictionary
    maxVal= max(stateScoreAvg.values())#Turn values into a list, return max value in that list
    maxState= [i for i in stateScoreAvg.keys() if stateScoreAvg[i] == maxVal]#Return key with equivalent value to max value and max value
    print maxState[0]
if __name__ == '__main__':
    main()
