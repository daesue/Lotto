import random
import sqlite3
import time
import sys
import os
import getopt
import mysql.connector 
from mysql.connector import Error
import pathlib
import datetime

#from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg

import Configuration as Conf

import MenuFile as mFile
import MenuHelp as mHelp
import MenuDatabase as mDatabase
import MenuSetting as mSetting

import LottoDatabase as database

class Cnf :
	def __init__(self):
		pass


class Version :
	ver = "0.1"
	ver_cui = "0.1.4.1"
	ver_gui = "0.1.4.5.1"

	def __init__(self):
		pass

	def getVersion(self, mode):
		if mode == "cui" :
			return self.ver_cui
		elif mode == "gui":
			return self.ver_gui
		elif mode == "release":
			return self.ver
		else :
			print("The mode is defferent.")
			return -1

	def infoVersion(self, mode):
		if mode == "cui" :
			print("Lotto CUI Version : ", ver_cui)
		elif mode == "gui":
			print("Lotto GUI Version : ", ver_gui)
		elif mode == "release":
			print("Lotto release Version : ", ver)
		else :
			print("The mode is defferent.")

class Lotto(Version) :

	cnt = 0
	lottoNumberRandom = []
	lottoNumberSort = []

	def __init__(self):
		conf = Conf.Configuration()
		Version.__init__(self)
#		Configuration.__init__(self)


	def randomOneNumber(self):
		extractNum = random.randrange(1, 46, 1)
		return extractNum

	def extract(self):
		self.lottoNumberRandom.clear()
		for  x in range(0, 6): 
			tmp = self.randomOneNumber()
			onlyOne = self.overlap(tmp)
			self.lottoNumberRandom.append(onlyOne)
		lottoNumSort = sorted(self.lottoNumberRandom)
		return lottoNumSort

	def extractCount(self, count):
		lotto = []
		lottoGroup = []
		if count == lottoGroup :
			return None
		for x in range (0, count):
			lotto = self.extract()
			lottoGroup.append(lotto)
		return lottoGroup

	def extract2(self):
		self.lottoNumberSort = sorted(random.sample(range(1, 46), 6))
		return self.lottoNumberSort

	def overlap(self, comparison):
		for one in self.lottoNumberRandom:
			if comparison == one :
				deduplication = self.overlap(self.randomOneNumber())
				return deduplication
		return comparison

class Lotto_CUI(Lotto) :
	def __init__(self):
		Lotto.__init__(self)
		print("Lotto CUI mode : ", self.getVersion("cui") )

	def run(self):
		lotto = []
		lottos = []
		print("cui running")
		#lotto = self.extract()
		#print(lotto)
		#Lotto.extract(self)
		#print(self.lottoNumberSort)

		lottos = self.extractCount(5)
		for x in lottos:
			print(x)

class Lotto_GUI(Lotto) :
	def __init__(self):
		Lotto.__init__(self)

		db = database.LottoDatabase(2)

		print("Lotto GUI mode : ", self.getVersion("gui") )

	def run(self):
		lotto = []
		lottos = []
		print("gui running")

		now = datetime.datetime.now()
		print("now : ", now)
		print("now date and time : " + str(now))
		print("now year : " + str(now.year))
		print("now month : " + str(now.month))
		print("now day : " + str(now.day))
		print("now hour : " + str(now.hour))
		print("now min : " + str(now.minute))
		print("now second : " + str(now.second))
		print("now date : {}-{}-{}".format(now.year, now.month, now.day))

		tomorrow = now + datetime.timedelta(days=1)
		print("tomorrow : ", tomorrow)

		win = tk.Tk()
		self.init(win)
		self.menu(win)
		self.base(win)
		win.mainloop()

	def init(self, win):
		self.win = win
		win.title("Lotto v" + self.getVersion("gui"))
