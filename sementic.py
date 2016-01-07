
import ply.yacc as yacc
import AST
from lexical import tokens

precedence = (
    ('left','ADDITION'),
    ('left','MULTIPLICATION'),
)

def p_expression_num ( p ) :
    """expression : NUMBER"""
    p[0] = p[1]


def p_expression_addop ( p ) :
    """expression : expression ADD_OP expression"""
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]


def p_expression_mulop ( p ) :
    """expression : expression MUL_OP expression"""
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_error (p) :
    print("Syntax error in line %d " % p.lineno)
    yacc.errok()


yacc.yacc(outputdir='tmp')


if __name__ == "__main__":
    import sys
    result = yacc.parse(open("input/source-code.txt").read())
    print(result)


