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

class MenuDatabase:
	def __init__(self, menu, win):
		self.win = win
		self.radVarSelected = tk.IntVar(self.win)
		self.radVarSelected.set(2)

		self.database = tk.Menu(menu, tearoff = 0)
		self.SelectedDB = tk.Menu(menu, tearoff=0)

		self.database.add_command(label="_")
		self.database.add_command(label="__")
		self.database.add_command(label="___")

		self.SelectedDB.add_radiobutton(label="MySQL", variable=self.radVarSelected, value=1, command=self.selectDatabase)
		self.SelectedDB.add_radiobutton(label="SQLite3", variable=self.radVarSelected, value=2, command=self.selectDatabase)
		self.database.add_cascade(label="Select", menu=self.SelectedDB)

		menu.add_cascade(label="Database", menu=self.database)


	def selectDatabase(self):
		dbVar = self.radVarSelected.get()
		if dbVar == 1:
			print("selected MySQL")
		elif dbVar == 2:
			print("selected SQLite3")
		else : print("Error : Wrong?" )


#		self.radioDBVar = tk.IntVar(win)
#		self.radioDBVar.set(2)

#		menu_db = tk.Menu(MenuTitle, tearoff=0)
#		menu_dbKind = tk.Menu(MenuTitle, tearoff=0)

#		menu_dbKind.add_radiobutton(label="MySQL", variable=self.radioDBVar, value=1, command=self.selectDatabase)
#		menu_dbKind.add_radiobutton(label="SQLite3", variable=self.radioDBVar, value=2, command=self.selectDatabase)

#		MenuTitle.add_cascade(label="Database", menu=menu_db)
#		menu_db.add_cascade(label="Select", menu=menu_dbKind)

#import LottoDatabase as database
#import LottoHelp as Help
#		db = database.LottoDatabase(2)
		#db.view()


