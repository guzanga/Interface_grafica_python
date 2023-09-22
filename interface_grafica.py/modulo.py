import customtkinter as tk

# criando codigo para reutilzação
# cria janela
def CriarJanelaP(Titulo,Tamanho,Tipo,Redimensionar=False):
    if Tipo ==1:
        janela = tk.CTk()
    elif Tipo ==2:
        janela = tk.CTkToplevel()
    elif Tipo ==3:
        janela = tk.CTkInputDialog()
    janela.title(Titulo)
    janela.geometry(Tamanho)
    if Redimensionar !=False:
        janela.resizable(width=True, height=True)
    else:
        janela.resizable(width=False, height=False)
    colunas = list(range(13))
    linhas = list(range(13))
    janela.grid_columnconfigure(colunas, weight=1)
    janela.grid_rowconfigure(linhas, weight=1)
    return janela

# cria label
def CriarLabel(Local,Texto,Linha,Coluna):
    label = tk.CTkLabel(Local,text=Texto)
    label.grid(row=Linha, column = Coluna)
    return label

# cria input
def CriarCaixaTexto(Local,Largura,Altura,Linha,Coluna,Texto="nada"):
    caixa = tk.CTkEntry(Local,width=Largura,height=Altura)
    caixa.grid(row=Linha, column=Coluna)
    if Texto!="nada":
        caixa.configure(placeholder_text=Texto)
    return caixa
# cria botão
def CriarBotao(Local,Texto,Comando,Largura,Altura,Linha,Coluna):
    btn = tk.CTkButton(Local,text=Texto,command=Comando,width=Largura,height=Altura)
    btn.grid(row=Linha,column=Coluna)
    return btn

# cria CheckBox
def Criarcheckbox(Local,Texto,Linha,Coluna ):
    check = tk.CTkCheckBox(Local,text=Texto)
    check.grid(row=Linha,column=Coluna)
    return check

#  cria Switch
def Criarswitch(Local,Texto,Linha,Coluna ):
    switch = tk.CTkSwitch(Local,text=Texto)
    switch.grid(row=Linha,column=Coluna)
    return switch

#  cria ComboBox
def CriarComboBox(Local,Valores,Largura,Altura,Linha,Coluna):
    combo= tk.CTkComboBox(Local,width=Largura,height=Altura, values=Valores)
    combo.grid(row=Linha,column=Coluna)
    # este set seta a opção como algo indefinido, de forma q o usuario possa selecionar algo depois
    combo.set("selecione")
    return combo

#  cria barra de progresso
def CriarBarraDeProgresso(Local,Largura,Altura,Linha,Coluna):
    barra= tk.CTkProgressBar(Local,width=Largura,height=Altura)
    barra.grid(row=Linha,column=Coluna)
    return barra

#  cria slider
def CriarSlider(Local,Largura,Altura,Linha,Coluna):
    slider= tk.CTkProgressBar(Local,width=Largura,height=Altura)
    slder.grid(row=Linha,column=Coluna)
    return slider