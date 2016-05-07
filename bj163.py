# import multiprocessing
import threading
import requests
import os
import json
import ui
from mpg123 import Mpg123
import api
import login_api
import getpass
# from ui import t


def login():
	username = input('帐号: ')
	password = getpass.getpass('密码: ')
	cookies = login_api.login(username, password)
	with open('cookie', 'w') as f:
		f.write(json.dumps(cookies))


def fm163():
	# global window
	# urls = ['msg.mp3','msg.mp3','msg.mp3','7-17. Beautiful World.mp3', '2-17. only my railgun.mp3']
	# dir = os.path.expanduser('~') + '/.netease-musicbox'
	s = requests.session()
	headers = s.headers
	headers['Referer'] = 'http://music.163.com/search/'
	# cookies = open(dir + '/cookie').read()
	cookies = open('cookie').read()
	cookies = json.loads(cookies)
	# for url in urls:
	for music in api.musiclist(cookies):
		print(music['name'])
		window.t = music['name']
		window.artist_ = music['artist']
		window.album_ = music['album']
		mpg123.load(music['url'])
		window.like.like_flag = False
		like_flag = False
		while 1:
			if window.next_song.next_flag:
				window.next_song.next_flag = False
				break
			elif window.like.like_flag != like_flag:
				if window.like.like_flag:
					print('like')
					api.like(music['id'], True, cookies)
				else:
					print('dislike')
					api.like(music['id'], False, cookies)
				like_flag = window.like.like_flag

			text = mpg123.mpg123.stdout.readline()
			try:
				text = text.decode()
				if '@P 0' in text:
					break
			except UnicodeDecodeError:
				pass


# if __name__ == '__main__':

# p = threading.Thread(target=fm163,args=(mpg123,window,director,))
if not os.path.exists('cookie'):
	login()

mpg123 = Mpg123()
director = ui.director
director.director.init( width=420, height=180, caption='网易云音乐' )
window = ui.Window(mpg123)
main_scene = ui.cocos.scene.Scene( window )

t = threading.Thread(target=fm163)
t.setDaemon(True)
# p = multiprocessing.Process(target=director.director.run,args=(main_scene,))
t.start()
director.director.run(main_scene)
# p.terminate()
