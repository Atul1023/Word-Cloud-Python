from wordcloud import WordCloud, STOPWORDS
import os
from PIL import Image
import numpy as np
import re

current_dir = os.path.dirname(__file__)

#reading file from console
def file_to_text(filename) :
    # uninteresting_words = ["<Media omitted>", "Media", "omitted", '<Media omitted>', "the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    #                        "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
    #                        "they", "them", \
    #                        "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
    #                        "been", "being", \
    #                        "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
    #                        "where", "how", \
    #                        "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
    #                        "can", "will", "just"]


    fh = open(filename, encoding='cp437')
    lst = []
    for line in fh :
        line.strip()
        # index = line.find(": <")
        # line = line[:index]
        line = line.split()
        for word in line :
            if len(word) > 0 :
                lst.append(word)
    str = ""
    for word in lst :
        # if word not in uninteresting_words :
            str += word + " "

    return str
    # frequencies = {}
    #
    # for word in words:
    #     if word.lower() not in frequencies:
    #         frequencies[word.lower()] = 1
    #     else:
    #         frequencies[word.lower()] += 1

# print(file_to_text("sample.txt"))

#Removing unnecessary emojis
def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')

string = deEmojify(file_to_text("chats.txt"))
# print(string)

#generating wordcloud
def create_wordcloud(text) :
    stopwords = set(STOPWORDS)

    wc = WordCloud(background_color="black", max_words=200, stopwords=stopwords, width=1600, height=800)
    wc.generate(text)

    wc.to_file(os.path.join(current_dir,"wc.png"))

create_wordcloud(string)
