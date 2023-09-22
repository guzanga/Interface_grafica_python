# chama a biblioteca e da um apelido a ela
import customtkinter as Tk

# importei o mudolo para otmizar meu codigo
from modulo import*

# criei uma janela
# da para ter o Dark e o System
Tk .set_appearance_mode("Dark")

# abstração i=onde eu defini uma classe a um objeto
janela = Tk.CTk()

# titulo da janela
janela.title("Janela 1")

# defini o tamanho de uma ganela
janela.geometry("500x500")

# atribui a cor de interface
janela.configure(fg_color="LightCyan")

# aqui ele limita o tamanho da tela
janela.resizable(width=False, height=False)

# aqui a janela foi divida as a janela em uma tabela de 13 por 13 para auxiliar no posicionamento das coisas na janela
colunas = list(range(12))
linhas = list(range(12))
janela.grid_columnconfigure(colunas, weight = 1)
janela.grid_rowconfigure(linhas, weight = 1)

# ----------------------------------label-----------------------------------------

# aqui é a criação de um label onde eu atribuo onde ele vai ficar, neste  caso na janela, após issoo eu coloco o que vai estar escrito nele e o resto são paramentros opcionais de decoração e etc.
text1 = Tk.CTkLabel(janela, text = "digite algo no input",  text_color = "black",  font = ("Arial", 20))
text1.grid(row = 1, column = 6)


# -----------------------------------Botão------------------------------------------

# aqui eu crie um botão onde ele esta na janela, ele vem com um parametro obrigatorio chamado command onde ele irá executar uma função, por isso eu tive de criar uma  

def clique():
    text1.configure(text = caixa1.get())
 
button = Tk.CTkButton(janela, text="clique-me", command=clique, height= 40, width= 80, hover_color = "green")
button.grid (row=3, column=6)

# ----------------------------------caixa de texto-------------------------------------

# aqui eu foi criado uma cauxa de texto com um placeholder e seu posicionamento para ele foi usado o Entry
caixa1 = Tk.CTkEntry(janela, placeholder_text="digite algo..", placeholder_text_color="white" , width=200, height=30)
caixa1.grid (row=2, column=6)
# aqui eu salvei o que foi escrito na caixa de texto
texto = caixa1.get()

# ----------------------------------CheckBox-------------------------------------

# aqui eu foi criado uma checkbox pode colocar command
check1 = Tk.CTkCheckBox(janela, text="Marque", text_color = "black")
check1.grid (row=4, column=6)

# ----------------------------------switch-------------------------------------

# aqui eu foi criado uma switch pode colocar command
switch = Tk.CTkSwitch(janela, text="marque", text_color = "black" )
switch.grid (row=5, column=6)


# ----------------------------------combobox-------------------------------------

# aqui foi criado uma combobox, nela é possivel colocar um command, alem disso é nescessario criar uma lista para que existam os values
lista =["item1","item2","item3"]
combo = Tk.CTkComboBox(janela, values = lista,height=30, width=100)
combo.set("selecione")
combo.grid (row=6, column=6)

# ----------------------------------Barra de progresso-------------------------------------

# aqui eu foi criado uma barra de progresso, com um botão para aumenta-la
a= 0
def aumento():
    global a
    a+=0.1
    barra_progresso.set(a)

barra_progresso = Tk.CTkProgressBar(janela, progress_color="blue",width=200, height = 10)
barra_progresso.grid (row=7, column=6)
barra_progresso.set(0)

button = Tk.CTkButton(janela, text="clique para aumentar a barra", command=aumento, height= 40, width= 80, hover_color = "red")
button.grid (row=8, column=6)

# ----------------------------------slider-------------------------------------
# aqui eu foi criado um slider
slider = Tk.CTkSlider(janela,width=200,height=15, progress_color="green")
slider.grid (row=9, column=6)
slider.get()

# isso matem a janela aberta, então tudo a ser declarado deve esta acima deste mainloop
janela.mainloop()


