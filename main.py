import pandas as pd
import numpy as np
import datetime
from weekdayRating import *
if __name__ == '__main__':
    ds = pd.read_csv('movies.csv', encoding="ISO-8859-1")
    convertToDatetime(ds)
    convertToFloat(ds)
    plotAverages(plotDataframe(ds))
    #czy gorsze filmy maja wieksza szanse na sukces w zaleznosci od gatunku
    #jakie gatunki filmu radza sobie najlepiej w dana pore roku
    #czy budzet filmu wplywa na oceny IMDb czy MovieLens bardziej
    #jakie gatunki filmowe zarabiaja najwiecej