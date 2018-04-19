# -*- coding:utf-8 -*-
from string import maketrans 
import pandas as pd

word_freq = {}
word_list = open(r"./AV1611Bible.txt", "r").read().split() 
for word in word_list:
    word = word.translate(maketrans("",""), '!"#$%&()*+,./:;<=>?@ [\\]^_`{|}~0123456789')
    if word.startswith('-'):
        word = word.replace('-','')
    if len(word):
        word_freq[word] = word_freq.get(word, 0) + 1 
keys = sorted(word_freq.keys())
x=pd.DataFrame(keys)
x.to_pickle('uniqueWords.pickle')

def binaryText(x, target, my_min=1, my_max=None):
    if my_max is None:
        my_max = len(x) - 1
        while my_min <= my_max:
            mid = (my_min + my_max)//2
            midval = x.iloc[mid]
            if midval.values < target:
                my_min = mid + 1
            elif midval.values > target:
                my_max = mid - 1
            else:
                return mid 
    raise ValueError

