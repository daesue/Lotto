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


class Lotto :

	cnt = 0
	lottoNumberRandom = []
	lottoNumberSort = []

	def __init__(self, lottoNumberSort):
		#self.cnt += 1   # self.cnt == Lotto.cnt
		#print("Lotto cnt : ", self.cnt)
		pass

	def randomOneNumber(self):
		extractNum = random.randrange(1, 46, 1)
		return extractNum

	def extract(self):
		for  x in range(0, 6): 
			tmp = self.randomOneNumber()
			onlyOne = self.overlap(tmp)
			self.lottoNumberRandom.append(onlyOne)
		self.lottoNumberSort = sorted(self.lottoNumberRandom)
		lottoNumSort = sorted(self.lottoNumberRandom)
		return lottoNumSort

	def extractCount(self, count):
		print("{:d} 개의".format(count) )
		self.lottoNumberSort.clear()
		print("extractCount lotto : ", self.lottoNumberSort)

		self.extract()
		print("extractCount lotto : ", self.lottoNumberSort)

		self.lottoNumberSort.clear()
		print("extractCount lotto : ", self.lottoNumberSort)

		self.extract()
		print("extractCount lotto : ", self.lottoNumberSort)


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
	def __init__(self, lottoNumberSort):
		Lotto.__init__(self, lottoNumberSort)
		print("Lotto CUI mode")

	#def extract(self):
	#	print("cui extract")

	def run(self):
		print("cui running")
		self.extract()
		print(self.lottoNumberSort)

		Lotto.extract(self)
		print(self.lottoNumberSort)

		Lotto.lottoNumberSort.clear
		self.lottoNumberSort.clear
		Lotto.extractCount(self, 10)

class Lotto_GUI(Lotto) :
	def __init__(self):
		Lotto.__init__(self)
		print("Lotto GUI mode")

	def run(self):
		print("gui running")
		Lotto.extract(self)
		print(self.lottoNumberSort)


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
		cLotto = Lotto_CUI()
		cLotto.run()




if __name__ == '__main__':
	try :
		if len(sys.argv) == 0:
			print("zero main")

		main(sys.argv)
	except getopt.GetoptError:
		print("ummm")
		pass


