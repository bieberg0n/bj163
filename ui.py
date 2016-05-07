import cocos
from cocos import director
# import os
# import time
# import threading

# class Text(cocos.layer.ColorLayer):
# 	def __init__(self):
# 		super( Text, self ).__init__(0,0,0,0,width=200,height=30)
# 		label = cocos.text.Label('网易云音乐',
# 								 font_name='微软雅黑',
# 								 font_size=12)
# 		self.add(label)

# class Like(cocos.layer.ColorLayer):
# 	is_event_handler = True
# 	def __init__(self):
# 		super( Like, self ).__init__(0,0,0,0,width=40,height=40)
# 		self.like = cocos.sprite.Sprite('image/like.png')
# 		self.like.scale = 40 / self.like.height
# 		self.like.image_anchor = (20, 0)
# 		self.like.position = (0, 0)
# 		self.add(self.like)
		# self.addsprite('image/like.jpg')
		# self.addsprite('image/pic.png')

	# def addsprite(self, jpg):
	# 	self.sprite = cocos.sprite.Sprite(jpg)
	# 	print('载入',jpg)
	# 	self.sprite.scale = 160 / self.sprite.height
	# 	self.sprite.image_anchor = (0, 0)
	# 	self.sprite.position = (0, 0)
	# 	self.add(self.sprite)

	# def on_mouse_press(self, x, y, buttons, modifiers):
	# 	if (self.x-self.width//2) <= x <= (self.x+self.width//2) and\
	# 	   self.y <= y <= (self.y+self.height):
	# 		print('pic', x, y)

