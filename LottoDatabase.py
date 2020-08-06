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

class LottoDatabase:
	def __init__(self, selectDatabase):
		print("Lotto Database : ", selectDatabase)

	def view(self):
		print("Lotto Database view")


