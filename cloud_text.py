'''
Created on 17 Sep 2019

@author: benjaminsenyonyi
'''
import matplotlib.pyplot as plt 
from wordcloud import WordCloud, STOPWORDS 


lines = ' '
stopwords = set(STOPWORDS) 

fileName = "read_up.txt"

with open(fileName, 'r') as file_for_cloud:
            for line in file_for_cloud:
                text = str(line)
                tokens = text.split()
                for i in range(len(tokens)): 
                    tokens[i] = tokens[i].lower() 
        
                for words in tokens: 
                    lines = lines + words + ' '


word_cloud =  WordCloud(font_path= "/Library/Fonts/Arial Italic.ttf",
                                height = 750, width = 600, background_color ='#EFEFEF', stopwords = stopwords).generate(lines) 

                   
plt.figure(figsize = (8, 8), facecolor = "#EFEFEF") 
plt.imshow(word_cloud) 
plt.tight_layout(pad = 0) 
plt.axis("off")


plt.show() 

