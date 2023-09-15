# chama a biblioteca e da um apelido a ela
import customtkinter as Tk

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
text1.grid(row = 6, column = 6)


# -----------------------------------Botão------------------------------------------

# aqui eu crie um botão onde ele esta na janela, ele vem com um parametro obrigatorio chamado command onde ele irá executar uma função, por isso eu tive de criar uma  

def clique():
    text1.configure(text = caixa1.get())
 
button = Tk.CTkButton(janela, text="clique-me", command=clique, height= 40, width= 80, hover_color = "green")
button.grid (row=8, column=6)

# ----------------------------------caixa de texto-------------------------------------

# aqui eu foi criado uma cauxa de testo com um placeholder e seu posicionamento para ele foi usado o Entry
caixa1 = Tk.CTkEntry(janela, placeholder_text="digite algo..", placeholder_text_color="white" , width=200, height=30)
caixa1.grid (row=7, column=6)
# aqui eu salvei o que foi escrito na caixa de texto
texto = caixa1.get()



# isso matem a janela aberta, então tudo a ser declarado deve esta acima deste mainloop
janela.mainloop()