#		img = tk.Image("photo", file="res/lotto.png")
#		win.tk.call('wm','iconphoto',win._w, img)
		win.geometry("800x480")

	def menu(self, win):
		MenuTitle = tk.Menu(win)
		win.config(menu = MenuTitle)

		menu_file = mFile.MenuFile(MenuTitle, win)
		menu_database = mDatabase.MenuDatabase(MenuTitle, win)
		menu_setting = mSetting.MenuSetting(MenuTitle, win)
		menu_help = mHelp.MenuHelp(MenuTitle, win)

	def base(self, win):

		styleFrmExtract = ttk.Style()
		styleFrmExtract.configure('Subject.TLabelframe.Label', font=('맑은 고딕', 14, 'bold'))

		lbFrmExtract = ttk.LabelFrame(win, text="Extract", style="Subject.TLabelframe")
		lbFrmExtract.grid(row=0, column=0, padx=5, pady=1, sticky='w')
		lbFrmLottery = ttk.LabelFrame(win, text="Lottery Day", style="Subject.TLabelframe")
		lbFrmLottery.grid(row=0, column=1, padx=10, pady=1, sticky='w')
		lbFrmInfo = ttk.LabelFrame(win, text="Info", style="Subject.TLabelframe")
		lbFrmInfo.grid(row=1, column=0, padx=5, pady=1, sticky='w')

		self.baseFrmExtract(lbFrmExtract)
		self.baseFrmLottoery(lbFrmLottery)
		self.baseFrmInfo(lbFrmInfo)

	def baseFrmExtract(self, winFrm):
		self.listExtract = tk.Listbox(winFrm, width=60)
		self.listExtract.grid(row=3, columnspan=3, sticky="w", padx=5, pady=2)

		lbElements=ttk.Label(winFrm, text="Number of elements to group")
		lbElements.grid(row=0, column=0, padx=2, pady=12,  sticky='w')

		lbEleRange=ttk.Label(winFrm, text="( 1 ~ 100)")
		lbEleRange.grid(row=0, column=2, padx=5, sticky='w')

		self.intElements = tk.IntVar()
		entElements=ttk.Entry(winFrm, width=5, textvariable=self.intElements)
		entElements.grid(row=0, column=1, padx=5, sticky='w')

		lbExtract=ttk.Label(winFrm, text="Number of Extraction ")
		lbExtract.grid(row=1, column=0, padx=2, sticky='w')

		self.intExtract = tk.IntVar()
		entExtract=ttk.Entry(winFrm, width=15, textvariable=self.intExtract)
		entExtract.grid(row=1, column=1, padx=5, sticky='w')

		btnExtract=ttk.Button(winFrm, text="Extract", command=self.btnClickExtract)
		btnExtract.grid(row=1, column=2, padx=10, sticky='w')

		lbView=ttk.Label(winFrm, text="")
		lbView.grid(row=2, column=1)

	def baseFrmLottoery(self, winFrm):
		lbLottoDay=ttk.Label(winFrm, text="Lottery Day")
		lbLottoDay.grid(row=0, column=0, padx=2, pady=12,  sticky='w')

	def baseFrmInfo(self, winFrm):
		lbTotal = ttk.Label(winFrm, text="Extracted Total Lotto Number")
		lbTotal.grid(row= 4, column=0, padx=2, pady=15)

		lbTotalValue = ttk.Label(winFrm, text="_")
		lbTotalValue.grid(row= 4, column=1, padx=2, pady=15)

		btnTotal = ttk.Button(winFrm, text="update", command=self.btnTotalUpdate)
		btnTotal.grid(row=4, column=2, padx=10)

		lbOverlap = ttk.Label(winFrm, text="Overlap Lotto Number")
		lbOverlap.grid(row=5, column=0, padx=2, pady=10)

		btnOverlap = ttk.Button(winFrm, text="view", command=self.btnGetOverlap)
		btnOverlap.grid(row=5, column=1, padx=10)

	def btnClickExtract(self):
		count = self.intExtract.get()

		for inc in range (0, count):
			lotto = self.extract()
			lstSize = self.listExtract.size()
			tmpView = str(inc+1) + " : " + str(lotto)
			self.listExtract.insert(0,  tmpView)
			if lstSize == 10:
				self.listExtract.delete(10,10)
			self.win.update()

	def btnTotalUpdate(self):
		print("totalUpdatet")

	def btnGetOverlap(self):
		print("getOverlapt")


def main(arg):
	try :
		if arg[1] == "cui" :
			cLotto = Lotto_CUI(None)
			cLotto.run()

		elif arg[1] == "gui" :
			gLotto = Lotto_GUI()
			gLotto.run()

		else :
			print("Wrong argument")
	except :
		pass
		#cLotto = Lotto_CUI()
		#cLotto.run()

if __name__ == '__main__':
	try :
		#print(sys.path)
		sys.path.append('c:\Lotto')
		#print(sys.path)

		if len(sys.argv) == 0:
			print("zero main")

		main(sys.argv)
	except getopt.GetoptError:
		print("ummm")


