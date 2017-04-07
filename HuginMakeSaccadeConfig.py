#!/usr/bin/python3
import json
import sys
from collections import OrderedDict
import xml.etree.ElementTree
import math
import os
import re
#parses json data from .pano into the .json file
#input pano filename, textfile with ports, and new json filename in that order as arguments



def parse(pano, filename):

	yaw = list()
	pitch = list()
	roll = list()
	k1 = list()
	offsetx = list()
	offsety = list()
	f = list()
	s = list()
	vig2 = list()
	vig4 = list()
	vig6 = list()
	redg = list()
	blueg = list()
	gain = list()

	#opens and parses through pano file, putting values in a list
	with open(pano) as openfileobject:
		for line in openfileobject:
			if "#-hugin" in line:
				print(line)
				temp=openfileobject.readline()
				print(temp)
				m=re.search('\sy\S+\s',temp)
				y=(temp[m.start()+2:m.end()])
				print("yaw is "+ str(y))
				m=re.search('\sp\S+\s',temp)
				p=(temp[m.start()+2:m.end()])
				print("pitch is "+ str(p))
				m=re.search('\sr\S+\s',temp)
				r=(temp[m.start()+2:m.end()])
				print("roll is "+ str(r))

				m=re.search('\sb\S+\s',temp)
				if(temp.find('=')!=-1):
					print("found the equals")
				else:
					k=(temp[m.start()+2:m.end()])
				print("distortion is "+ str(k))


				m=re.search('\sv\S+\s',temp)
				fov=(temp[m.start()+2:m.end()])
				print("fov is "+ str(fov))

				m=re.search('\sw\S+\s',temp)
				width=(temp[m.start()+2:m.end()])
				print("width is "+ str(width))

				m=re.search('\sh\S+\s',temp)
				height=(temp[m.start()+2:m.end()])
				print("height is "+ str(height))

				if(fov.find('=')!=-1):
					print("found the equals")
				else:
					F=float(width)/(math.pi*float(fov)/180)
				#	F=41578.58/float(fov)
					F=220363.4/float(fov) # = 41578* 5.2
				print("f is "+str(F))

				#m=re.search('mcam_\S+.',temp)
				#slot=(temp[m.start():m.end()].split('.')[0].split('_')[1])
				m=re.search('1700\S+.',temp)
				slot=temp[m.start()-3:m.end()].split('.')[0]
				print("slot is "+str(slot))

				m=re.search('\sVb\S+\s',temp)
				if(temp.find('=')!=-1):
					print("found the equals")
				else:
					v_r2=(temp[m.start()+3:m.end()])
				print("vignetting r2 term is "+str(v_r2))

				m=re.search('\sVc\S+\s',temp)
				if(temp.find('=')!=-1):
					print("found the equals")
				else:
					v_r4=(temp[m.start()+3:m.end()])
				print("vignetting r4 term is "+str(v_r4))

				m=re.search('\sVd\S+\s',temp)
				if(temp.find('=')!=-1):
					print("found the equals")
				else:
					v_r6=(temp[m.start()+3:m.end()])
				print("vignetting r6 term is "+str(v_r6))

				m=re.search('\sEr\S+\s',temp)
				Er=(temp[m.start()+3:m.end()])
				print("red gain term is "+str(Er))

				m=re.search('\sEb\S+\s',temp)
				Eb=(temp[m.start()+3:m.end()])
				print("blue gain term is "+str(Eb))

				m=re.search('\sEev\S+\s',temp)
				Eev=(temp[m.start()+4:m.end()])
				print("overall gain term is "+str(Eev))


				k1.append(float(k))
				s.append(int(slot))
				f.append(float(F))
				roll.append(float(r))
				pitch.append(float(p))
				yaw.append(float(y))
				vig2.append(float(v_r2))
				vig4.append(float(v_r4))
				vig6.append(float(v_r6))
				#redg.append(float(Er)*float(Er))
				redg.append(1/(float(Er)*float(Er)))
				#blueg.append(float(Eb)*float(Eb))
				blueg.append(1/(float(Eb)*float(Eb)))
				#gain.append(math.sqrt((pow(2.0,float(Eev)))))
				gain.append(1.0)

