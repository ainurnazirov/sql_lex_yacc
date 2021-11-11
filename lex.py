import ply.lex as lex
import re

# список токенов
tokens = ('SQLINSERT', 'SQLFROM', 'SQLVALUES', 'SQLNUM', 'SQLCORRESPONDING', 'SQLBY', 'SQLNAME', 'SQLSTRING',
          'SQLCOLON', 'SQLCOMMA', 'SQLOPEN', 'SQLCLOSE')

# определение токенов
t_SQLINSERT = r'(i|I)(n|N)(s|S)(e|E)(r|R)(t|T)( )+(i|I)(n|N)(t|T)(o|O)'
t_SQLFROM = r'(F|f)(R|r)(O|o)(M|m)'
t_SQLVALUES = r'(V|v)(A|a)(L|l)(U|u)(E|e)(S|s)'
t_SQLCORRESPONDING = r'(c|C)(o|O)(r|R)(r|R)(e|E)(s|S)(p|P)(o|O)(n|N)(d|D)(i|I)(n|N)(g|G)'
t_SQLBY = r'(b|B)(y|Y)'
t_SQLNAME = r'[A-Za-z_][A-Za-z0-9_]*'
t_SQLSTRING = r"\'\w*\'"
t_SQLCOLON = r'\;'
t_SQLCOMMA = r'\,'
t_SQLNUM = r'\d+'
t_SQLOPEN = r'\('
t_SQLCLOSE = r'\)'

# игнорируем незначащие символы
t_ignore = ' \r\t\f'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# обработка ошибок
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex(reflags=re.UNICODE | re.DOTALL)

# правильный запрос
data = '''
INSERT INTO TestTable(ProductName, Price)
    VALUES ('Computer', 100), ('Keyboard', 20), ('Monitor', 50)
'''

# запрос с ошибкой
# data = '''
# INSERT TestTable ProductName, Price
#     VALUES ('Компьютер', 100), ('Клавиатура', 20), ('Монитор', 50)
# '''

lexer.input(data)

while True:
    tok = lexer.token()  # читаем следующий токен
    if not tok:
        break  # закончились печеньки
    print(tok)
