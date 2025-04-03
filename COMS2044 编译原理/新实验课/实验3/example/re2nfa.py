#! /usr/bin/env python
#coding=utf-8


S=[] # Status
ST=[] # temp status
T=0
K=0

input='(ab)*'
n=len(input)

def get_current(input,i):
    return input[i]

def get_next(input,i):
    if i<len(input)-1:
        return input[i+1]
    else:
        return ''
    
def add_to_status(t0,ch,t1):
    S.append((t0,ch,t1))

def check_vocab(ch):
    if ch>='a' and ch<='z':
        return True
    else:
        return False

for i in range(n):
    ch=get_current(input,i)
    sym=get_next(input,i)
    
    if check_vocab(ch)==True:
        if sym=='*':
            add_to_status(T,'eps',K+1)
            add_to_status(K+1,ch,K+1)
            add_to_status(K+1,'eps',K+2)
            K=K+2
            T=K
        else:
            add_to_status(T,ch,K+1)
            K=K+1
            T=K
    
    if ch=='(':
        ST.append(T)
        add_to_status(T,'eps',K+1)
        K=K+1
        T=K
        
    if ch==')':
        if sym!='*':
            pass
        else:
            add_to_status(T,'eps',ST[-1])
            add_to_status(ST[-1],'eps',K+1)
            K=K+1
            T=K
            
            ST.pop()
            
        

for t0,ch,t1 in S:
    print '%s\t[%s]\t%s' %(t0,ch,t1)
        
    
    

