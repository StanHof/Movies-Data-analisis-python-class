import pandas as pd
import numpy as np
from datetime import datetime

from pandas import Series, DataFrame


def filterBadMovies(df: pd.DataFrame) -> pd.DataFrame:
    badMovies = df[(df['IMDb Rating'] + df['MovieLens Rating']*2) / 2 < 5]
    return badMovies

def sortByAvgRating(df: pd.DataFrame , ascending: bool) -> pd.DataFrame:
    return df.sort_values(by='IMDb Rating', key=df['MovieLens Rating'].add, ascending=ascending)

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

def filterByYear(df: pd.DataFrame, year: int , newer: bool) -> pd.DataFrame:
    if newer: return df[df['Release Date'].dt.year >= year]
    else: return df[df['Release Date'].dt.year <= year]

def profitByGenre(df: pd.DataFrame) -> DataFrame:
    genres = df['Genre'].unique()
    x = {"Genre": genres, "Gross": [] }
    pbg = pd.Series(index=genres)
    for genre in genres:
        tmp = df[df['Genre'] == genre]
        print(f"{tmp["Adjusted Gross ($mill)"].size} , {genre}")
        pbg[genre] =  tmp["Adjusted Gross ($mill)"].mean()
    pbg.sort_index(inplace=True)
    return pbg