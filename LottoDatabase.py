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

conf_fileName = 'set.conf'
conf_dir = 'conf/'
conf_file = conf_dir + conf_fileName


class LottoDatabase:

	def __init__(self):
		print("Lotto Database : ")
		readFile = open(conf_file, mode='rt', encoding='utf-8')
		self.readDB = readFile.read()
		print("Read file : ", self.readDB)
		readFile.seek(0)
		readFile.close()

	def view(self):
		pass

	def getDBValue(self):
		return self.readDB


