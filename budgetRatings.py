from conversions import *
import pandas as pd
import matplotlib.pyplot as plt

def budgetCategoryRating(df : pd.DataFrame):
    df.sort_values("Budget Cat", ascending = False, inplace = True)
    budgetDf = pd.DataFrame(index=df["Budget Cat"].unique() , columns =  ["Budget", "IMDb Ratings Avg", "MovieLens Ratings Avg"] )
    budgetDf.sort_index(inplace = True)
    for i in range(10):
        tmp = df[df["Budget Cat"] == i]
        IMDb = tmp["IMDb Rating"].mean()
        MovieLens = tmp["MovieLens Rating"].mean()
        budgetDf.iloc[i] = [f"{i*30} - {(i+1)*30} mill" , IMDb, MovieLens]
    print(budgetDf)
    budgetDf.index = budgetDf["Budget"]
    return budgetDf


