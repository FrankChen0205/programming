#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 14:20:40 2023

@author: chen_ruiping
"""

def printrow(row):
    n=0
    while n<=14:
        print(row[n],end="")
        n+=1
    print()
    
def printall():
    i=1
    print("  1 2 3 4 5 6 7 8")
    while i<=8:
        print(str(i)+" ",end="")
        printrow(table[i-1])
        i+=1

def flip(x,y,p1,p2):
    if p1==black:
        chess='●'
    if p1==white:
        chess='○'
    i=1
    while True:
        if (x,y+i) in p1:
            i+=10
            break
        elif (x,y+i) in p2:
            i+=1
        else:
            break
    if i>10:
        for j in range(i-11):
            p2.remove((x,y+j+1))
            p1.add((x,y+j+1))
            table[y+j][2*x-2]=chess
            
    i=1
    while True:
        if (x,y-i) in p1:
            i+=10
            break
        elif (x,y-i) in p2:
            i+=1
        else:
            break
    if i>10:
        for j in range(i-11):
            p2.remove((x,y-j-1))
            p1.add((x,y-j-1))
            table[y-j-2][2*x-2]=chess
            
    i=1
    while True:
        if (x+i,y) in p1:
            i+=10
            break
        elif (x+i,y) in p2:
            i+=1
        else:
            break
    if i>10:
        for j in range(i-11):
            p2.remove((x+j+1,y))
            p1.add((x+j+1,y))
            table[y-1][2*x+2*j]=chess
            
            
    i=1
    while True:
        if (x-i,y) in p1:
            i+=10
            break
        elif (x-i,y) in p2:
            i+=1
        else:
            break
    if i>10:
        for j in range(i-11):
            p2.remove((x-j-1,y))
            p1.add((x-j-1,y))
            table[y-1][2*x-2*j-4]=chess
            
    i=1
    while True:
        if (x+i,y+i) in p1:
            i+=10
            break
        elif (x+i,y+i) in p2:
            i+=1
        else:
            break
    if i>10:
        for j in range(i-11):
            p2.remove((x+j+1,y+j+1))
            p1.add((x+j+1,y+j+1))
            table[y+j][2*x+2*j]=chess
            
    i=1
    while True:
        if (x-i,y-i) in p1:
            i+=10
            break
        elif (x-i,y-i) in p2:
            i+=1
        else:
            break
    if i>10:
        for j in range(i-11):
            p2.remove((x-j-1,y-j-1))
            p1.add((x-j-1,y-j-1))
            table[y-j-2][2*x-2*j-4]=chess
            
    i=1
    while True:
        if (x+i,y-i) in p1:
            i+=10
            break
        elif (x+i,y-i) in p2:
            i+=1
        else:
            break
    if i>10:
        for j in range(i-11):
            p2.remove((x+j+1,y-j-1))
            p1.add((x+j+1,y-j-1))
            table[y-j-2][2*x+2*j]=chess
            
    i=1
    while True:
        if (x-i,y+i) in p1:
            i+=10
            break
        elif (x-i,y+i) in p2:
            i+=1
        else:
            break
    if i>10:
        for j in range(i-11):
            p2.remove((x-j-1,y+j+1))
            p1.add((x-j-1,y+j+1))
            table[y+j][2*x-2*j-4]=chess

row1=["┌","─","┬","─","┬","─","┬","─","┬","─","┬","─","┬","─","┐"]
row2=["├","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┤"]
row3=["├","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┤"]
row4=["├","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┤"]
row5=["├","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┤"]
row6=["├","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┤"]
row7=["├","─","┼","─","┼","─","┼","─","┼","─","┼","─","┼","─","┤"]
row8=["└","─","┴","─","┴","─","┴","─","┴","─","┴","─","┴","─","┘"]
table=[row1,row2,row3,row4,row5,row6,row7,row8]

table[3][6]="○"
table[4][8]="○"
table[4][6]="●"
table[3][8]="●"
black=set()
white=set()
black.add((5,4))
black.add((4,5))
white.add((4,4))
white.add((5,5))
print()
printall()
print()
print()
step=1
flag=0
while flag<2 and len(black)+len(white)<64:
    flag=0
    ans=input("step_"+str(step)+" : ● ")
    if ans=='p':
        print('Pass.')
        flag+=1
    else:
        x=ans[0]
        y=ans[2]
        x,y=int(x),int(y)
        table[y-1][2*x-2]="●"
        black.add((x,y))
        flip(x,y,black,white)
        print()  
        printall()
    step+=1
    print()
    print()

    ans=input("step_"+str(step)+" : ○ ")
    if ans=='p':
        print('Pass.')
        flag+=1
    else:
        x=ans[0]
        y=ans[2]
        x,y=int(x),int(y)
        table[y-1][2*x-2]="○"
        white.add((x,y))
        flip(x,y,white,black)
        print()
        printall()
    step+=1
    print()
    print()
print('●',len(black))
print('○',len(white))
print()
if len(black)>len(white):
    print('● wins!')
if len(black)<len(white):
    print('○ wins!')
if len(black)==len(white):
    print("It's a tie.")