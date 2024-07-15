#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 21:50:12 2023

@author: Alephrank
"""

def permutation(i):
    if i==1: a,b,c,d=p,q,r,s
    if i==2: a,b,c,d=p,q,s,r
    if i==3: a,b,c,d=q,p,r,s
    if i==4: a,b,c,d=q,p,s,r
    if i==5: a,b,c,d=p,r,q,s
    if i==6: a,b,c,d=p,s,q,r
    if i==7: a,b,c,d=q,r,p,s
    if i==8: a,b,c,d=q,s,p,r
    if i==9: a,b,c,d=p,r,s,q
    if i==10: a,b,c,d=p,s,r,q
    if i==11: a,b,c,d=q,r,s,p
    if i==12: a,b,c,d=q,s,r,p
    if i==13: a,b,c,d=r,p,q,s
    if i==14: a,b,c,d=s,p,q,r
    if i==15: a,b,c,d=r,q,p,s
    if i==16: a,b,c,d=s,q,p,r
    if i==17: a,b,c,d=r,p,s,q
    if i==18: a,b,c,d=s,p,r,q
    if i==19: a,b,c,d=r,q,s,p
    if i==20: a,b,c,d=s,q,r,p
    if i==21: a,b,c,d=s,r,p,q
    if i==22: a,b,c,d=r,s,p,q
    if i==23: a,b,c,d=s,r,q,p
    if i==24: a,b,c,d=r,s,q,p
    return a,b,c,d

p,q,r,s=input("Please enter 4 positive integers.").split(",")
p=int(p)
q=int(q)
r=int(r)
s=int(s)
ans=set()
i=1
while i<=3:
    if i==1: a,b,c,d=p,q,r,s
    if i==2: a,b,c,d=p,r,q,s
    if i==3: a,b,c,d=p,s,q,r
    op1=1
    while op1<=4:
        if op1==1:
            e=a+b;sg1="+"
            if a>b: a,b=b,a
        if op1==2:
            if a>=b: e=a-b
            if a<b: a,b=b,a; e=a-b
            sg1="-"
        if op1==3:  e=a*b;sg1="×"
        if op1==4 and a!=0 and b!=0:
            if a>=b: e=a/b
            if a<b: a,b=b,a; e=a/b
            sg1="÷"
        op2=1
        while op2<=4:
            if op2==1:
                f=c+d;sg2="+"
                if c>d: c,d=d,c
            if op2==2:  
                if c>=d:f=c-d
                if c<d:c,d=d,c; f=c-d
                sg2="-"
            if op2==3:  f=c*d;sg2="×"
            if op2==4 and d!=0:
                if c>=d: f=c/d
                if c<d: c,d=d,c; f=c/d
                sg2="÷"
            op3=1
            while op3<=4:
                if op3==1:  g=e+f;sg3="+"
                if op3==2:  
                    if e>=f: g=e-f
                    if e<f: e,f=f,e; sg1,sg2=sg2,sg1; a,b,c,d=c,d,a,b; g=e-f
                    sg3="-"
                if op3==3:  g=e*f;sg3="×"
                if op3==4 and e!=0 and f!=0:
                    if e>=f: g=e/f
                    if e<f: e,f=f,e; sg1,sg2=sg2,sg1; a,b,c,d=c,d,a,b; g=e/f
                    sg3="÷"
                if g==24:
                    if sg3=="+":
                        ans.add(str(a)+sg1+str(b)+sg3+str(c)+sg2+str(d)+"=24")
                    if sg3=="-":
                        if sg2=="×" or sg2=="÷":
                            ans.add(str(a)+sg1+str(b)+sg3+str(c)+sg2+str(d)+"=24")
                    if sg3=="×" or sg3=="÷":
                        if sg1=="+" or sg1=="-":
                            if sg2=="+" or sg2=="-":
                                ans.add("("+str(a)+sg1+str(b)+")"+sg3+"("+str(c)+sg2+str(d)+")"+"=24")
                        elif sg2=="+" or sg2=="-":
                            ans.add(str(a)+sg1+str(b)+sg3+"("+str(c)+sg2+str(d)+")"+"=24")
                op3+=1
            op2+=1
        op1+=1
    i+=1

i=1
while i<=24:
    a,b,c,d = permutation(i)
    op1=1
    while op1<=4:
        if op1==1:  
            e=a+b;sg1="+"
            if a>b: a,b=b,a
        if op1==2:  e=a-b;sg1="-"
        if op1==3:  
            e=a*b;sg1="×"
            if a>b: a,b=b,a
        if op1==4 and b!=0:  e=a/b;sg1="÷"
        op2=1
        while op2<=4:
            if op2==1:  f=e+c;sg2="+"
            if op2==2:  f=e-c;sg2="-"
            if op2==3:  f=e*c;sg2="×"
            if op2==4 and c!=0:  f=e/c;sg2="÷"
            op3=1
            while op3<=4:
                if op3==1:  g=f+d;sg3="+"
                if op3==2:  g=f-d;sg3="-"
                if op3==3:  g=f*d;sg3="×"
                if op3==4 and d!=0:  g=f/d;sg3="÷"
                if g==24:
                    if (op2==1 or op2==2) and (op3==1 or op3==2):
                        ans.add(str(a)+sg1+str(b)+sg2+str(c)+sg3+str(d)+"=24")
                    if (op1==3 or op1==4) and (op2==3 or op2==4):
                        ans.add(str(a)+sg1+str(b)+sg2+str(c)+sg3+str(d)+"=24")
                    if (op2==1 or op2==2) and (op3==3 or op3==4): 
                        ans.add("("+str(a)+sg1+str(b)+sg2+str(c)+")"+sg3+str(d)+"=24")
                    if (op1==1 or op1==2) and (op2==3 or op2==4): 
                        ans.add("("+str(a)+sg1+str(b)+")"+sg2+str(c)+sg3+str(d)+"=24")
                op3+=1
            op2+=1
        op1+=1
    i+=1

if ans==set():  print("No solutions.")
else:           print(ans)
