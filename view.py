import sqlite3 as lite

con = lite.connect('dados.db')

#CRUD (Create, Read, Update, Delete)

#ITENS
#inserir dados


def inserir_itens(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO estoque(nome, tipo, quantidade_total, quantidade_estoque, quantidade_emprestada) VALUES(?,?,?,?,?)"
        cur.execute(query,i)


#atualizar dados

def atualizar_itens(i):
    with con:
        cur = con.cursor()
        query = "UPDATE estoque SET nome=?, tipo=?, quantidade_total=?, quantidade_estoque=?, quantidade_emprestada=? WHERE id=?"
        cur.execute(query,i)


#deletar dados
def deletar_itens(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM estoque WHERE id=?"
        cur.execute(query,i)



#ver dados
  
def ver_dados(): 
    ver_dados = [] 
    with con:
        cur = con.cursor()
        query = "SELECT * FROM estoque"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados        

#print(ver_dados)       


#ver dados individuais
    
def ver_item(id):
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM estoque WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)


            


#FUNCIONARIO

def inserir_funcionarios(i):
    with con:
        cur1 = con.cursor()
        query = "INSERT INTO funcionario(nome, cargo, itens_emprestados) VALUES(?,?,?)"
        cur1.execute(query,i)


#atualizar funcionarios

def atualizar_funcionarios(i):
    with con:
        cur1 = con.cursor()
        query = "UPDATE funcionario SET nome=?, cargo=?, itens_emprestados=? WHERE id=?"
        cur1.execute(query,i)


#deletar funcionarios
def deletar_funcionarios(i):
    with con:
        cur1 = con.cursor()
        query = "DELETE FROM funcionario WHERE id=?"
        cur1.execute(query,i)



#ver funcionarios
  
def ver_funcionarios(): 
    ver_funcionarios = [] 
    with con:
        cur1 = con.cursor()
        query = "SELECT * FROM funcionario"
        cur1.execute(query)

        rows = cur1.fetchall()
        for row in rows:
            ver_funcionarios.append(row)
    return ver_funcionarios        

#print(ver_funcionarios)       


#ver funcionarios individuais
    
def ver_funcionario(id_func):
    ver_funcionarios_individual = []
    with con:
        cur1 = con.cursor()
        query = "SELECT * FROM funcionario WHERE id=?"
        cur1.execute(query, id_func)

        rows = cur1.fetchall()
        for row in rows:
            ver_funcionarios_individual.append(row)



#MANIPULACAO

#emprestar itens
def emprestar_item(id):

    #criar
    with con:
     
     pass   