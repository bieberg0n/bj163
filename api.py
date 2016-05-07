import hashlib
import requests,json
import base64
import pprint

s = requests.session()
headers = s.headers
headers['Referer'] = 'http://music.163.com/search/'

def like(id, iflike,cookies):
	red = 'true' if iflike else 'false'
	r = s.get('http://music.163.com/api/radio/like?alg=itembased&trackId={}&like={}&time=25'.format(id,red), headers=headers, cookies=cookies)
	print(r.text)


def musiclist(cookies):
	# headers = s.headers
	# headers['Referer'] = 'http://music.163.com/search/'
	while 1:
		r = s.get('http://music.163.com/api/radio/get',
					   headers=headers, cookies=cookies)
		d = json.loads(r.text)
		# pprint.pprint(d)
		try:
			musiclist = [ { 'name':x['name'],
							'url':geturl( str(x['hMusic']['dfsId']) ),
							'id':x['id'],
							'lrcs':getlrcs(x['id'], cookies),
							'artist':x['artists'][0]['name'],
							'album':x['album']['name'],
							'pic':x['album']['picUrl'] }
						  for x in d['data'] ]
		except TypeError:
			continue
		for music in musiclist:
			yield music


def getlrcs(id, cookies):
	headers = s.headers
	headers['Referer'] = 'http://music.163.com/search/'
	r = s.get('http://music.163.com/api/song/lyric?os=pc&id={}&lv=-1&kv=-1&tv=-1'.format(id), headers=headers, cookies=cookies )
	d = json.loads(r.text)
	lrc = d['lrc']['lyric'].split('\n') if d.get('lrc') else []
	try:
		tlrc = d['tlyric']['lyric'].split('\n') if d.get('tlyric') else []
	except AttributeError:
		tlrc = []
	lrcs = { 'lrc':lrc, 'tlrc':tlrc }
	return lrcs


def geturl(dfsid):
	eid = get_eid(dfsid)
	url = 'http://m1.music.126.net/' + eid +'/'+ dfsid + '.mp3'
	return url


def get_eid(dfsid):
	byte1     = bytearray(b'3go8&$8*3*3h0k(2)2')
	byte1_len = len(byte1)
	byte2     = bytearray(dfsid.encode())
	for i in range(len(byte2)):
		byte2[i] = byte2[i]^byte1[i%byte1_len]

	m = hashlib.md5()
	m.update(byte2)

	result = base64.b64encode(m.digest()).decode()
	result = result.replace('/', '_')
	result = result.replace('+', '-')
	return result


def get_id(song,artist):
	data = {
			'hlpretag':'<span class="s-fc7">',
			'hlposttag':'</span>',
			's':song,
			'type':'1',
			'limit':'3',
			'offset':'0',
			}
	r = s.post('http://music.163.com/api/search/suggest/web?csrf_token=',data=data,headers={'referer':'http://music.163.com/'})
	d = json.loads(r.text)

	for i in range(len(d['result']['songs'])):
		if d['result']['songs'][i]['artists'][0]['name'].encode('utf-8').lower() == artist.encode('utf-8').lower():
			return str(d['result']['songs'][i]['id'])


def wangyi(id):
	r     = s.get('http://music.163.com/api/song/detail/?id=' + id + '&ids=%5B' + id +'%5D&csrf_token=')
	d     = json.loads(r.text)
	dfsid = str(d['songs'][0]['hMusic']['dfsId'])
	eid   = get_eid(dfsid)
	url   = 'http://m1.music.126.net/' + eid +'/'+ dfsid + '.mp3'
	return url


'''
id = '7860408627359797'
eid = encrypted_id(id)
os.system('wget http://m1.music.126.net/' + eid + '/' + id + '.mp3')
'''

if __name__ == '__main__':
	song = 'An Unfinished Life'
	artist = 'Audio Machine'
	print(wangyi(get_id(song, artist)))
	#print(encrypted_id('25889578'))

