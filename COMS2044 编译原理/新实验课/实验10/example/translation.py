#! /usr/bin/env python
#coding=utf-8
from __future__ import division

v_table={} # variable table

def update_v_table(name,value):
    v_table[name]=value

def trans(node):
    for c in node.getchildren():
        trans(c)

    # Translation

    # Assignment
    if node.getdata()=='[ASSIGNMENT]': 
        ''' statement : VARIABLE '=' NUMBER'''
        value=node.getchild(2).getvalue()
        node.getchild(0).setvalue(value)
        # update v_table
        update_v_table(node.getchild(0).getdata(),value)
     
    
    # Operation
    elif node.getdata()=='[OPERATION]':
        '''operation : VARIABLE '=' VARIABLE '+' VARIABLE
                     | VARIABLE '=' VARIABLE '-' VARIABLE'''
        arg0=v_table[node.getchild(2).getdata()]
        arg1=v_table[node.getchild(4).getdata()]
        op=node.getchild(3).getdata()
        
        if op=='+':
            value=arg0+arg1
        else:
            value=arg0-arg1
        
        node.getchild(0).setvalue(value)
        # update v_table
        update_v_table(node.getchild(0).getdata(),value)
        
    # Print
    elif node.getdata()=='[PRINT]':
        '''print : PRINT '(' VARIABLE ')' '''
        arg0=v_table[node.getchild(2).getdata()]
        print arg0
   
        
        
            
            
        
        

