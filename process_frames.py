import sys
import os
from moviepy.editor import *
import image
import time

def get_frame_times(clip):
	lst = []
	t = 0
	end = clip.duration
	while t < end:
		lst.append(t)
		t += 0.125
	return lst

def extract_frames(m, imgdir):
	clip = VideoFileClip(m)
	times = get_frame_times(clip)
	f = open("milo.txt", "w")
	f.write(str(len(times)))
	for t in times:
		imgpath = os.path.join(os.getcwd(), imgdir + '\\{}.jpg'.format(t))
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

def main():
	time.sleep(2)
	if (not(len(sys.argv) == 4)):
		print("wrong no. of arguments")
	else:
		m = sys.argv[1]
		imgdir = sys.argv[2]
		txtdir = sys.argv[3]
		extract_frames(m, imgdir)
		process_frames(imgdir, txtdir)

main()
exit()