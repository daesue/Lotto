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

class LottoHelp:
	def __init__(self):
		print("Lotto Help")
		self.styleAbout = ttk.Style()
		self.styleAbout.configure("About.TLabel", foreground="black", background="white")

	def help(self):
		print("Lotto Help")

	def support(self):
		supportText = "pichxp@gmail.com \n 입금 계좌 : "
#		msg.messagebox.showinfo("Support", supportText)
		msg.showinfo("Support", supportText)

	def about(self):
		ver = Lotto.Version()
		aboutText = "Lottery Program v" + ver.getVersion("gui")
#		msg.messagebox.showinfo("About", aboutText)
		msg.showinfo("About", aboutText)






		#		styleAbout = ttk.Style()
		#		styleAbout.configure('Subject.TLabelframe.Label', font=('맑은 고딕', 14, 'bold'))

		#		lbFrmExtract = ttk.LabelFrame(win, text="Extract", style="Subject.TLabelframe")

		#style = ttk.Style()
		#style.configure("BW.TLabel", foreground="black", background="white")
		#
		#l1 = ttk.Label(text="Test", style="BW.TLabel")
		#l2 = ttk.Label(text="Test", style="BW.TLabel")