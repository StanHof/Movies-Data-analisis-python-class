from conversions import *

def genreRatingPlot(df: pd.DataFrame):
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