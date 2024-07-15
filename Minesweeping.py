#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:50:01 2023

@author: chenyux
"""
import random

def printrow(row,status):
    n=1
    while n<=9:
        if row[n]!=-1 and row[n]!=0:
            print(row[n],end=" ")
        if row[n]==0:
            print("□",end=" ")
        if row[n]==-1:
            if status==-1:
                print("●",end=" ")
            if status==1:
                print("⚑",end=" ")
        n+=1
    
def printall(matrix,status):
    print("    1 2 3 4 5 6 7 8 9")
    print("  ┌───────────────────┐")
    i=1
    while i<=9:
        print(str(i),end=" │ ")
        printrow(matrix[i],status)
        print("│")
        i+=1
    print("  └───────────────────┘")
    
# def printall(matrix,status):
#     print("    1 2 3 4 5 6 7 8 9")
#     print("  ╔═══════════════════╗")
#     i=1
#     while i<=9:
#         print(str(i),end=" ║ ")
#         printrow(matrix[i],status)
#         print("║")
#         i+=1
#     print("  ╚═══════════════════╝")

# def printall(matrix,status):
#     print("    1 2 3 4 5 6 7 8 9")
#     print("  ┏━━━━━━━━━━━━━━━━━━━┓")
#     i=1
#     while i<=9:
#         print(str(i),end=" ┃ ")
#         printrow(matrix[i],status)
#         print("┃")
#         i+=1
#     print("  ┗━━━━━━━━━━━━━━━━━━━┛")

def overlap(surface,table):
    count=0
    i=1
    while i<=9:
        j=1
        while j<=9:
            if table[j][i]==surface[j][i]:
                count+=1
            j+=1
        i+=1
    return count

status=0

row0=[0,0,0,0,0,0,0,0,0,0,0]
row1=[0,0,0,0,0,0,0,0,0,0,0]
row2=[0,0,0,0,0,0,0,0,0,0,0]
row3=[0,0,0,0,0,0,0,0,0,0,0]
row4=[0,0,0,0,0,0,0,0,0,0,0]
row5=[0,0,0,0,0,0,0,0,0,0,0]
row6=[0,0,0,0,0,0,0,0,0,0,0]
row7=[0,0,0,0,0,0,0,0,0,0,0]
row8=[0,0,0,0,0,0,0,0,0,0,0]
row9=[0,0,0,0,0,0,0,0,0,0,0]
row10=[0,0,0,0,0,0,0,0,0,0,0]

table=[row0,row1,row2,row3,row4,row5,row6,row7,row8,row9,row10]

line0=['■','■','■','■','■','■','■','■','■','■','■']
line1=['■','■','■','■','■','■','■','■','■','■','■']
line2=['■','■','■','■','■','■','■','■','■','■','■']
line3=['■','■','■','■','■','■','■','■','■','■','■']
line4=['■','■','■','■','■','■','■','■','■','■','■']
line5=['■','■','■','■','■','■','■','■','■','■','■']
line6=['■','■','■','■','■','■','■','■','■','■','■']
line7=['■','■','■','■','■','■','■','■','■','■','■']
line8=['■','■','■','■','■','■','■','■','■','■','■']
line9=['■','■','■','■','■','■','■','■','■','■','■']
line10=['■','■','■','■','■','■','■','■','■','■','■']

surface=[line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10]

print()
print('Welcome to MINESWEEPER!')
print()
num=input("Number of Mines:")
num=int(num)
print()
print("Let's Start!")
print('>> Tips: u=▲, d=▼, l=◀︎, r=▶︎, x,y=loaction')
print()

bomb=set()
n=1
while n<=num:
    x = random.randint(1,9)
    y = random.randint(1,9)
    if (x,y) not in bomb:
        bomb.add((x,y))
        table[y][x]=-1
        i=-1
        while i<=1:
            j=-1
            while j<=1:
                if table[y+j][x+i]!=-1:
                    table[y+j][x+i]+=1
                j+=1
            i+=1
        n+=1

printall(surface,status)
print()
step=1

while step>0:
    ans=input("step_"+str(step)+" ")
    print()
    if ',' in ans:
        x=int(ans[0])
        y=int(ans[2])
    else:
        x+=ans.count('r')
        x-=ans.count('l')
        y-=ans.count('u')
        y+=ans.count('d')
    
    surface[y][x]=table[y][x]
    if table[y][x]==0:
        i=-1
        while i<=1:
            j=-1
            while j<=1:
                surface[y+j][x+i]=table[y+j][x+i]
                j+=1
            i+=1
    if table[y][x]==-1:
        status=-1
        break
    if overlap(surface,table)==81-num:
        status=1
        break
    
    printall(surface,status)
    print()
    print()
    step+=1
if status==-1:
    printall(table,status)
    print()
    print("You lose. :(")
if status==1:
    printall(table,status)
    print()
    print("You win! :)")

        