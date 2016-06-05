# ## Loading state sentiment scores

import json
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

stateScoreFile= sys.argv[1]
mapfile= sys.argv[2]

stateScores= json.load(open(stateScoreFile))

#Load raw data into dataframe
df= pd.DataFrame.from_dict(stateScores, orient= 'index')

df2= df.transpose()
df2.head(3)


# In order to visualize the data on a map easily, we'll drop the non-continental states and territories. First we'll drop them from the map coordinates from bokeh, and then from the dataframe df2.


#First delete/exclude from the bokeh coordinate dictionary and sort them alphabetically
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.us_states import data as states

del states["HI"]
del states["AK"]

EXCLUDED = ("ak", "hi", "pr", "gu", "vi", "mp", "as")#Exclude territories

import collections#This will allow us to order our states to match coordinates of coord library with data

ordStates= collections.OrderedDict(sorted(states.items()))

#Now exclude Hawaii, Alaska, and territories from our dataframe
df3= df2.drop(['HI','AK','PR','GU','VI','MP','AS','NA'], axis= 1)#For some reason we also have a 'NA' column, drop that too


# Now we'll count the number of tweets in in each state in df3 and calculate the mean tweet score for all the columns/states/series (will ignore NaN's, but output is NaN if the list for a state was empty). 

dfCount= df3.count()
dfMean= df3.mean()

# So now we have three dataframes: df3 = filtered data, dfCount = tweet count for each state in df3, dfMean= mean tweet score for each state in df3.  We'll use these to build our map and <strong>scale and normalize our tweet sentiment score data</strong>.
# Since some of our values are negative, we'll account for that as well.


#First I'll convert this to a dictionary to play with just the values and order the dictionary to match ordStates
dfMeanDict= dfMean.to_dict()
ordMeanDict= collections.OrderedDict(sorted(dfMeanDict.items()))

#I'll also turn the item values into lists to make it easy to normalize scores
ordScoreKey= ordMeanDict.keys()
ordMeanScore= ordMeanDict.values()

#Now we'll calculate the min scores to help us normalize the data
minScore= min(ordMeanScore)

normScores= ordMeanScore 

#Get weight after converting count dictionary and sorting based on key, then taking values like we did with scores
weights= dfCount.to_dict()#Convert to dict
orderedCounts= collections.OrderedDict(sorted(weights.items())).values()#Sort dict by key, take values list
weights= np.float64(orderedCounts)/max(orderedCounts)#Normalize weight by max value


# Great. Now we have a sorted dictionary for our state coordinates (ordStates), a list of normalized tweetscores whose values match the order of the dictionary (normScores), and a list of corresponding weights for said scores (weights). We can now visualize the data! 

#Here, we'll split the coordinates of all the states into x,y lists and initialize our figure object
state_xs = [ordStates[code]["lons"] for code in ordStates]
state_ys = [ordStates[code]["lats"] for code in ordStates]


# Now we'll generate a list of colors that we'll use to represent tweet score values. We'll use the cmap object to return a RGBA value depending on what value from 0 to 1 we feed it from our normalized tweet score list. 

import matplotlib

#Below we'll set the range for the colormap that we use. Although min and max values for sentiments are -5, and +5, it'll be much easier to visualize changes if we narrow the working range, say to -1.5:1.5
norm = matplotlib.colors.Normalize(vmin=-1.5, vmax=1.5)
cmap= matplotlib.cm.get_cmap('bwr')#Initialize cmap object


colorScore= []#Initialize list
for i in range(0,len(normScores)):
    if np.isnan(normScores[i]):#If the normScores value is nan (no tweets), return white (not in 'viridis' colormap)
        colorScore.append('#000000')
        
    else:
        colorScore.append(matplotlib.colors.rgb2hex(cmap(norm(normScores[i]))[:3]))


# Not all the states have the same number of tweets, thus we'll need to represent this in our map. The alpha transparency property will be a good way to scale the color intensity of each state based on the weights we calculated for each state. The more transparent the color, the fewer tweets it generated.

# In[475]:

from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool

#We'll now make the source for the info on our hover
source= ColumnDataSource(data= dict(stateKey=ordScoreKey, counts=orderedCounts, score=ordMeanScore))

hover= HoverTool(tooltips= [("State", "@stateKey"), ("Avg Tweet Score", "@score"), ("# of Tweets", "@counts")])

p = figure(title="Twitter Sentiment Score ", tools=[hover, 'wheel_zoom', 'pan', 'reset'], toolbar_location="left",
           plot_width=1100, plot_height=700)

#Plot map and use color list to assign colors
p.patches(state_xs, state_ys, line_color= 'black', color= colorScore, source= source)#, fill_alpha= alphaWeights)
#This part here is the tricky part ,we must take the order listed by states and match it with our score/weight order

output_file(mapfile, title="choropleth.py example")
show(p)


