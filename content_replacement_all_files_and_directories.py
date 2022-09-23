# Lance Mendenhall
# September 19, 2022

from bs4 import BeautifulSoup
import os

start_string = "CAD"
end_string = "xml"

len_start_string = len(start_string)
len_end_string = len(end_string)
threshold = max(len_start_string,len_end_string)

for root, dirs, filename in os.walk("content"):
    for afile in filename: 
        if len(afile) >= threshold:
            if (afile[0:3] == start_string) and (afile[-3:].lower() == end_string):

                # print("filename",afile)

                path = root + "\\" + afile
                # print("path:",path)

                f = open(path)
                data = f.read()
                f.close()

                soup = BeautifulSoup(data,"xml")

                with open("changes.txt") as f:
                    for line in f:
                        if(line.strip(' \n') != ""):

                            sss = line.split("|")
                            t = sss[0].strip()     # tag
                            c = sss[1].strip()     # content
                            
                            mytag = soup.find_all(t)
                            
                            for x in mytag:
                                x.string.replace_with(c)

                with open(path, "w") as file:
                    file.write(str(soup))

	


# CAD * .twb - fix only those