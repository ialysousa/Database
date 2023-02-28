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
janela.geometry('900x600')

janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")


#criando frame

frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)


frameMeio = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

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








janela.mainloop()