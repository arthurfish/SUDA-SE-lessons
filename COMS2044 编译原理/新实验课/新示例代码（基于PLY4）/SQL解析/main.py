from ply.lex import lex
from ply.yacc import yacc
import re
from math import *
from node import node

#TOKENS
tokens=('SELECT','FROM','WHERE','NAME')

#DEFINE OF TOKENS
def t_SELECT(t):
    r'SELECT'
    return t

def t_FROM(t):
    r'FROM'
    return t

def t_WHERE(t):
    r'WHERE'
    return t

def t_NAME(t):
    r'[A-Za-z]+|[a-zA-Z_][a-zA-Z0-9_]*|[A-Z]*\.[A-Z]$'
    return t

# IGNORED
t_ignore = " \t"
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# LEX ANALYSIS   
lexer = lex()

#PARSING
def p_query(t):
    '''query :  select'''
    t[0]=t[1]
        
def p_select(t):
    '''select : SELECT list FROM table '''
    t[0]=node('QUERY')
    t[0].add(node('[SELECT]'))
    t[0].add(t[2])
    t[0].add(node('[FROM]'))
    t[0].add(t[4])
    
def p_table(t):
    '''table : NAME'''
    t[0]=node('[TABLE]')
    t[0].add(node(t[1]))

def p_list(t):
    ''' list : '*'
             | NAME'''

    t[0]=node('[FIELD]')
    t[0].add(node(t[1]))

parser = yacc()

query='SELECT key FROM table'

parse=parser.parse(query)
parse.print_node(0)