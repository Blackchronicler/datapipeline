import tkinter as tk
from tkinter import *
from src.main import calc_propotion
from src.main.connect_to_db import ConnectToDatabase
from src.main.query_data import QueryData as QD

conn = ConnectToDatabase._connecting_to_db()
cur = conn.cursor()

# incase second window require, code here

colors = ["#ccabbd", "#615EBD", "#8acfc2", "#EFBE7D", "#9AA349", "#a8c7f2"]
lang_color = []


def prop(n):
    return 360 * n / 1000


def pieChart(canvas, color, n_start, n_extent):
    canvas.create_arc((2, 2, 200, 200), fill=color, outline=color, start=prop(n_start), extent=prop(n_extent))


def writeArc(org, f):
    # langs_bytes_list
    c = tk.Canvas(f, width=400, height=400)
    langs_bytes_list = QD().get_langs_bytes(org)
    total_bytes = QD().get_total_bytes(org)

    tk.Label(f, text=org, font=("Arial", 25)).pack()
    c.pack(side=LEFT)
    print(len(langs_bytes_list))
    index = 0
    total_proportion = 0
    for lang_bytes in langs_bytes_list[:5]:
        percentage = calc_propotion.get_proportion(langs_bytes_list, lang_bytes[0], total_bytes)
        pieChart(c, colors[index], total_proportion, percentage)
        print("color=", colors[index], "start=", total_proportion, "precentage=", percentage)
        # lang_color[index][1] = colors[index]
        # lang_color[index][0] = lang_bytes[0]
        index += 1
        total_proportion += percentage

    others_percentage = 1000 - total_proportion
    pieChart(c, colors[5], total_proportion, others_percentage)

# writeArc("facebook")
# root.mainloop()
