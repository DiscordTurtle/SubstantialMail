from pygame import mixer

def init():
	mixer.init()
	mixer.music.load('/home/pi/mailbox/sound.mp3')
	mixer.music.set_volume(1)

def play_effect():
	mixer.music.play()