#!/usr/bin/env python3

import re
import numpy as np
import sys
import pandas as pd
import IPython

def print_full(x):
    pd.set_option('display.max_rows', len(x))
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', -1)
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.float_format')
    pd.reset_option('display.max_colwidth')


def count():
    titles = open('allTitles.txt', 'r')

    names = []
    p = re.compile(r'^.*?#.*?(-|with)\s*?(?P<name>.*?)(\(.*?\))?$')
    for title in titles:
        try:
            guests = re.split(',|&', p.match(title).group('name'))
            for person in guests:
                person=person.strip()
                names.append(person)
        except Exception as err:
            pass


    npNames = np.array(names)
   
    sortedNames=np.sort(npNames)

    res=pd.value_counts(sortedNames, sort=True)
    

    nRes=np.transpose(np.array([res.keys().to_numpy(),res.to_numpy()]))
    #print(list(nRes))
    calculations(nRes)
def calculations(arr):
    delRange=[]
    for i in range(len(arr)):
        if arr[i][1]==1:
            delRange.append(i)
    arr = np.delete(arr, delRange, 0)
   # print(np.lexsort((arr[:0],arr[:1])))
   # print(arr)
    IPython.embed()


def main():
    count()
    #IPython.embed()



if __name__ == "__main__":
    main()


#np.set_printoptions(threshold=sys.maxsize)
#print(type(npNames))
#
#nam,cnt=np.unique(npNames,return_counts=True)
#
#cnt2=np.array(list(map(int, cnt)))
#
#
#namCnt=np.array([nam,cnt2])

#print(np.sort(np.transpose(namCnt), axis=0))
