import time
from typing import final
from bs4 import BeautifulSoup
import requests
import re
import random


#random words for website.

Genres = ["vaporwave","jazz","blues","soul_music","nightcore"]
# function
def cleanUp(final_string):

	# remove all citations and additional space.
    final_string = re.sub(r'\[[0-9]*\]',' ',final_string)
    final_string = re.sub(r'\s+',' ',final_string)
    return final_string


def proccess(keyWord):
    
    url = "https://en.wikipedia.org/wiki/" + keyWord

	# request the url for wiki
    res = requests.get(url)

    doc = BeautifulSoup(res.text, "html.parser")
		
	# grab all passages and store in list.	
    passages = doc.find_all(["p"])

    possible_list = []
    index = 0
	
	# select the first list that has more than 20 words.
    for i in range(len(passages)):
        length = passages[i].text.split(" ")
        if len(length) > 20:
            index = i
            break
                

        
    pass_text = passages[index].text.split(" ")

	# split the list and then reconstruct it.
    final_string = ""

    for x in range(len(pass_text)):
        final_string += pass_text[x]

        if(x != len(pass_text)-1):
            final_string += " "
    
    return final_string




while True:
    
    # read the first line in the file
	
    read_com = open("pipe.txt", "r")
    line1 = read_com.readline()
	
    # remove any line breaks
    line1 = line1.rstrip('\n')
    

    if (line1 == "vaporwave"):
        
        # if the first line is simply 'vaporwave' then a request has been sent. Now read the second line.
        key2 = read_com.readline()
        read_com.close()

        keyWord = line1
        # pass the first keyword in to a function to web scrape.
        final_string = proccess(keyWord)
		# pass the second keyword in to the function to web scrape.
        fin_string2 = proccess(key2)
    
		# Remove all non English and citations from the paragraph.
        string1 = cleanUp(final_string)
        string2 = cleanUp(fin_string2)
        
		# write both paragraphs to the text file.
        write_to = open("pipe.txt", "w")
        write_to.write(string1 + "\n")
        write_to.write(string2 + "\n")
        print(string1)
        print(" ")
        print(string2)
        
        write_to.close()
    

        
        
       


