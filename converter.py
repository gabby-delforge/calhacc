import struct 
from matplotlib import plot
import io

def convert(imgs, labels):
	#Remove header
	openfile = open(imgs, 'rb')
	a = array.array("L")
	header = a.fromfile(openfile, 4)
	header2 = struct.unpack(">", openfile)
	print(header)
	print(header2)
	#num_imgs = 
	#num_rows = 
	#num_cols = 

	#Splice imgs
	#Returns a list of lists, num_imgs long
	#imgs = 

	#Splice labels
	#Returns a list of labels, num_imgs long
	#labels = 

	#Merge into correct format
	#merged = 
	
	#return merged 


"""returns a list of lists where each nested list contains all the pixel values
for a particular image"""
def splice_imgs(img_file):
	result = []
	#make the file into a stream of bytes
	pixels_stream = io.open(img_file)
	while result.length < 60000:
		num_pixels = 0
		img_pixels = []
		while num_pixels < 784:
			_next = pixels_stream.read(4)
			pixel = struct.unpack("I", _next)
			img_pixels.append(pixel)

			num_pixels += 1
		result.append(img_pixels)
	return result



"""returns a list of integers where each integer matches with the number to be
read from the corresponding image"""
def splice_labels(labels_file):
	result = []
	labels_stream = io.open(labels_file)
	while result.length < 60000:
		_next = labels_stream.read(4)
		label = struct.unpack("I", _next)
		result.append(label)
	return result





#DESIRED OUTPUT:
#List of tuples, each tuple containing a list of pixel values and a label
#[([1, 2, 3, 4], 5), ([1, 2, 3, 4], 5), ([1, 2, 3, 4], 5)]