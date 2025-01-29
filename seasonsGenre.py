from conversions import *
def plotSeasonGenre(df: pd.DataFrame):
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