#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


i = 0
cache = [] 
length = 0
hit = 0
j = 0

with open('user-ct-test-collection-02.txt','r') as file:
    for line in file:
        if(j > 500000):
            break
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


def find_in_cache(word,time):
    for i in range(len(cache)):
        if(cache[i][0] == word):
            cache[i][1] = time
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
        
def put_in_cache(word,time,size):
    if(size <= cache_size):
        word_array = []
        word_array.append(word)
        word_array.append(time)
        cache.append(word_array)
    else:
        index = find_min()
        cache[index][0] = word
        cache[index][1] = time



with open('user-ct-test-collection-02.txt','r') as file:
    for line in file:
        i = 0
        if(length > 500000):
            break
        print(length,"  /  " ,words)
        for word in line.split():
                 
            if(i == 0):
                i += 1
                continue
            if('-' in word):
                break
            
            word_time = time.time() 
            length += 1
            check = find_in_cache(word,word_time)
            if(check == True):
                hit += 1
                continue
            else:
                put_in_cache(word,word_time,length)

print("cache hit:",hit/length*100,"%")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
