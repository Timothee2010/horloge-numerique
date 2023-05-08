from tkinter import *
from tkinter.ttk import *

from time import strftime

root = tk()
root.title("clock")

def time():
  string = strftime("%H:%M:%S %p")
  label.config(text=string)
  label.after(1000, time)
  label = label(root
