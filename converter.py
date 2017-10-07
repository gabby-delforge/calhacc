import struct 
import matplotlib as mpl
import numpy as np

num_pixels = 784
num_imgs = 10000

def convert(imgs, labels):
	#Remove header
	
	with open(imgs, 'rb') as open_image:
		magic, num_img, rows, cols = struct.unpack(">IIII", open_image.read(16))

	with open(labels, 'rb') as open_label:
		magic, num_img = struct.unpack(">II", open_label.read(8))
			
	print("Before image splicing")		
	imgs_list = splice_imgs(imgs)
	print("Before labels splicing")		
	labels_list = splice_labels(labels)
	print("After label splicing")		


	get_tuple = lambda i: (imgs_list[i], labels_list[i])

	merged = []
	for i in range(num_imgs):
		merged += get_tuple(i)
		
	print(merged)
	return merged

"""returns a list of lists where each nested list contains all the pixel values
for a particular image"""
def splice_imgs(img_file):
	result = []
	#make the file into a stream of bytes
	with open(img_file, 'rb') as pixels_stream:
		pixels_stream.read(16)
		num_imgs_read = 1
		while len(result) < num_imgs:
			pixels_count = 0
			img_pixels = []
			while pixels_count < num_pixels:
				try:
					_next = pixels_stream.read(1)
					pixel = struct.unpack("B", _next)
					#print(pixel[0])
					img_pixels.append(pixel[0])

					pixels_count += 1
				except structerror: 
					print("reached the end of the stream ( at image number " + str(pixels_count) + ")")
					return result
			#print("i've reached the end of image " + str(num_imgs_read) + "!")
			num_imgs_read += 1
			result.append(img_pixels)
	return result



"""returns a list of integers where each integer matches with the number to be
read from the corresponding image"""
def splice_labels(labels_file):
	result = []
	with open(labels_file, 'rb') as labels_stream:
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

convert("MNISTfiles/test_images", "MNISTfiles/test_labels")




#DESIRED OUTPUT:
#List of tuples, each tuple containing a list of pixel values and a label
#[([1, 2, 3, 4], 5), ([1, 2, 3, 4], 5), ([1, 2, 3, 4], 5)]