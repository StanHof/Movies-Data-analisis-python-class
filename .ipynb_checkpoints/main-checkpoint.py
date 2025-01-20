import pandas as pd
import numpy as np

if __name__ == '__main__':
    ds = pd.read_csv('movies.csv')
    cor = ds.corr().abs().unstack()
    print(cor)
