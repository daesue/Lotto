import sys
import os

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg


conf_fileName = 'set.conf'
conf_dir = 'conf/'
conf_file = conf_dir + conf_fileName

class Configuration :

	def __init__(self):

		# 여기서 sub를 만들지 않으면
		# info 창 종료 후 새로 생성되는 win 과 충돌하는지
		# 새로운 윈도우가 생성되지 않는다.
		# 그래서 이를 구분해 주어야 한다.
		sub = tk.Tk()

		try:
			# Check conf directory
			if not os.path.exists(conf_dir):
				msg_str = conf_dir + " directory does not exist. \nSo it creates the " + conf_dir + "directory.\n" 
				print(msg_str)

				
				msg.showinfo("Alert", msg_str)
				
				os.makedirs(os.path.join(conf_dir))

				if os.path.isdir(conf_dir):

					# search file
					if os.path.isfile(conf_file):
						print("The basics have been configured.")
						readFile = open(conf_file, mode='rt', encoding='utf-8')
						tmpStr = readFile.read()
						readFile.seek(0)
						readFile.close()
						if tmpStr == "" :
							self.initConfWrite()
							#baseFile = open(conf_file, mode='wt', encoding='utf-8')
							#baseFile.write('SQLite3')
							#baseFile.close()
						else :
							# file 안 내용 확인...
							pass

					else :
						file_str = "There are no files.\nSo it creates an " + conf_file +  " file. \n"
						msg.showinfo("Alert", file_str)
						print(file_str)

						createFile = open(conf_file, 'w', encoding='utf-8')
						createFile.close()

						# check create file
						if os.path.isfile(conf_file):
							print("input base text : SQLite3")
							self.initConfWrite()
							#baseFile = open(conf_file, mode='wt', encoding='utf-8')
							#baseFile.write('SQLite3')
							#baseFile.close()

							readFile = open(conf_file, mode='rt', encoding='utf-8')
							print("Read file : ", readFile.read())
							readFile.seek(0)
							readFile.close()

							print("complete ...\n\n")
						else :
							msg.showerror("Error", "The file have not be created.")

				else :
					msg.showerror("Error", "The directory have not be created.")

				sub.destroy()

				print("retry run program\n")
			else:
				print("It is directory : ", conf_dir)
				# search file
				if os.path.isfile(conf_file):
					print("The basics have been configured.")
					readFile = open(conf_file, mode='rt', encoding='utf-8')
					tmpStr = readFile.read()
					readFile.seek(0)
					readFile.close()
					if tmpStr == "" :
						self.initConfWrite()
						#baseFile = open(conf_file, mode='wt', encoding='utf-8')
						#baseFile.write('SQLite3')
						#baseFile.close()
					else :
						pass

				else :
					file_str = "There are no files.\nSo it creates an " + conf_file +  " file. \n"
					msg.showinfo("Alert", file_str)
					print(file_str)

					createFile = open(conf_file, 'w', encoding='utf-8')
					createFile.close()

					# check create file
					if os.path.isfile(conf_file):
						print("input base text : SQLite3")
						self.initConfWrite()
						#baseFile = open(conf_file, mode='wt', encoding='utf-8')
						#baseFile.write('SQLite3')
						#baseFile.close()

						readFile = open(conf_file, mode='rt', encoding='utf-8')
						print("Read file : ", readFile.read())
						readFile.seek(0)
						readFile.close()

						print("complete ...\n\n")
					else :
						msg.showerror("Error", "The file have not be created.")

				print("##################################")
				sub.destroy()

		except OSError:
			print("Error : creating directory.")

	def isConfFile(self):
		pass

	def initConfWrite(self):
		baseFile = open(conf_file, mode='wt', encoding='utf-8')
		baseFile.write('SQLite3')
		baseFile.close()
