from conversions import *
def plotSeasonGenre(df: pd.DataFrame):
    others = [0 , 0 , 0 ,0]
    def addRow(row, seasons, others):
        i = 0
        for season in seasons:
            if len(season[season["Genre"] == row.name].index) >= 10:
                row.iloc[i] = len(season[season["Genre"] == row.name].index)
            else:
                others[i] += len(season[season["Genre"] == row.name].index)
            i += 1




    winter = df[df["Season"] == 1]
    spring = df[df["Season"] == 2]
    summer = df[df["Season"] == 3]
    fall = df[df["Season"] == 4]

    seasons = [winter, spring, summer, fall]

    seasonDF = pd.DataFrame(index = df["Genre"].unique() , columns = ["Winter", "Spring", "Summer", "Fall"])
    seasonDF.apply(lambda x : addRow(x , seasons, others), axis = 1)

    seasonDF.loc["others"] = others
    print(seasonDF)
    return seasonDF