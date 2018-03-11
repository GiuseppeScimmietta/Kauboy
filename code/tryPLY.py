# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'EXPECT_STM',
   'NAME',
)

# Regular expression rules for simple tokens
t_EXPECT_STM    = r'(expect[ \t\f\v]*:)|(expect[ \t\f\v]*\\[\r\n]+[ \t\f\v]*:)'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()



# Test it out
codeTxt = open('example/testMe.py').read()
#codeTxt = data = '''
#3 + 4 * 10
#  + -20 *2
#'''


# Give the lexer some input
lexer.input(codeTxt)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)