from tkinter import*
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk



#cores

co0 = "#2e2d2b" #prata

co1 = "#feffff" #branca

co2 = "#4fa882" #verde

co3 = "#38576b" #valor

co4 = "#403d3d" #letra

co5 = "#e06636" #profit

co6 = "#038cfc" #azul

co7 = "#3fbfb9" 

co8 = "#263238" 

co9 = "#e9edf5" 


#criando janela

janela = Tk()
janela.title('')
janela.geometry('800x2500')

janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")


#criando frame

frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)


frameMeio = Frame(janela, width=1043, height=250, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=350, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

frameBaixo2 = Frame(janela, width=1043, height=350, bg=co1, relief=FLAT)
frameBaixo2.grid(row=3, column=0, pady=0, padx=0, sticky=NSEW)

#Trabalhando no frame cima ----------------

#abrindo imagem
app_img = Image.open('inventory.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=' Estoque Residência', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)


#Trabalhando no frame meio ----------------

#criando entradas
#nome
l_nome = Label(frameMeio, text='Item', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify='left', relief='solid')
e_nome.place(x=130, y=11)

#tipo
l_tipo = Label(frameMeio, text='Tipo', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_tipo.place(x=10, y=40)
e_tipo = Entry(frameMeio, width=30, justify='left', relief='solid')
e_tipo.place(x=130, y=41)

#qtd total
l_qtd_total = Label(frameMeio, text='Qtd Total', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_qtd_total.place(x=10, y=70)
e_qtd_total = Entry(frameMeio, width=30, justify='left', relief='solid')
e_qtd_total.place(x=130, y=71)

#qtd estoque
l_qtd_estoque = Label(frameMeio, text='Qtd Estoque', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_qtd_estoque.place(x=10, y=100)
e_qtd_estoque = Entry(frameMeio, width=30, justify='left', relief='solid')
e_qtd_estoque.place(x=130, y=101)

#qtd emprestada
l_qtd_emprestada = Label(frameMeio, text='Qtd Emprestada', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_qtd_emprestada.place(x=10, y=130)
e_qtd_emprestada = Entry(frameMeio, width=30, justify='left', relief='solid')
e_qtd_emprestada.place(x=130, y=131)

#funcionario
l_funcionario = Label(frameMeio, text='Funcionário', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_funcionario.place(x=10, y=160)
e_funcionario = Entry(frameMeio, width=30, justify='left', relief='solid')
e_funcionario.place(x=130, y=161)

#cargo
l_cargo = Label(frameMeio, text='Cargo', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cargo.place(x=10, y=190)
e_cargo = Entry(frameMeio, width=30, justify='left', relief='solid')
e_cargo.place(x=130, y=191)

#item_emprestado
l_item_emprestado = Label(frameMeio, text='Item Emprestado', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_item_emprestado.place(x=10, y=190)
e_item_emprestado = Entry(frameMeio, width=30, justify='left', relief='solid')
e_item_emprestado.place(x=130, y=191)



#Criando botoes --------

#botao add
app_add = Image.open('add.png')
app_add = app_add.resize((20,20))
app_add = ImageTk.PhotoImage(app_add)

b_add = Button(frameMeio, image= app_add, width=95, text='Add item', compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_add.place(x=330, y=10)


#botao atualizar
app_atualizar = Image.open('atualizar.png')
app_atualizar = app_atualizar.resize((20,20))
app_atualizar = ImageTk.PhotoImage(app_atualizar)

b_atualizar = Button(frameMeio, image= app_atualizar, width=95, text='Atualizar item', compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_atualizar.place(x=330, y=50)


#botao deletar
app_deletar = Image.open('delete.png')
app_deletar = app_deletar.resize((20,20))
app_deletar = ImageTk.PhotoImage(app_deletar)

b_deletar = Button(frameMeio, image= app_deletar, width=95, text='Deletar item', compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_deletar.place(x=330, y=90)



#botao add funcionario
app_add_func = Image.open('add.png')
app_add_func = app_add_func.resize((20,20))
app_add_func = ImageTk.PhotoImage(app_add_func)

b_add_func = Button(frameMeio, image= app_add_func, width=100, text='Add funcionário', compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_add_func.place(x=330, y=155)


#botao add item emprestado
app_item_empr = Image.open('add.png')
app_item_empr = app_item_empr.resize((20,20))
app_item_empr = ImageTk.PhotoImage(app_item_empr)

b_item_empr = Button(frameMeio, image= app_item_empr, width=100, text='Add empréstimo', compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_item_empr.place(x=330, y=185)




# tabela -----------------------------------------------------------

# creating a treeview with dual scrollbars
#tabela itens

tabela_head = ['Id','Nome', 'Tipo','Qtd Total', 'Qtd Estoque', 'Qtd Emprestada']

lista_itens = []

global tree

tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

# vertical scrollbar
vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

# horizontal scrollbar
hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')
frameBaixo.grid_rowconfigure(0, weight=12)

hd=["center","center","center","center","center","center"]
h=[40,150,100,130,130,160]
n=0

for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
    # adjust the column's width to the header string
    tree.column(col, width=h[n],anchor=hd[n])
    n+=1


# inserindo os itens dentro da tabela
for item in lista_itens:
    tree.insert('', 'end', values=item)


quantidade = [8888,88]

for iten in lista_itens:
    quantidade.append(iten[6])

Total_valor = sum(quantidade)
Total_itens = len(quantidade)

#l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
#l_qtd['text'] = Total_itens


#tabela funcionarios
# creating a treeview with dual scrollbars
tabela_head2 = ['Id','Nome', 'Cargo', 'Itens Emprestados']

lista_itens2 = []

global tree2

tree2 = ttk.Treeview(frameBaixo2, selectmode="extended",columns=tabela_head2, show="headings")

# vertical scrollbar
vsb2 = ttk.Scrollbar(frameBaixo2, orient="vertical", command=tree2.yview)

# horizontal scrollbar
hsb2 = ttk.Scrollbar(frameBaixo2, orient="horizontal", command=tree2.xview)

tree2.configure(yscrollcommand=vsb2.set, xscrollcommand=hsb2.set)
tree2.grid(column=0, row=0, sticky='nsew')
vsb2.grid(column=1, row=0, sticky='ns')
hsb2.grid(column=0, row=1, sticky='ew')
frameBaixo2.grid_rowconfigure(0, weight=12)

hd2=["center","center","center","center"]
h2=[40,150,100,160]
n2=0

for col in tabela_head2:
    tree2.heading(col, text=col.title(), anchor=CENTER)
    # adjust the column's width to the header string
    tree2.column(col, width=h[n2],anchor=hd[n2])
    n+=1


# inserindo os itens dentro da tabela
for item in lista_itens:
    tree2.insert('', 'end', values=item)


quantidade2 = [8888,88]

for iten in lista_itens:
    quantidade2.append(iten[6])

Total_valor2 = sum(quantidade)
Total_itens2 = len(quantidade)

janela.mainloop()
