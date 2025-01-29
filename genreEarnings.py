from conversions import *
def genreEarnings(df : pd.DataFrame):

    genres = df["Genre"].unique()
    earnings = pd.DataFrame(index= genres,columns=[ "Avg. Gross ($mill)"])
    for genre in genres:
        if len(df[df["Genre"] == genre].index) > 10:
            earnings.loc[genre] = df[df["Genre"] == genre]["Adjusted Gross ($mill)"].mean()
    earnings.sort_values(["Avg. Gross ($mill)"] , inplace= True)
    return earnings