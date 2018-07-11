import os 
import json 
import collections


filename = "index.json"
indexFile = open(filename ,"w+")

#Delete contents of indexFile
indexFile.truncate(0)

#Get directory where this script is located 
currentDirectory = os.path.dirname(os.path.realpath(__file__))

all_files = list()

#Setup JSON object 
index_data = {} 

base_url = "https://github.com/vedantroy/Image-Database/raw/master/Curated"

#Traverse all sub-directories. 
for sub_dir in os.walk(currentDirectory):
	#I know none of my subdirectories will have their own subfolders 
	if len(sub_dir[1]) == 0:
		sub_dir_name = sub_dir[0].split('\\')[-1]

		if len(sub_dir[2]) == 0:
			print("Empty directory: " + sub_dir_name)
		#Prepend url to each file name
		file_urls = list()
		for file_name in sub_dir[2]:
			all_files.append(file_name)
			file_urls.append(base_url + "/" + sub_dir_name + "/" + file_name)

		index_data[sub_dir_name] = file_urls



indexFile.write(json.dumps(index_data))
indexFile.close()

print("Duplicates: ")
print([item for item, count in collections.Counter(all_files).items() if count > 1])


#Open file in default program
os.system("start " + filename)