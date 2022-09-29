from cmath import pi
import piechart
import tkinter as tk
from tkinter import *

# main window
root = tk.Tk()
frame = Frame(root)
bf = Frame(root)
bf.pack(side=BOTTOM)
frame.pack()
root.title("Welcome to GithubCrawler")
#root.geometry("2000x1000")


# position = [tk.TOP, tk.RIGHT, tk.LEFT, tk.BOTTOM, tk.SW], [tk.BOTTOM, tk.S], [tk.BOTTOM, tk.SE]]


class orgPiechart:
    def create_piecharts(self):
        orgs_wanted = ["facebook", "netflix", "twitter", "adobe", "ubuntu", "OSGeo"]
        index = 0

        for org in orgs_wanted:
            if index < 3:
                piechart.writeArc(org, frame)
            else:
                piechart.writeArc(org, bf)
            # print(org, position[index][0],  position[index][1])
            index += 1


if __name__ == "__main__":
    orgPiechart().create_piecharts()
    root.mainloop()
