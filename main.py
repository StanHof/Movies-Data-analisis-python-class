import pandas as pd
import numpy as np
import datetime
from budgetRatings import *
from genreRating import *
from genreEarnings import *
from seasonsGenre import plotSeasonGenre

if __name__ == '__main__':
    ds = pd.read_csv('movies.csv', encoding="ISO-8859-1")
    convertToDatetime(ds)
    convertToFloat(ds)
    addSeasonColmun(ds)
    addAvgRating(ds)
    addbudgetAdjusted(ds)

    # jakie gatunki filmow najczesciej znajduja sie w top i bottom 100 ocenianych
    genreRatingPlot(ds)

    #jakie gatunki filmu radza sobie najlepiej w dana pore roku
    plotSeasonGenre(ds)

    #czy budzet filmu wplywa na oceny IMDb czy MovieLens bardziej
    budgetCategoryRating(ds)

    #jakie gatunki filmowe zarabiaja najwiecej
    genreEarnings(ds)