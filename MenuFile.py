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

class MenuFile:
	def __init__(self, menu, win):
		self.win = win
		self.file = tk.Menu(menu, tearoff = 0)

		self.file.add_command(label="New")
		self.file.add_command(label="Open")
		self.file.add_command(label="Save")
		self.file.add_command(label="Save As...")
		self.file.add_separator()
		self.file.add_command(label="Exit", command=self.quit)

		menu.add_cascade(label="File", menu=self.file)

	def quit(self):
		print("exit")
		ext = msg.askokcancel("Exit", "Realy, Exit?")  # return True, False
		if ext == True :
			print("ok")
			self.win.quit()
		elif ext == False :
			#tk.messagebox.showinfo("id")
			print("no")


#	def _quit(self):
#		print("exit")
#		ext = msg.askokcancel("Exit", "Realy, Exit?")  # return True, False
#		if ext == True :
#			print("ok")
#			self.win.quit()
#		elif ext == False :
#			#tk.messagebox.showinfo("id")
#			print("no")
#