import subprocess
# import threading
# import requests
# import os
# import json
# import api

class Mpg123():
	def __init__(self):
		self.mpg123 = subprocess.Popen('mpg123 -R',
									   stdin=subprocess.PIPE,
									   stdout=subprocess.PIPE,
									   shell=True)
									   # stderr=subprocess.PIPE,
		# self.urls = ['msg.mp3', '2-17. only my railgun.mp3']
		# self.s = requests.session()
		# self.headers = self.s.headers
		# self.headers['Referer'] = 'http://music.163.com/search/'
		# self.cookies = open(os.path.expanduser('~') + '/.netease-musicbox/cookie').read()
		# self.cookies = json.loads(self.cookies)
		
		# t = threading.Thread(target=self.load)
		# t.setDaemon(True)
		# t.start()


	def load(self, url):
		# for url in self.urls:
		# for music in api.musiclist(self.cookies):
		# 	print(music['name'])
		self.mpg123.stdin.write('L {}\n'.format(url).encode())
		self.mpg123.stdin.flush()
		# 	while self.mpg123.poll() == None:
		# 		text = self.mpg123.stdout.readline()
		# 		try:
		# 			text = text.decode()
		# 			if '@P 0' in text:
		# 				break
		# 		except UnicodeDecodeError:
		# 			pass						

	def pause(self):
		self.mpg123.stdin.write('P\n'.encode())
		self.mpg123.stdin.flush()

