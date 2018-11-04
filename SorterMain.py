#!/usr/bin/env python3

__author__ = "Taha Jalili"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "tahajalili@gmail.com"

import os
from pyfiglet import Figlet
import inquirer

class Sorter(object):
	

	def __init__(self):
		self.path = os.getcwd()
		self.dirs = os.listdir(self.path)
		self.all_dirs = list()
		self.all_items = list()
		self.movies = list()
		self.address = list()
		self.condition = None
		self.file_types = {
		'video' : ['.mp4','.mkv','.avi','.flv','.mov'],
		'audio' : ['.mp3','.m4a']
		}

	def header(self):
		f = Figlet(font="small")
		print(f.renderText('Taha Search App'))

	def user_input(self):
		questions = [
		inquirer.List(
				'type',
				message = 'Which type do you want to look after?',
				choices=['Video','Audio']
			),
		]
		answers = inquirer.prompt(questions)
		if answers['type'] == 'Video':
			self.condition = self.file_types['video']
		elif answers['type'] == 'Audio':
			self.condition = self.file_types['audio']

	def find(self):
		for item in self.dirs:
			if os.path.splitext(os.path.join(self.path,item))[1] in self.condition:
				self.movies.append(item)
				self.address.append(os.path.join(self.path+'/',item))
			else:
				self.all_dirs.append(item)
		for d in self.all_dirs:
			try:
				if os.path.isdir(os.path.join(self.path,d)):
					for i in os.listdir(os.path.join(self.path,d)):
						if os.path.splitext(os.path.join(self.path+d,i))[1] in self.condition:
							self.movies.append(i)
							self.address.append(os.path.join(self.path+'/'+d,i))
			except Exception:
				pass

	def show(self):
		for i in range(len(self.movies)):
			print('\n'+self.movies[i],self.address[i])

	def continue_proccess(self):
		questions = [
			inquirer.Confirm('continue',
					message="Do you wish to continue?"
				),
		]
		answers = inquirer.prompt(questions)
		if answers['continue'] == True:
			return 1
		elif answers['continue'] == False:
			return 0

def main():
	s = Sorter()
	s.user_input()
	s.find()
	s.show()
	a = s.continue_proccess()
	if a == 1:
		main()
	elif a == 0:
		print("==> Bye <==")

	


if __name__ == '__main__':
	s = Sorter()
	s.header()
	main()
