import os
from moviepy.editor import *
import image

def get_frame_times(clip):
	lst = []
	t = 0
	end = clip.duration
	print(clip.duration)
	while t < end:
		lst.append(t)
		t += 0.125
	return lst

def extract_frames(m, imgdir):
	clip = VideoFileClip(m)
	times = get_frame_times(clip)
	for t in times:
		imgpath = os.path.join(os.getcwd(), imgdir + '\\{}.jpg'.format(t))
		print(imgpath)
		clip.save_frame(imgpath, t)

def process_frames(imgdir, txtdir):
	count = 0
	for fnm in os.listdir(imgdir):
		strcnt = str(count)
		fnm = os.path.join(os.getcwd(), imgdir + "\\" + fnm)
		txtnm = os.path.join(os.getcwd(), txtdir + "\\" + strcnt + ".txt")
		f = open(txtnm, "w+")
		f.close()
		image.image_print(fnm, txtnm)
		count += 1


