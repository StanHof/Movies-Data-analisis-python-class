import pandas as pd
import numpy as np
import datetime

import budgetRatings
import genreRating
from budgetRatings import *
from genreRating import *
from genreEarnings import *
from seasonsGenre import plotSeasonGenre
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



if __name__ == '__main__':
    ds = pd.read_csv('movies.csv', encoding="ISO-8859-1")
    convertToDatetime(ds)
    convertToFloat(ds)
    addSeasonColmun(ds)
    addAvgRating(ds)
    addbudgetAdjusted(ds)
    pd.set_option('future.no_silent_downcasting', True)
    # Initialize Tkinter and Matplotlib Figure
    root = tk.Tk()
    root.geometry('1920x1080')


    # Tkinter Application
    frame = tk.Frame(root)
    label = tk.Label(text="Analiza Danych")
    label.config(font=("Courier", 16))
    label.pack()
    frame.pack()
    canvas = None
    def b1():
        global canvas
        if canvas:
            canvas.get_tk_widget().destroy()
        fig, ax = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        genreRatingPlot(ds)[["Nr. of bad movies", "Nr. of good movies"]].plot(kind='bar', figsize=(16, 9), ax=ax, rot=0)
        canvas.draw()
    def b2():
        global canvas
        if canvas:
            canvas.get_tk_widget().destroy()
        fig, ax = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        genreEarnings(ds).plot(ax=ax)
    def b3():
        global canvas
        if canvas:
            canvas.get_tk_widget().destroy()
        fig, ax = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        plotSeasonGenre(ds).plot.pie(subplots = True , figsize=(16,9), legend = False , autopct= '%1.2f%%', ax=ax)
    def b4():
        global canvas
        if canvas:
            canvas.get_tk_widget().destroy()
        fig, ax = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        budgetCategoryRating(ds).plot(ax=ax)

    button1 = tk.Button(frame, text="Worst and best rated genres", command=b1)
    button1.pack()
    button2 = tk.Button(frame, text="Avg earning by genre", command=b2)
    button2.pack()
    button3 = tk.Button(frame, text="Genre Releases by seasons", command=b3)
    button3.pack()
    button4 = tk.Button(frame, text="Ratings by budget", command=b4)
    button4.pack()


    root.mainloop()
