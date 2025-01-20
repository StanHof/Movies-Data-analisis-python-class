import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from pandas import Series, DataFrame


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
        pbg.loc[len(pbg)] = [genre , len(tmp.index) , tmp["Adjusted Gross ($mill)"].mean(), (tmp["IMDb Rating"].mean()  + tmp["MovieLens Rating"].mean() * 2) / 2 ]

    pbg.sort_values("No. of Movies", ascending=False, inplace=True)
    return pbg
def plotAverages(worst: pd.DataFrame , best: pd.DataFrame):
    worstSeries = pd.Series(worst['No. of Movies'])
    print(worstSeries)
    plt.show()