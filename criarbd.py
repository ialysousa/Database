import sqlite3 as lite

con = lite.connect('dados.db')


with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE estoque(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, tipo TEXT, quantidade_total TEXT, quantidade_estoque TEXT, quantidade_emprestada TEXT)")
    cur1 = con.cursor()
    cur1.execute("CREATE TABLE funcionario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, cargo TEXT, itens_emprestados TEXT)")
