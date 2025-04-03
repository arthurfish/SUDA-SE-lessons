#! /usr/bin/env python
#coding=utf-8
import ply.yacc as yacc
from py_lex import *
from node import node,num_node

# YACC for parsing Python

def simple_node(t,name):
    t[0]=node(name)
    for i in range(1,len(t)):
        t[0].add(node(t[i]))
    return t[0]

def p_program(t):
    '''program : statements'''
    if len(t)==2:
        t[0]=node('[PROGRAM]')
        t[0].add(t[1])
        
def p_statements(t):
    '''statements : statements statement
                  | statement'''
    if len(t)==3:
        t[0]=node('[STATEMENTS]')
        t[0].add(t[1])
        t[0].add(t[2])
    elif len(t)==2:
        t[0]=node('[STATEMENTS]')
        t[0].add(t[1])

def p_statement(t):
    ''' statement : assignment
                  | operation
                  | print'''
    if len(t)==2:
        t[0]=node(['STATEMENT'])
        t[0].add(t[1])
        
def p_assignment(t):
    '''assignment : VARIABLE '=' NUMBER'''
    if len(t)==4:
        t[0]=node('[ASSIGNMENT]')
        t[0].add(node(t[1]))
        t[0].add(node(t[2]))
        t[0].add(num_node(t[3]))
        

def p_operation(t):
    '''operation : VARIABLE '=' VARIABLE '+' VARIABLE
                 | VARIABLE '=' VARIABLE '-' VARIABLE'''
    if len(t)==6:
        t[0]=simple_node(t,'[OPERATION]')
        
def p_print(t):
    '''print : PRINT '(' VARIABLE ')' '''
    if len(t)==5:
        t[0]=simple_node(t,'[PRINT]')
       
def p_error(t):
    print("Syntax error at '%s'" % t.value)

yacc.yacc()
