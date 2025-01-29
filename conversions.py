import numpy as np
import pandas as pd
from datetime import datetime
import math
import matplotlib.pyplot as plt
def filterBadMovies(df: pd.DataFrame) -> pd.DataFrame:
    badMovies = df[(df['IMDb Rating'] + df['MovieLens Rating']*2) / 2 < 5]
    return badMovies

def sortByAvgRating(df: pd.DataFrame , ascending: bool):
    df.sort_values(by='IMDb Rating', key=df['MovieLens Rating'].add, ascending=ascending , inplace=True)
    return

def getMovieWeekday(mov: pd.core.series.Series):
    return datetime.strptime(mov.loc['Release Date'] , '%d/%m/%Y').weekday()

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

def addSeasonColmun(df: pd.DataFrame):
    def addSeason(row: pd.DataFrame) -> int:
        if row["Release Date"].month == 12:
            return 1
        else:
            return math.ceil((row["Release Date"].month / 2.75))
    df["Season"] = df.apply(addSeason , axis = 1)

def addAvgRating(df: pd.DataFrame):
    df["Avg Rating"] = df.apply(lambda x : (x["IMDb Rating"] + x["MovieLens Rating"]*2) / 2, axis = 1)
    df["MovieLens Rating"] = df.apply(lambda x : x["MovieLens Rating"]*2, axis = 1)

def addbudgetAdjusted(df : pd.DataFrame):
    df["Budget Adjusted"] = df.apply(lambda x : (x["Adjusted Gross ($mill)"] / x["Gross ($mill)"]) * x["Budget ($mill)"], axis = 1)
    df["Budget Cat"] = df.apply(lambda x : int(x["Budget Adjusted"] / 30) , axis = 1)