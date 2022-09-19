# Lance Mendenhall
# September 19, 2022

from bs4 import BeautifulSoup
with open("books.xml") as f:
    data = f.read()
soup = BeautifulSoup(data,"html.parser")

with open("changes.txt") as f:
    for line in f:
        if(line.strip(' \n') != ""):
            # print(line)
            sss = line.split("|")
            t = sss[0].strip()     # tag
            c = sss[1].strip()     # content
            
            mytag = soup.find_all(t)
            
            for x in mytag:
                x.string.replace_with(c)

with open("different.xml", "w") as file:
    file.write(str(soup))