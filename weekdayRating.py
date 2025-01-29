import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from numba.cuda.libdevice import ceilf
from pandas import DataFrame
import math

def filterBadMovies(df: pd.DataFrame) -> pd.DataFrame:
    badMovies = df[(df['IMDb Rating'] + df['MovieLens Rating']*2) / 2 < 5]
    return badMovies

def sortByAvgRating(df: pd.DataFrame , ascending: bool):
    df.sort_values(by='IMDb Rating', key=df['MovieLens Rating'].add, ascending=ascending , inplace=True)
    return

def getMovieWeekday(mov: pd.core.series.Series):
    return datetime.strptime(mov.loc['Release Date'] , '%d/%m/%Y').weekday()

def filterByGenre(df: pd.DataFrame, genre: str) -> pd.DataFrame:
    return df[df['Genre'] == genre]

def convertToDatetime(df: pd.DataFrame):
    df['Release Date'] = df['Release Date'].apply(lambda x: datetime.strptime(x, '%d/%m/%Y'))
    return df

def convertToFloat(df: pd.DataFrame):
    df['Adjusted Gross ($mill)'] = df['Adjusted Gross ($mill)'].str.replace(',', '')
    df['Adjusted Gross ($mill)'] = df['Adjusted Gross ($mill)'].apply(lambda x: float(x))
    df["Gross ($mill)"] = df["Gross ($mill)"].str.replace(',', '')
    df["Gross ($mill)"] = df["Gross ($mill)"].apply(lambda x: float(x))
    return

def filterByYear(df: pd.DataFrame, year: int , newer: bool) -> pd.DataFrame:
    if newer:
        return df[df['Release Date'].dt.year >= year]
    else:
        return df[df['Release Date'].dt.year <= year]

def avergesByGenre(df: pd.DataFrame) -> DataFrame:
    genres = df['Genre'].unique()
    pbg = pd.DataFrame(columns=["Genre" , "No. of Movies" , "Avg. Gross", "Avg. Rating"])
    for genre in genres:
        tmp = df[df['Genre'] == genre]
        pbg.loc[len(pbg)] = [genre , len(tmp.index) , tmp["Adjusted Gross ($mill)"].mean(), (tmp["IMDb Rating"].mean()
        + tmp["MovieLens Rating"].mean() * 2) / 2 ]
    pbg.sort_values("No. of Movies", ascending=False, inplace=True)
    return pbg

def plotDataframe(df: pd.DataFrame):
    sortByAvgRating(df, ascending=True)
    bottomMovies = df.head(100)
    topMovies = df.tail(100)
    genres = np.intersect1d(topMovies['Genre'], bottomMovies['Genre'])
    pbg = pd.DataFrame(columns=["Genre" , "Nr. of bad movies" , "Nr. of good movies" , "Avg. bad rating", "Avg. good rating"])
    for genre in genres:
        botRow = bottomMovies[bottomMovies['Genre'] == genre]
        topRow = topMovies[topMovies['Genre'] == genre]
        botNr = len(botRow.index)
        topNr = len(topRow.index)
        avgBotRtg =  (botRow["IMDb Rating"].mean() + botRow["MovieLens Rating"].mean() * 2) / 2
        avgTopRtg =  (topRow["IMDb Rating"].mean() + topRow["MovieLens Rating"].mean() * 2) / 2
        pbg.loc[len(pbg)] = [genre , botNr, topNr, avgBotRtg, avgTopRtg]
    pbg.set_index('Genre', inplace=True)
    pbg.sort_values(["Nr. of bad movies"] + ["Nr. of good movies"], inplace=True)
    return pbg
def plotAverages(df: pd.DataFrame):

    df[["Nr. of bad movies" , "Nr. of good movies"]].plot(kind='bar' , figsize=(16,9))
    plt.show()
def addSeasonColmun(df: pd.DataFrame):
    def addSeason(row: pd.DataFrame) -> int:
        if row["Release Date"].month == 12:
            return 1
        else:
            return math.ceil((row["Release Date"].month / 2.75))
    df["Season"] = df.apply(addSeason , axis = 1)

def plotSeason(df: pd.DataFrame):
    def addRow(row, seasons):
        i = 0
        for season in seasons:
            row.iloc[i] = len(season[season["Genre"] == row.name].index)
            i += 1
    winter = df[df["Season"] == 1]
    spring = df[df["Season"] == 2]
    summer = df[df["Season"] == 3]
    fall = df[df["Season"] == 4]
    seasons = [winter, spring, summer, fall]
    seasonDF = pd.DataFrame(index = df["Genre"].unique() , columns = ["Winter", "Spring", "Summer", "Fall"])
    seasonDF.apply(lambda x : addRow(x , seasons), axis = 1)
    print(seasonDF)
    seasonDF.plot.pie(subplots = True , figsize=(16,9), legend = False , autopct= '%1.2f%%')
    plt.show()
def addAvgRating(df: pd.DataFrame):
    df["Avg Rating"] = df.apply(lambda x : (x["IMDb Rating"] + x["MovieLens Rating"]*2) / 2, axis = 1)
    df["MovieLens Rating"] = df.apply(lambda x : x["MovieLens Rating"]*2, axis = 1)

def addbudgetAdjusted(df : pd.DataFrame):
    df["Budget Adjusted"] = df.apply(lambda x : (x["Adjusted Gross ($mill)"] / x["Gross ($mill)"]) * x["Budget ($mill)"], axis = 1)
    df["Budget Cat"] = df.apply(lambda x : int(x["Budget Adjusted"] / 30) , axis = 1)

def budgetCategory(df : pd.DataFrame):
    df.sort_values("Budget Cat", ascending = False, inplace = True)
    budgetDf = pd.DataFrame(index=df["Budget Cat"].unique() , columns =  ["Budget", "IMDb Ratings Avg", "MovieLens Ratings Avg"] )
    budgetDf.sort_index(inplace = True)
    for i in range(10):
        tmp = df[df["Budget Cat"] == i]
        IMDb = tmp["IMDb Rating"].mean()
        MovieLens = tmp["MovieLens Rating"].mean()
        budgetDf.iloc[i] = [f"{i*30} - {(i+1)*30} mill" , IMDb, MovieLens]
    print(budgetDf)
    budgetDf.plot()
    plt.show()