#	f=open(pano,'r')
	print(yaw[1])
	print(roll[1])
	print(f[1])
	vig2_avg=sum(vig2)/len(vig2)
	vig4_avg=sum(vig4)/len(vig4)
	vig6_avg=sum(vig6)/len(vig6)
	#	#m=re.search("-hugin",str(lines))
#	#if m:
#		print(lines(m.start():m.start()+20))
#	e = xml.etree.ElementTree.parse(pano).getroot()#
#	x = 0
#	i = 1
#	for child in e:
#		if(child.tag == "images"):
#			while(len(s)<len(child)):
#				for child2 in child:
#					for child3 in child2:
#						if(child3.tag=="def"):
#							fi = child3.get('filename')
#							head, sep, tail = fi.partition('mcam_')
#							head2, sep2, tail2 = tail.partition('.')
#							if(int(head2)==i):
#								s.append(head2)
#								i+=1
#								for child3 in child2:
#									if(child3.tag == "camera"):
#										y = child3.get('yaw')
#										y = float(y)
#										y = (180*y)/math.pi
#										yaw.append(y)
#										p = child3.get('pitch')
#										p = float(p)
#										p = (180*p)/math.pi
#										pitch.append( p)
#										r = child3.get('roll')
#										r = float(r)
#										r = (180*r)/math.pi
#										roll.append(r)
#										k = child3.get('k1')
#										k = float(k)
#										k1.append(k)
#										F = child3.get('f')
#										f.append(F)
#										x+=1

#	from PIL import Image#
#	#im = Image.open(fi)#
#	#print(im.size) # returns (width, height) tuple
#	fi_index=fi.rindex('/')
#	mcam_file=fi[fi_index+1:]
#	print('filename is ',mcam_file)
#	im=Image.open(mcam_file)
#	print(im.size[1])

	#opens and parses through json file, saving new pano values
	with open('reference.json') as json_file:
		json_data = json.load(json_file, object_pairs_hook = OrderedDict)

	poly = list()
	i = 0
	while(i < 10):
		alist = list()
		alist.insert(0, 0)
		poly.insert(i, alist)
		i +=1
	alist = list()
	alist.insert(0, 1)
	poly.insert(i, alist)
	poly[-2]=[vig2_avg]
	poly[-3]=[vig4_avg]
	poly[-4]=[vig6_avg]
	print(poly)
	for key in json_data.keys():
		for key2 in json_data[key]:
			if(key2 == "global"):
				json_data[key][key2]['vig_poly_red'] = poly
				json_data[key][key2]['vig_poly_green'] = poly
				json_data[key][key2]['vig_poly_blue'] = poly
				json_data[key][key2]['sensorwidth'] = int(width)
				json_data[key][key2]['sensorheight'] = int(height)
				json_data[key][key2]['pixel_size'] = .0014
				json_data[key][key2]['focal_length'] = 35
			if(key2 == "microcameras"):
				i = 0
				while(i<len(json_data[key][key2])):
					json_data[key][key2][i] = {'Slot': int(s[i]), 'Sensorcal': ["1",str(redg[i]),  str(blueg[i]),"1"], 'gain': gain[i], 'vigoffset_x': 0, 'vigoffset_y': 0, 'Yaw': yaw[i], 'Pitch': pitch[i], 'Roll': roll[i], 'K1': k1[i], 'OFFSET_X': 0, 'OFFSET_Y': 0, 'F': f[i]}
					i +=1
				while(i<len(s)):
					json_data[key][key2].append({'Slot': int(s[i]), 'Sensorcal': ["1",str(redg[i]), str(blueg[i]),"1"], 'gain': gain[i], 'vigoffset_x': 0, 'vigoffset_y': 0, 'Yaw': yaw[i], 'Pitch': pitch[i], 'Roll': roll[i], 'K1': k1[i], 'OFFSET_X': 0, 'OFFSET_Y': 0, 'F': f[i]})
					i+=1


	#saves new json file
	data = json.dumps(json_data, indent=4)
	with open(filename, "w") as outfile:
		outfile.write(data)
		print(data)
		print("Wrote above data to "+filename)




if __name__ == "__main__":
	parse(sys.argv[1], sys.argv[2])
