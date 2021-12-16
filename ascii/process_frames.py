import sys
import os
from moviepy.editor import *
import image
import time
import subprocess

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
	if (not(len(sys.argv) == 4)):
		print("wrong no. of arguments")
	else:
		m = sys.argv[1]
		imgdir = sys.argv[2]
		txtdir = sys.argv[3]
		if (os.path.exists(imgdir)):
			os.system("./mv_rm.sh %s".format(imgdir))
			subprocess.call(["mkdir", imgdir])
		if (os.path.exists(txtdir)):
			subprocess.call(["./mv_rm.sh", txtdir])
			subprocess.call(["mkdir", txtdir])
		extract_frames(m, imgdir)
		process_frames(imgdir, txtdir)

main()