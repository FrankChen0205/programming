# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
from itertools import permutations

def point(x):
    if x<=52:
        n=((x-1)//4)+1
        return n
    else:
        if x==53:
            return 14
        if x==54:
            return 15

def points(card):
    points=[]
    for x in card:
        if x<=52:
            n=((x-1)//4)+1
        else:
            if x==53:
                n=14
            if x==54:
                n=15
        points.append(n)
    return points

def showpoint(x):
    if x<=52:
        if point(x)==11:
            return'K'
        elif point(x)==10:
            return'Q'
        elif point(x)==9:
            return'J'
        elif point(x)==8:
            return'X'
        elif point(x)==12:
            return'A'
        elif point(x)==13:
            return'2'
        else:
            return str(point(x)+2)
    else:
        if x==53:
            return'B'
        if x==54:
            return'R'
            
def deshow(x):
    if x=='2':
        return 13
    elif x=='A' or x=='a':
        return 12
    elif x=='K' or x=='k':
        return 11
    elif x=='Q' or x=='q':
        return 10
    elif x=='J' or x=='j':
        return 9
    elif x=='X' or x=='x':
        return 8
    elif x=='B' or x=='b':
        return 14
    elif x=='R' or x=='r':
        return 15
    else:
        return int(x)-2

def suit(x):
    if x<=52:
        n=x%4
        return n
    else:
        return 4

def showsuit(x):
    if suit(x)==0:
        return'♦'
    if suit(x)==1:
        return'♣'
    if suit(x)==2:
        return'♥'
    if suit(x)==3:
        return'♠'
    if suit(x)==4:
        return'J'

def printcard(card):
    l=len(card)
    for i in range (l):
        print('╭─',end='')
    print('─╮')
    for i in range (l):
        print('│',end='')
        print(showpoint(card[i]),end='')
    print(' │')
    for i in range (l):
        print('│',end='')
        print(showsuit(card[i]),end='')
    print(' │')
    for i in range (l):
        print('╰─',end='')
    print('─╯')
  

  
def delcard(perm,card):
    chupai=[]
    for i in range (len(perm)):
        if perm[i]==14:
            index=card.index(53)
            chupai.append(card[index])
            del card[index]
        if perm[i]==15:
            index=card.index(54)
            chupai.append(card[index])
            del card[index]
        else:
            if (perm[i])*4-3 in card:
                index=card.index((perm[i])*4-3)
                chupai.append(card[index])
                del card[index]
            elif (perm[i])*4-2 in card:
                index=card.index((perm[i])*4-2)
                chupai.append(card[index])
                del card[index]
            elif (perm[i])*4-1 in card:
                index=card.index((perm[i])*4-1)
                chupai.append(card[index])
                del card[index]
            elif (perm[i])*4 in card:
                index=card.index((perm[i])*4)
                chupai.append(card[index])
                del card[index]
    return [card,chupai]


def checkcard(points):
    l=len(points)
    result=[0]
    for perm in permutations(points,l):
        n=0
        for i in range (l-1):
            if perm[i]==perm[i+1]-1:
                n+=1
        if n==l-1 and l>=5:
            result=[l*10,perm[0]]
        else:
            if l==1:
                result=[1,perm[0]]
            if l==2:
                if perm[0]==53 and perm[1]==54:
                    result=[11]
                elif perm[0]==perm[1]:
                    result=[2,perm[0]]
            if l==3:
                if perm[0]==perm[1]==perm[2]:
                    result=[3,perm[0]]
            if l==4:
                if perm[0]==perm[1]==perm[2]==perm[3]:
                    result=[10,perm[0]]
                elif perm[0]==perm[1] and perm[2]==perm[3] and perm[0]<perm[2]:
                    result=[4,perm[2],perm[0]]
                elif perm[0]==perm[1]==perm[2] and perm[0]!=perm[3]:
                    result=[5,perm[0],perm[3]]
            if l==5:
                if perm[0]==perm[1]==perm[2] and perm[3]==perm[4]:
                    result=[6,perm[0],perm[3]]
            if l==6:
                if perm[0]==perm[1]==perm[2] and perm[3]==perm[4]==perm[5] and perm[0]<perm[3]:
                    result=[7,perm[3],perm[0]]
                if perm[0]==perm[1] and perm[2]==perm[3] and perm[4]==perm[5] and perm[0]<perm[2]<perm[4]:
                    result=[8,perm[4],perm[2],perm[0]]
            if l==8:
                if perm[0]==perm[1] and perm[2]==perm[3] and perm[4]==perm[5] and perm[6]==perm[7] and perm[0]<perm[2]<perm[4]<perm[6]:
                    result=[9,perm[6],perm[4],perm[2],perm[0]]
            if l==10:
                if perm[0]==perm[1] and perm[2]==perm[3] and perm[4]==perm[5] and perm[6]==perm[7] and perm[8]==perm[9] and perm[0]<perm[2]<perm[4]<perm[6]<perm[8]:
                    result=[9,perm[8],perm[6],perm[4],perm[2],perm[0]]
    return result

def countcard(card):
    l=len(checkcard(card))
    s=0
    for i in range(l-1):
        s+=checkcard(card)[i+1]*(0.1**i)
    return s

finish=0
flag=0
pile=[]
for i in range (54):
    pile.append(i+1)
random.shuffle(pile)

mycard=pile[0:18]
mycard.sort(reverse=True)
drcard=pile[-19:-1]
drcard.sort(reverse=True)
index=0
perm=0

while len(mycard)>0 and len(drcard)>0:
    print('你目前的手牌：')
    printcard(mycard)
    ans=input("")
    print()
    enter=[]
    out=[]
    if ans!='P' and ans!='p':
        for i in range (len(ans)):
            enter.append(deshow(ans[i]))
            
        mytype=checkcard(enter)
        out=delcard(enter,mycard)[1]
        if enter==[14]:
            mycard.append(53)
        if enter==[15]:
            mycard.append(54)
        mycard=delcard(enter,mycard)[0]
        print('你：')
        printcard(out)
        print()
        # printcard(drcard)
    else:
        print('你：过')
        print()
        
    if len(mycard)==0:
        flag=1
    
    if flag==0:
        choice=[]
        if mytype[0]<=4:
            i=mytype[0]
        else:
            i=mytype[0]-1
        for choose in permutations(drcard[0:8],i):
            choose=list(choose)
            perm=points(choose)
            if checkcard(perm)[0]==mytype[0] and countcard(perm)>countcard(enter):
                choice.append(choose)
        select=[]
        for x in choice:
            x=countcard(x)
            select.append(x)
        if len(select)>0:
            out=choice[select.index(min(select))]
            drcard=delcard(points(out),drcard)[0]
            print('小贝：')
            printcard(out)
            print()
        else:
            print('小贝：过')
            print()
        
    if len(drcard)==0:
        flag=-1

if flag==1:
    print('你赢了！')
if flag==-1:
    print('你输了。')


    
            
            
        
        
        
        
    