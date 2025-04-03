#! /usr/bin/env python
#coding=utf-8
from py_lex import *
from py_yacc import *
from util import clear_text
from translation import Tran

text=clear_text(open('0.py').read())

# syntax parse
lexer = lex()
parser = yacc()
root=parser.parse(text)
root.print_node(0)

# translation
t=Tran()
t.trans(root)
print(t.v_table)