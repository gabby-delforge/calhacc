import struct 
import matplotlib as mpl
import numpy as np
import io



num_images = #however many images are in the file
def convert(imgs, labels):
	#Remove header
	
	with open(imgs, 'rb') as open_image:
		magic, num_img, rows, cols = struct.unpack(">IIII", openfile.read(16))

	with open(labels, 'rb') as open_label:
		magic, num_img = struct.unpack(">II", openfile.read(8))
		

	get_img = lambda i: (imgs[i], labels[i])
	
	#num_imgs = 
	#num_rows = 
	#num_cols = 

	#Splice imgs
	#Returns a list of lists, num_imgs long
	imgs = splice_imgs(imgs_file)

	#Splice labels
	#Returns a list of labels, num_imgs long
	labels = splice_labels(labels_file)

	#Merge into correct format
	#merged = 
	
	#return merged 


"""returns a list of lists where each nested list contains all the pixel values
for a particular image"""
def splice_imgs(img_file):
	result = []
	#make the file into a stream of bytes
	pixels_stream = open(img_file, 'rb')
	pixels_stream.read(4)
	pixels_stream.read(4)
	pixels_stream.read(4)
	pixels_stream.read(4)
	while len(result) < num_images:
		num_pixels = 0
		img_pixels = []
		while num_pixels < 400:
			_next = pixels_stream.read(1)
			pixel = struct.unpack("B", _next)
			print(pixel)
			img_pixels.append(pixel)

			num_pixels += 1
		result.append(img_pixels)
	return result



"""returns a list of integers where each integer matches with the number to be
read from the corresponding image"""
def splice_labels(labels_file):
	result = []
	labels_stream = open(labels_file)
	labels_stream.read(4)
	labels_stream.read(4)
	while len(result) < 60000:
		_next = labels_stream.read(1)
		label = struct.unpack("B", _next)
		print(label)
		result.append(label)
	return result





#DESIRED OUTPUT:
#List of tuples, each tuple containing a list of pixel values and a label
#[([1, 2, 3, 4], 5), ([1, 2, 3, 4], 5), ([1, 2, 3, 4], 5)]