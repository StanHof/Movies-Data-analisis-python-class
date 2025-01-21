import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from pandas import DataFrame


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