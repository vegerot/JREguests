#!/usr/bin/env python3

import re
import numpy as np
import pandas as pd
import youtube_dl
from tabulate import tabulate

def getTitles():
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

    with ydl:
        ydl.params.update(ignoreerrors=True) #Dom Irrera's podcast is blocked on Copyright grounds
        result = ydl.extract_info(
            'https://www.youtube.com/playlist?list=UUzQUP1qoWDoEbmsQxvdjxgQ',
            download = False # We just want to extract the info
        )

    titles = []
    for t in range(len(result['entries'])):
        try:
            titles.append(result['entries'][t]['title'])
        except:
            pass        
    out = open('titles.txt', 'w')
    
    for title in titles:
        out.write('%s\n' %title)

    return titles

def getNames(titles):
    names = []
    p = re.compile(r'^.*?#.*?(-|with)+\s*?(?P<name>.*?)(\(.*?\))?$')
    for title in titles:
        try:
            allGuests = re.split(',|&', p.match(title).group('name'))
            for person in allGuests:
                person = person.strip()
                names.append(person)
        except Exception as err:
            #print(err)
            #print(title)
            pass
    return names

def count(names):
    npNames = np.array(names)
    sortedNames = np.sort(npNames)
    res = pd.value_counts(sortedNames, sort=True)
    nRes = np.transpose(np.array([res.keys().to_numpy(),res.to_numpy()]))
    return nRes

def removeSingles(arr):
    delRange = []
    for i in range(len(arr)):
        if arr[i][1] == 1:
            delRange.append(i)
    arr = np.delete(arr, delRange, 0)
    return arr

def mathewPrinciple(arr):
   print(np.sum(arr[:int(np.sqrt(len(arr)))][:,1]))
   print(np.sum(arr[int(np.sqrt(len(arr)))+1:][:,1]))



def printer(counts):
    print(tabulate(counts))

def redditPrinter(counts):
    for guest in counts:
        print("|"+guest[0]+"|"+str(guest[1])+"|")

def main():
    #Uncomment to download list from web (slow)
    #titles = getTitles()

    #Uncomment below to use cached list (fast)
    titles = open('allTitles.txt')

    names = getNames(titles)
    viewCounts = count(names)
    #redditPrinter(viewCounts)
    relevantCounts = removeSingles(viewCounts)
    printer(relevantCounts)

if __name__ == '__main__':
    main()