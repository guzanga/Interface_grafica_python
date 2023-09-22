import customtkinter as Tk

Tk .set_appearance_mode("Dark")
janela = Tk.CTk()
janela.title("Janela 1")
janela.geometry("650x550")
janela.configure(fg_color="LightCyan")
janela.resizable(width=False, height=False)

colunas = list(range(12))
linhas = list(range(12))
janela.grid_columnconfigure(colunas, weight = 1)
janela.grid_rowconfigure(linhas, weight = 1)

text1 = Tk.CTkLabel(janela, text = "Digite em cada input um numero e descubra qual é o maior",  text_color = "black",  font = ("Arial", 20))
text1.grid(row = 4, column = 6)

inp1 = Tk.CTkEntry(janela, placeholder_text="Digite o primeiro numero", placeholder_text_color="white" , width=200, height=30)
inp1.grid (row=5, column=6)

inp2 = Tk.CTkEntry(janela, placeholder_text="Digite o segundo numero", placeholder_text_color="white" , width=200, height=30)
inp2.grid (row=6, column=6)

def clique():
    num1 = int(inp1.get())
    num2 = int(inp2.get()) 
    if num1 > num2:
        text2.configure(text =f"este é o maior numero: {num1}")
        
    else:
        text2.configure(text = f"este é o maior numero: {num2}")
        
        
button = Tk.CTkButton(janela, text="Verificar", command=clique, height= 40, width= 80, hover_color = "green")
button.grid (row=7, column=6)

text2 = Tk.CTkLabel(janela, text = "",  text_color = "black",  font = ("Arial", 20))
text2.grid(row = 8, column = 6)

janela.mainloop()
