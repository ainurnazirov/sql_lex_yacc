import ply.lex as lex
import re

# список токенов
tokens = ('SQLINSERT', 'SQLFROM', 'SQLVALUES', 'SQLNUM', 'SQLCORRESPONDING', 'SQLBY', 'SQLNAME', 'SQLSTRING',
          'SQLCOLON', 'SQLCOMMA', 'SQLOPEN', 'SQLCLOSE')

# регулярное выражение для абстрактного идетификатора
ident = r'[A-Za-z0-9_]\w*'

# определение токенов
t_SQLINSERT = r'insert into|INSERT INTO'
t_SQLFROM = r'from|FROM'
t_SQLVALUES = r'values|VALUES'
t_SQLCORRESPONDING = r'corresponding|CORRESPONDING'
t_SQLBY = r'by|BY'
t_SQLNAME = ident
t_SQLSTRING = r"\'" + ident + r"'"
t_SQLCOLON = r'\;'
t_SQLCOMMA = r'\,'
t_SQLNUM = r'\d+'
t_SQLOPEN = r'\('
t_SQLCLOSE = r'\)'

# игнорируем незначащие символы
t_ignore = ' \r\n\t\f'


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
