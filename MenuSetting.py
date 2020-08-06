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

class MenuSetting:
	def __init__(self, menu, win):
		self.win = win
		self.setting = tk.Menu(menu, tearoff = 0)

		self.setting.add_command(label="_")
		self.setting.add_command(label="__")
		self.setting.add_command(label="___")
		self.setting.add_command(label="setting")

		menu.add_cascade(label="Setting", menu=self.setting)

