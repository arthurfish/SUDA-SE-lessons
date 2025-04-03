#! /usr/bin/env python
#coding=utf-8
import re
from html2pdf import html2pdf 

# parse by regex

def re_find(p,text):
    m=p.findall(text)
    if len(m)==1:
        return m[0]
    else:
        return ''

def re_findall(p,text):
    return p.findall(text)

def clear_text(text):
    lines=[]
    for line in text.split('\n'):
        line=line.strip()
        if len(line)>0:
            lines.append(line)
    return ' '.join(lines)

# 1. read tex file
content=open('example.tex','rb').read()

# 2. extract document part
p_doc=re.compile(r'\\begin{document}(.+?)\\end{document}',re.S)
document=re_find(p_doc,content)


# 3. extract head
p_title=re.compile(r'\\title{(.+?)}',re.S)
title=re_find(p_title,document)

# 4. extract abstract
p_abs=re.compile(r'\\begin{abstract}(.+?)\\end{abstract}',re.S)
abstract=re_find(p_abs,document)
abstract=clear_text(abstract)

# 5. sections
p_sec=re.compile(r'\\section{(.+?)}(.+?)\\section',re.S) # only for Section 1
section_title,section_content=re_find(p_sec,document)
section_content=clear_text(section_content)


# 6. generate html text
html_text=''
# title
html_text+='<h1>%s</h1>\n\n' %title
# abstract
html_text+='<p>%s</p>\n\n' %abstract
# section -- 1
html_text+='<h2>%s</h2>\n\n' %section_title
html_text+='<p>%s</p>\n\n' %section_content

html2pdf(html_text,'2.pdf')