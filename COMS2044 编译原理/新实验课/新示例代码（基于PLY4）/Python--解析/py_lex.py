#! /usr/bin/env python
#coding=utf-8
from ply.lex import lex

# LEX for parsing Python

# Tokens
tokens=('VARIABLE','NUMBER','IF','WHILE','PRINT','DEF','RETURN')

literals=['=','+','-','*','(',')','{','}','<','>'] 

#Define of tokens

def t_NUMBER(t):
    r'[0-9]+'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_IF(t):
    r'if'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_DEF(t):
    r'def'
    return t

def t_RETURN(t):
    r'return'
    return t


def t_VARIABLE(t):
    r'[a-zA-Z]+'
    return t


# Ignored
t_ignore = " \t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    

