import numpy as np
import sys
from load_images import load_images, SECTION_SIZE, load_base_image
from PIL import Image

np.set_printoptions(threshold=sys.maxsize)

def construct_tiling(imgs, base):
	print(imgs.shape, base.shape)
	tiled_img = np.zeros(base.shape)
	baseh = base.shape[0]
	basew = base.shape[1]
	iterh = baseh // SECTION_SIZE
	iterw = basew // SECTION_SIZE
	for i in range(iterh):
		for j in range(iterw):
			tempim = base[i*SECTION_SIZE:(i+1)*SECTION_SIZE,j*SECTION_SIZE:(j+1)*SECTION_SIZE]

			diffs = np.abs(imgs - tempim).sum(axis=(1, 2, 3))
			idxs = np.argsort(diffs)[0:3]
			idx = np.random.choice(idxs)
			tiled_img[i*SECTION_SIZE:(i+1)*SECTION_SIZE,j*SECTION_SIZE:(j+1)*SECTION_SIZE] = imgs[idx]

	return tiled_img


image_to_tile = sys.argv[1]
tiling_images_folder = sys.argv[2]
i = load_images(tiling_images_folder)
b = load_base_image(image_to_tile)

c = construct_tiling(i, b)
result = Image.fromarray(np.uint8(c)).convert('RGB')
result.show()
result.save(image_to_tile.split(".")[0] + "_tiled.jpg")