class Like(cocos.layer.ColorLayer):
	is_event_handler = True
	def __init__(self):
		super( Like, self ).__init__(0,0,0,0,width=40,height=40)
		# self.mpg123 = mpg123
		self.hl_flag = False
		# pause_flag 表示播放器状态,播放时显示暂停图标
		self.like_flag = False

		# self.red = cocos.sprite.Sprite('image/red.png')
		# self.red.scale = 40 / self.red.height
		# self.red.image_anchor = (20, 0)
		# self.red.position = (0, 0)
		
		# self.red_hl = cocos.sprite.Sprite('image/red_hl.png')
		# self.red_hl.scale = 40 / self.red_hl.height
		# self.red_hl.image_anchor = (20, 0)
		# self.red_hl.position = (0, 0)

		# self.like = cocos.sprite.Sprite('image/like.png')
		self.addsprite('image/like.png')
		# self.like.scale = 40 / self.like.height
		# self.like.image_anchor = (20, 0)
		# self.like.position = (0, 0)
		# self.add(self.like)

		# self.like_hl = cocos.sprite.Sprite('image/like_hl.png')
		# self.like_hl.scale = 40 / self.like_hl.height
		# self.like_hl.image_anchor = (20, 0)
		# self.like_hl.position = (0, 0)

	def addsprite(self, jpg):
		self.sprite = cocos.sprite.Sprite(jpg)
		self.sprite.scale = 40 / self.sprite.height
		self.sprite.image_anchor = (13, 0)
		self.sprite.position = (0, 0)
		self.add(self.sprite)

	def on_mouse_motion(self, x, y, dx, dy):
		if (self.x-self.width//2) <= x <= (self.x+self.width//2) and\
		   self.y <= y <= (self.y+self.height):
			if not self.hl_flag:
				if self.like_flag:
					self.remove(self.sprite)
					self.addsprite('image/red_hl.png')
					self.hl_flag = True
				else:
					self.remove(self.sprite)
					self.addsprite('image/like_hl.png')
					self.hl_flag = True
		else:
			if self.hl_flag:
				if self.like_flag:
					self.remove(self.sprite)
					self.addsprite('image/red.png')
					self.hl_flag = False
				else:
					self.remove(self.sprite)
					self.addsprite('image/like.png')
					self.hl_flag = False

	def on_mouse_press(self, x, y, buttons, modifiers):
		# print(self.x, self.y)
		if (self.x-self.width//2) <= x <= (self.x+self.width//2) and\
		   self.y <= y <= (self.y+self.height):
			# print('right')
			# print('play', x, y)
			if self.like_flag:
				self.remove(self.sprite)
				self.addsprite('image/like_hl.png')
			else:
				self.remove(self.sprite)
				self.addsprite('image/red_hl.png')

			self.like_flag = False if self.like_flag else True


class Pic(cocos.layer.ColorLayer):
	is_event_handler = True
	def __init__(self):
		super( Pic, self ).__init__(0,0,0,0,width=160,height=160)
		self.addsprite('image/source.jpg')
		# self.addsprite('image/pic.png')

	def addsprite(self, jpg):
		self.sprite = cocos.sprite.Sprite(jpg)
		print('载入',jpg)
		self.sprite.scale = 160 / self.sprite.height
		self.sprite.image_anchor = (0, 0)
		self.sprite.position = (0, 0)
		self.add(self.sprite)

	def on_mouse_press(self, x, y, buttons, modifiers):
		if self.x <= x <= (self.x+self.width) and\
		   self.y <= y <= (self.y+self.height):
			print('pic', x, y)

	# def update(self):
	# 	self.remove(self.sprite)
	# 	self.addsprite('image/pic.png')
		# self.sprite = cocos.sprite.Sprite('image/source.jpg')
		# self.sprite.scale = 160 / self.sprite.height
		# self.sprite.image_anchor = (0, 0)
		# self.sprite.position = (0, 0)
		# self.add(self.sprite)


class Play(cocos.layer.ColorLayer):
	is_event_handler = True
	def __init__(self, mpg123):
		super( Play, self ).__init__(0,0,0,0,width=40,height=40)
		self.mpg123 = mpg123
		self.hl_flag = False
		# pause_flag 表示播放器状态,播放时显示暂停图标
		self.pause_flag = False

		self.play = cocos.sprite.Sprite('image/play.png')
		self.play.image_anchor = (20, 0)
		self.play.position = (0, 0)
		
		self.play_hl = cocos.sprite.Sprite('image/play_hl.png')
		self.play_hl.image_anchor = (20, 0)
		self.play_hl.position = (0, 0)

		self.pause = cocos.sprite.Sprite('image/pause.png')
		self.pause.image_anchor = (20, 0)
		self.pause.position = (0, 1)
		self.add(self.pause)

		self.pause_hl = cocos.sprite.Sprite('image/pause_hl.png')
		self.pause_hl.image_anchor = (20, 0)
		self.pause_hl.position = (0, 1)

	def on_mouse_motion(self, x, y, dx, dy):
		if (self.x-self.width//2) <= x <= (self.x+self.width//2) and\
		   self.y <= y <= (self.y+self.height):
			if not self.hl_flag:
				if self.pause_flag:
					self.remove(self.play)
					self.add(self.play_hl)
					self.hl_flag = True
				else:
					self.remove(self.pause)
					self.add(self.pause_hl)
					self.hl_flag = True
		else:
			if self.hl_flag:
				if self.pause_flag:
					self.remove(self.play_hl)
					self.add(self.play)
					self.hl_flag = False
				else:
					self.remove(self.pause_hl)
					self.add(self.pause)
					self.hl_flag = False
		# else:
		# 	hl_flag = False
		# if self.hl_flag == hl_flag:
		
	def on_mouse_press(self, x, y, buttons, modifiers):
		# print(self.x, self.y)
		if (self.x-self.width//2) <= x <= (self.x+self.width//2) and\
		   self.y <= y <= (self.y+self.height):
			# print('right')
			# print('play', x, y)
			if self.pause_flag:
				self.remove(self.play_hl)
				self.add(self.pause_hl)
				self.mpg123.pause()
			else:
				self.remove(self.pause_hl)
				self.add(self.play_hl)
				self.mpg123.pause()

			self.pause_flag = False if self.pause_flag else True


class Nextsong(cocos.layer.ColorLayer):
	is_event_handler = True
	def __init__(self):
		super( Nextsong, self ).__init__(0,0,0,0,width=40,height=40)
		self.next_flag = False
		self.hl_flag = False
		
		self.nextsong = cocos.sprite.Sprite('image/next_song.png')
		self.nextsong.scale = 40 / self.nextsong.height
		self.nextsong.image_anchor = (20, 0)
		self.nextsong.position = (0, 0)
		self.add(self.nextsong)
		
		self.nextsong_hl = cocos.sprite.Sprite('image/next_song_hl.png')
		self.nextsong_hl.scale = 40 / self.nextsong_hl.height
		self.nextsong_hl.image_anchor = (20, 0)
		self.nextsong_hl.position = (0, 0)

	def on_mouse_motion(self, x, y, dx, dy):
		if (self.x-self.width//2) <= x <= (self.x+self.width//2) and\
		   self.y <= y <= (self.y+self.height):
			if not self.hl_flag:
					self.remove(self.nextsong)
					self.add(self.nextsong_hl)
					self.hl_flag = True
		else:
			if self.hl_flag:
					self.remove(self.nextsong_hl)
					self.add(self.nextsong)
					self.hl_flag = False

	def on_mouse_press(self, x, y, buttons, modifiers):
		# print(self.x, self.y)
		if (self.x-self.width//2) <= x <= (self.x+self.width//2) and\
		   self.y <= y <= (self.y+self.height):
			print('next', x, y)
			self.next_flag = True
		# 	self.mpg123.pause()
		

class Window(cocos.layer.Layer):
	is_event_handler = True
	def __init__(self, mpg123):
		super( Window, self ).__init__()

		bg = cocos.sprite.Sprite('image/bg.png')
		bg.position = (210, 90)
		bg.scale = 180 / bg.height
		self.add(bg, z=0)
		self.mpg123 = mpg123

		self.pic = Pic()
		# pic.scale = 160 / pic.height
		# pic.image_anchor = (0, 0)
		self.pic.position = (10, 10)
		self.add(self.pic)

		play = Play(mpg123)
		# play.image_anchor = (20, 0)
		play.position = (300, 10)
		self.add(play)
		
		self.next_song = Nextsong()
		# next_song.image_anchor = (20, 0)
		self.next_song.position = (360, 7)
		self.add(self.next_song)

		self.like = Like()
		self.like.position = (240, 10)
		self.add(self.like)
		
		self.text = cocos.text.Label('网易云音乐',
								 font_name='微软雅黑',
								 font_size=12)
		self.text.position = (200, 130)
		self.add(self.text)

		self.artist = cocos.text.Label('歌手:',
									 font_name='微软雅黑',
									 font_size=10)
		self.artist.position = (200, 100)
		self.add(self.artist)

		self.album = cocos.text.Label('专辑:',
									 font_name='微软雅黑',
									 font_size=10)
		self.album.position = (200, 70)
		self.add(self.album)

		self.t = '网易云音乐'
		self.artist_ = ''
		self.album_ = ''
		# self.pic_flag = False

	def update_text(self):
		if self.text.element.text != self.t:
			self.text.element.text = self.t
			self.like.remove(self.like.sprite)
			self.like.addsprite('image/like.png')
			print(self.text.element.text)
		if self.artist_ not in self.artist.element.text:
			self.artist.element.text = '歌手: ' + self.artist_
			print(self.artist.element.text)
		if self.album_ not in self.album.element.text:
			self.album.element.text = '专辑: ' + self.album_
			print(self.album.element.text)
		# if self.pic_flag:
		# 	print('pic_flag',self.pic_flag)
		# 	self.pic.update()
		# 	self.pic_flag = False
	# def on_mouse_press(self, x, y, buttons, modifiers):
		# if self.x <= x <= (self.x+self.width) and\
		#    self.y <= y <= (self.y+self.height):
		# print('pic', x, y)
		# self.update_text(t)
		# print('self.t',self.t)

	def on_mouse_motion(self, x, y, dx, dy):
		# print(x,y)
		# self.t = str(x)
		self.update_text()
		# time.sleep(1)
		

if __name__ == '__main__':
	director.director.init( width=420, height=180, caption='网易云音乐' )
	main_scene = cocos.scene.Scene( Window() )
	director.director.run(main_scene)
