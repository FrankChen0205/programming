#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:21:08 2023

@author: chenyux
"""
import random
from itertools import permutations

def name(n):
    x=n//10000
    if x==1:
        return 'High Card.'
    if x==2:
        return 'One Pair.'
    if x==3:
        return 'Two Pairs.'
    if x==4:
        return 'Three of a Kind.'
    if x==5:
        return 'Straight.'
    if x==6:
        return 'Flush.'
    if x==7:
        return 'Fullhouse.'
    if x==8:
        return 'Four of a Kind.'
    if x==9:
        return 'Straight Flush.'

def printcard(card):
    n=len(card)
    i=0
    while i<n:
        print("╭───╮",end="")
        i+=1
    print()
    i=0
    while i<n:
        if 2<=card[i]%13<=9:
            print("│ "+str(card[i]%13)+" │",end="")
        if card[i]%13==1:
            print('│ A │',end="")
        if card[i]%13==10:
            print('│ X │',end="")
        if card[i]%13==11:
            print('│ J │',end="")
        if card[i]%13==12:
            print('│ Q │',end="")
        if card[i]%13==0:
            print('│ K │',end="")
        i+=1
    print()
    i=0
    while i<n:
        if (card[i]-1)//13==0:
            print('│ ♦ │',end="")
        if (card[i]-1)//13==1:
            print('│ ♣ │',end="")
        if (card[i]-1)//13==2:
            print('│ ♥ │',end="")
        if (card[i]-1)//13==3:
            print('│ ♠ │',end="")
        i+=1
    print()
    i=0
    while i<n:
        print("╰───╯",end="")
        i+=1
    print()
    
def point(x):
        if x%13==0:
            n=13
        else:
            n=x%13
        return n

def checkcard(card):
    match=[]
    i=0
    while i<len(card):

        i+=1
    for five in permutations(card,5):
        if five[0]==five[1]-1==five[2]-2==five[3]-3==five[4]-5 and five[1] not in [10,11,12,13,23,24,25,26,36,37.38,39]:
            match.append(90000+point(five[0])*100)
            
        elif five[0]%13==five[1]%13==five[2]%13==five[3]%13:
            match.append(80000+point(five[0])*100+point(five[4]))
            
        elif five[0]%13==five[1]%13==five[2]%13 and five[3]%13==five[4]%13:
            match.append(70000+point(five[0])*100+point(five[3]))
            
        elif (five[0]-1)//13==(five[1]-1)//13==(five[2]-1)//13==(five[3]-1)//13==(five[4]-1)//13:
            match.append(60000+point(five[0])*100+point(five[1]))
            
        elif (five[0]-1)%13==(five[1]-1)%13-1==(five[2]-1)%13-2==(five[3]-1)%13-3==(five[4]-1)%13-4:
            match.append(50000+point(five[0])*100)
            
        elif five[0]%13==five[1]%13==five[2]%13:
            match.append(40000+point(five[0])*100+point(five[3]))
            
        elif five[0]%13==five[1]%13 and five[2]%13==five[3]%13:
            match.append(30000+point(five[0])*100+point(five[2]))
        
        elif five[0]%13==five[1]%13:
            match.append(20000+point(five[0])*100+point(five[2]))
        
        else:
            match.append(10000+point(five[0])*100+point(five[1]))
    match.sort()
    return match[-1]

print()
print("Welcome to TEXAS HOLD'EM!")
print()
print("This is Darren, your opponent today.")
print()
print(">> Darren: Hi.")
print()

print("Each of you have $100.")
print()
print("Now, Let The Game Begin!")
print()
mymoney=100
pgmoney=100
r=1
while mymoney>0 and pgmoney>0:
    pile=[]
    flag=0
    i=1
    while i<=52:
        pile.append(i)
        i+=1
    random.shuffle(pile)
    mycard=pile[-3:-1]
    pgcard=pile[-5:-3]
    myhole=pile[-3:-1]
    pghole=pile[-5:-3]
    flop=pile[0:3]
    print('>> Round',r)
    print()
    print('>> Your Hole Cards:')
    printcard(myhole)
    print()
    print(">> Place Your Bets.")
    print("(Tips: f = Fold, [n] = the Bet You Raise to)")
    ans=input("")
    print()
    if ans =='f':
        flag=-1
    else:
        mybet=int(ans)
        print(">> Your Bets: $"+str(mybet))
        print()
    if flag==0:
        while 0==0:
            pgbet=mybet
            decision=random.randint(-1,12)
            if decision<=0:
                print('>> Darren: Fold.')
                flag=-2
                break
            elif decision>8:
                pgbet=mybet
                print('>> Darren: Call.')
                break
            else:
                pgbet+=decision
                print(">> Darren's Bets: $"+str(pgbet))
            print()
            print(">> Your Turn.")
            print("(Tips: f = Fold, c = Call, [n] = the Bet You Raise to)")
            ans=input("")
            print()
            if ans =='f':
                print('You: Fold.')
                flag=-1
                break
            elif ans =='c':
                print('You: Call.')
                mybet=pgbet
                break
            else:
                mybet=int(ans)
                print("Your Bets: $"+str(mybet))
                print()
            
    if flag==0:
        print()
        print('>> Flop:')
        printcard(flop)
        print()
        mycard.append(flop[0])
        mycard.append(flop[1])
        mycard.append(flop[2])
        pgcard.append(flop[0])
        pgcard.append(flop[1])
        pgcard.append(flop[2])
        j=1
        print('(Your Hole Cards)')   
        printcard(myhole)
        while j<=3:
            i=1
            flag=0
            while True:
                print()
                print(">> Your Turn.")
                print("(Tips: f = Fold, c = Call, [n] = the Bet You Raise to, a = All-In)")
                ans=input("")
                print()
                if ans =='f':
                    print('You: Fold.')
                    flag=-1
                elif ans =='c':
                    if i==1:
                        print('You: Call.')
                        mybet=pgbet
                    else:
                        print('You: Call.')
                        mybet=pgbet
                        flag=1
                        break
                elif ans =='a':
                    print('You: All-In.')
                    flag=2
                else:
                    mybet=int(ans)
                    print(">> Your Bets: $"+str(mybet))
                print()
                if flag==1:
                    break
                if flag==2:
                    decision=random.randint(-1,10)
                    if decision<0:
                        flag=3
                    if decision>=0:
                        print('>> Darren: Fold.')
                        flag=-2
                if flag==3:
                    print('>> Darren: All-In.')
                    break
                    
                if flag<0 or flag>1:
                    break
                pgbet=mybet
                decision=random.randint(-1,12)
                if decision<=0:
                    print('>> Darren: Fold.')
                    flag=-2
                    break
                elif decision>10:
                    print('>> Darren: Call.')
                    break
                else:
                    pgbet+=decision
                    print(">> Darren's Bets: $"+str(pgbet))
                i+=1
                
            if flag<0 or flag>1:
                break
            if j==1:
                print()
                print('>> Turn 1:')
                flop.append(pile[3])
                mycard.append(flop[3])
                pgcard.append(flop[3])
                printcard(flop)
                print()
                print('(Your Hole Cards)')
                printcard(myhole)
            if j==2:
                print()
                print('>> Turn 2:')
                flop.append(pile[4])
                mycard.append(flop[4])
                pgcard.append(flop[4])
                printcard(flop)
                print()
                print('(Your Hole Cards)')
                printcard(myhole)
            j+=1
    
    if flag==-1:
        pgmoney+=mybet
        mymoney-=mybet
    elif flag==-2:
        pgmoney-=mybet
        mymoney+=mybet   
    else:
        if checkcard(mycard)>=checkcard(pgcard):
            
            if flag==0 or flag==1:
                mymoney+=mybet
                pgmoney-=mybet
            else:
                mymoney+=pgmoney
                pgmoney=0
        if checkcard(mycard)<checkcard(pgcard):
            if flag==0 or flag==1:
                mymoney-=mybet
                pgmoney+=mybet
            else:
                mymoney=0
                pgmoney+=mymoney
        print()
        print(">> Darren's Cards: "+name(checkcard(pgcard)))
        printcard(pghole)
        print()
        print('>> Your Cards: '+name(checkcard(mycard)))
        printcard(myhole)
    if pgmoney<=0:
        pgmoney=0
        mymoney=200
    if mymoney==0:
        mymoney=0
        pgmoney=200
    print()
    print(">> Your Money: $"+str(mymoney))
    print()
    print(">> Darren's Money: $"+str(pgmoney))
    print()
    r+=1
if pgmoney==0:
    print('>> You Win!')
if mymoney==0:
    print('>> You Lose.')
                
