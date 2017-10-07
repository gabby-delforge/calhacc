import struct 
import matplotlib as mpl
import numpy as np
import io

num_pixels = 784
num_imgs = 10000

def convert(imgs, labels):
	#Remove header
	
	with open(imgs, 'rb') as open_image:
		magic, num_img, rows, cols = struct.unpack(">IIII", open_image.read(16))

	with open(labels, 'rb') as open_label:
		magic, num_img = struct.unpack(">II", open_label.read(8))
			
	imgs_list = splice_imgs(imgs)
	labels_list = splice_labels(labels)

	get_tuple = lambda i: (imgs_list[i], labels_list[i])

	merged = []
	for i in range(num_imgs):
		merged += get_tuple(i)

"""returns a list of lists where each nested list contains all the pixel values
for a particular image"""
def splice_imgs(img_file):
	result = []
	#make the file into a stream of bytes
	pixels_stream = open(img_file, 'rb')
	pixels_stream.read(16)
	num_imgs_read = 1
	while len(result) < num_imgs:
		pixels_count = 0
		img_pixels = []
		while pixels_count < num_pixels:
			_next = pixels_stream.read(1)
			pixel = struct.unpack("B", _next)
			print(pixel[0])
			img_pixels.append(pixel[0])

			pixels_count += 1
		print("i've reached the end of image " + str(num_imgs_read) + "!")
		num_imgs_read += 1
		result.append(img_pixels)
	return result



"""returns a list of integers where each integer matches with the number to be
read from the corresponding image"""
def splice_labels(labels_file):
	result = []
	labels_stream = open(labels_file, 'rb')
	labels_stream.read(8)
	num_labels_read = 1
	while len(result) < num_imgs:
		_next = labels_stream.read(1)
		label = struct.unpack("B", _next)
		print(label[0])
		print("i've reached the end of label " + str(num_labels_read) + "!")
		num_labels_read += 1
		result.append(label[0])
	return result





#DESIRED OUTPUT:
#List of tuples, each tuple containing a list of pixel values and a label
#[([1, 2, 3, 4], 5), ([1, 2, 3, 4], 5), ([1, 2, 3, 4], 5)]