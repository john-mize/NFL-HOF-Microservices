import pandas as pd
from sklearn.linear_model import LogisticRegression

# import file
# statsDF = pd.read_csv('/home/john/Documents/nfl_hof_app/wrstats.csv')
statsDF = pd.read_csv('wrstats.csv')

# drop non RBs from dataframe
statsDF = statsDF.drop(statsDF[statsDF.Pos != "WR"].index)

# count how many excess RBs over 100, then drop that amount from end of list
numXtra = statsDF.shape[0] - 100
statsDF.drop(statsDF.tail(numXtra).index, inplace = True)

# drop team column
statsDF.drop(['Tm'], axis=1, inplace=True)

# reset rank to 1-100
statsDF.Rank = range(1,101)

# change Ys and Ns to 1s and 0s
statsDF['HOF'] = statsDF['HOF'].replace(['Y'], 1)
statsDF['HOF'] = statsDF['HOF'].replace(['N'], 0)
statsDF['HOF_Eligible'] = statsDF['HOF_Eligible'].replace(['Y'], 1)
statsDF['HOF_Eligible'] = statsDF['HOF_Eligible'].replace(['N'], 0)

# split data into two sets: HOF eligible and ineligible
statsDFtrain = statsDF[statsDF.HOF_Eligible == 1]
statsDFtest = statsDF[statsDF.HOF_Eligible == 0]

# Now we set up our Xtrain, ytrain, Xtest, and ytest datasets. We drop 'Rank', 'Player', 'First Year', 'Pos', 'HOF_Eligible', and 'HOF' 
# This leaves 'yds', 'last year', 'seasons', 'yds/season', 'TDs', 'rec TDs', 'Rush TDs', 'TDs/season', 'height', 'rec', 'rec/season', 'rec yds', 'rec yds/season' to train from
Xtrain = statsDFtrain.drop(['Rank', 'Player', 'First Year', 'Pos', '40 yd Dash', 'HOF_Eligible', 'HOF'], axis=1)
ytrain = statsDFtrain['HOF']

Xtest = statsDFtest.drop(['Rank', 'Player', 'First Year', 'Pos', '40 yd Dash', 'HOF_Eligible', 'HOF'], axis=1)
ytest = statsDFtest['HOF']

logistic_regression = LogisticRegression()

# Now we run our logistic regression for our datasets to predict the future HOF members
logistic_regression.fit(Xtrain, ytrain)

ypred = logistic_regression.predict(Xtest)

HOFplayers = []
HOF_predict = {}
for i in range(len(ypred)):
    if ypred[i] == 1:
        HOFplayers.append(statsDFtest.iloc[i]["Player"])

HOF_predict["Predicted HOF Wide Receivers"] = HOFplayers

playersNameDict = statsDF.set_index('Rank')['Player'].to_dict()
playerStatsDict = statsDF.to_dict('records')

playersDict = {}
for rank in playersNameDict.keys():
    playersDict[playersNameDict[rank]] = playerStatsDict[rank-1]