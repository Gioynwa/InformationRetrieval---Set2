#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:05:48 2020

@author: tsiv
"""


import time

start_time = time.time()
i = 0
cache = [] 
length = 0
j = 0
hit = 0

with open('user-ct-test-collection-02.txt','r') as file:
    for line in file:
        i = 0
        for word in line.split():
                 
            if(i == 0):
                i += 1
                continue
            if('-' in word):
                break
            
            j += 1

words = j
cache_size = int(j/100)

def find_in_cache(word):
    for i in range(len(cache)):
        if(cache[i][0] == word):
            cache[i][1] += 1
            return True
    return False
     
def find_min():
    min = cache[0][1]
    index = 0
    for i in range(len(cache)):
        if(cache[i][1] < min):
            min = cache[i][1]
            index = i
    return index
        
def put_in_cache(word,size):
    if(size <= cache_size):
        word_array = []
        word_array.append(word)
        word_array.append(1)
        cache.append(word_array)
    else:
        index = find_min()
        cache[index][0] = word
        cache[index][1] = 1

clock = time.time()

with open('user-ct-test-collection-02.txt','r') as file:
    for line in file:
        i = 0
        print(length,"  /  " ,words)
        for word in line.split():
                 
            if(i == 0):
                i += 1
                continue
            if('-' in word):
                break
            
            length += 1
            check = find_in_cache(word)
            if(check == True):
                hit += 1
                continue
            else:
                put_in_cache(word,length)

print("cache hit:",hit/length * 100,"%")
        
        
        