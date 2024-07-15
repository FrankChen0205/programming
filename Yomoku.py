#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 23:01:56 2023

@author: chenyux
"""

def printrow(row):
    n=0
    while n<=16:
        print(row[n],end="")
        n+=1
    print()
    
def printall():
    i=1
    print("  1 2 3 4 5 6 7 8 9")
    while i<=9:
        print(str(i)+" ",end="")
        printrow(table[i-1])
        i+=1

    
def check(set):
    result=0
    i=1
    while i<=9:
        j=1
        while j<=9:
            if (i,j)in set and (i,j+1)in set and (i,j+2)in set and (i,j+3)in set:
                result=1
            if (i,j)in set and (i+1,j)in set and (i+2,j)in set and (i+3,j)in set:
                result=1
            if (i,j)in set and (i+1,j+1)in set and (i+2,j+2)in set and (i+3,j+3)in set:
                result=1
            if (i,j)in set and (i+1,j-1)in set and (i+2,j-2)in set and (i+3,j-3)in set:
                result=1
            j+=1
        i+=1
    return result

black=set()
white=set()
    
row1=["┌","─","┬","─","┬","─","┬","─","┬","─","┬","─","┬","─","┬","─","┐"]
row2=["├","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┤"]
row3=["├","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┤"]
row4=["├","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┤"]
row5=["├","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┤"]
row6=["├","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┤"]
row7=["├","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┤"]
row8=["├","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┤"]
row9=["└","─","┴","─","┴","─","┴","─","┴","─","┴","─","┴","─","┴","─","┘"]
table=[row1,row2,row3,row4,row5,row6,row7,row8,row9]

step=1
while 1==1:
    
    x,y=input("step_"+str(step)+" : ● ").split(",")
    x,y=int(x),int(y)
    table[y-1][2*x-2]="●"
    black.add((x,y))
    print()  
    printall()
    step+=1
    print()
    if check(black)==1:
        print("● wins!")
        break
    print()

    x,y=input("step_"+str(step)+" : ○ ").split(",")
    x,y=int(x),int(y)
    table[y-1][2*x-2]="○"
    white.add((x,y))
    print()
    printall()
    step+=1
    print()
    if check(white)==1:
        print("○ wins!")
        break
    print()


