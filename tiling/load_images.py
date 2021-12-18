import os
from PIL import Image, ImageOps
import numpy as np

SECTION_SIZE = 48


def crop_center(img):
	w, h = img.size
	min_wh = w if w < h else h
	return img.crop((0, 0, min_wh, min_wh))

def load_images(tiling_images_folder):
	imgs = []
	size = SECTION_SIZE, SECTION_SIZE

	for file in os.listdir(tiling_images_folder):
		with Image.open(tiling_images_folder + "/" + file) as im:
			if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
				continue

			im = crop_center(im)
			im.thumbnail(size)

			#adding to numpy array
			a = np.array(im)
			imgs.append(a)

	return np.array(imgs).astype(np.int8)

def load_base_image(filename):
	with Image.open(filename) as im:
		w, h = im.size
		neww = int(w / SECTION_SIZE) * SECTION_SIZE
		newh = int(h / SECTION_SIZE) * SECTION_SIZE
		im = im.resize((neww, newh))
		a = np.array(im).astype(np.int8)
	return a