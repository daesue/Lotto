import random
import sqlite3
import time
import sys
import getopt
import mysql.connector 
from mysql.connector import Error
import pathlib

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg

import Lotto
import LottoHelp as Help
class MenuHelp:
	def __init__(self, menu, win):
		self.win = win
		self.help = tk.Menu(menu, tearoff = 0)

		self.help.add_command(label="Help", command=self.menuClkHelp)
		self.help.add_command(label="Support", command=self.menuClkSupport)
		self.help.add_command(label="__")
		self.help.add_command(label="___")
		self.help.add_separator()
#		self.help.add_command(label="About")
		self.help.add_command(label="About", command=self.menuClkAbout)

		menu.add_cascade(label="Help", menu=self.help)

		self.help = Help.LottoHelp()

	def menuClkAbout(self):
		self.help.about()

	def menuClkSupport(self):
		self.help.support()

	def menuClkHelp(self):
		self.help.help()
