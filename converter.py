import struct 
import matplotlib

def convert(imgs, labels):
	#Remove header
	print("hi")
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

#DESIRED OUTPUT:
#List of tuples, each tuple containing a list of pixel values and a label
#[([1, 2, 3, 4], 5), ([1, 2, 3, 4], 5), ([1, 2, 3, 4], 5)]