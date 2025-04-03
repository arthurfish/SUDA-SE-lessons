from ply.lex import lex
from ply.yacc import yacc

# http://www.dalkescientific.com/writings/NBN/parsing_with_ply.html

class Atom(object):
    def __init__(self, symbol, count):
        self.symbol = symbol
        self.count = count

# 词法分析

tokens = (
    "SYMBOL",
    "COUNT"
)

t_SYMBOL = (
    r"C[laroudsemf]?|Os?|N[eaibdpos]?|S[icernbmg]?|P[drmtboau]?|"
    r"H[eofgas]?|A[lrsgutcm]|B[eraik]?|Dy|E[urs]|F[erm]?|G[aed]|"
    r"I[nr]?|Kr?|L[iaur]|M[gnodt]|R[buhenaf]|T[icebmalh]|"
    r"U|V|W|Xe|Yb?|Z[nr]")

def t_COUNT(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))

lexer = lex()

# 语法分析

def p_species_list(p):
    "chemical_equation :  chemical_equation species"
    p[0] = p[1] + [p[2]]

def p_species(p):
    "chemical_equation : species"
    p[0] = [p[1]]

def p_single_species(p):
    """
    species : SYMBOL
    species : SYMBOL COUNT
    """
    if len(p) == 2:
        p[0] = Atom(p[1], 1)
    elif len(p) == 3:
        p[0] = Atom(p[1], p[2])
        
def p_error(p):
    print("Syntax error at '%s'" % p.value)


parser = yacc()

count = 0
for atom in parser.parse("H2SO4"):
    count += atom.count
print(count)