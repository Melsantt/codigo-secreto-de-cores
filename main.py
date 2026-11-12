
import tkinter as tk
from tkinter import TclError

from conversoes import (
    rgb_para_hex,
    rgb_para_binario,
    hex_para_rgb,
    binario_para_rgb
)

from validacoes import (
    validar_rgb,
    validar_hex,
    validar_binario
)


# ==========================================
# CONFIGURAÇÃO DA JANELA
# ==========================================

janela = tk.Tk()
janela.title("Código Secreto de Cores")
janela.geometry("950x900")
janela.minsize(680, 500)
janela.configure(bg="#151521")
janela.resizable(True, True)

try:
    janela.state("zoomed")
except TclError:
    pass


# ==========================================
# IDENTIDADE VISUAL
# ==========================================

FUNDO = "#151521"
CARD = "#202033"
AZUL = "#4169E1"
AZUL_HOVER = "#557BFF"
BRANCO = "#FFFFFF"
CINZA = "#A6A6B8"
CAMPO = "#303047"
VERDE = "#66D9A5"
VERMELHO = "#FF7070"


# ==========================================
# ÁREA DE ROLAGEM
# ==========================================

canvas = tk.Canvas(
    janela,
    bg=FUNDO,
    highlightthickness=0,
    yscrollincrement=1
)

canvas.pack(
    side="left",
    fill="both",
    expand=True
)

barra_rolagem_principal = tk.Scrollbar(
    janela,
    orient="vertical",
    command=canvas.yview
)

barra_rolagem_principal.pack(
    side="right",
    fill="y"
)

canvas.configure(
    yscrollcommand=barra_rolagem_principal.set
)

conteudo = tk.Frame(
    canvas,
    bg=FUNDO
)

janela_conteudo = canvas.create_window(
    (0, 0),
    window=conteudo,
    anchor="nw"
)


def atualizar_area_rolagem(event=None):
    canvas.configure(
        scrollregion=canvas.bbox("all")
    )


def ajustar_largura_conteudo(event):
    canvas.itemconfig(
        janela_conteudo,
        width=event.width
    )

    atualizar_area_rolagem()


conteudo.bind(
    "<Configure>",
    atualizar_area_rolagem
)

canvas.bind(
    "<Configure>",
    ajustar_largura_conteudo
)


# ==========================================
# ROLAGEM PELO MOUSE E TOUCHPAD
# ==========================================

TAG_ROLAGEM = "RolagemGlobal"


def rolar_com_touchpad(event):

    delta = event.delta

    if delta == 0:
        return "break"

    # Rolagem suave para movimentos do touchpad
    if abs(delta) < 120:
        unidades = 1 if delta > 0 else -1

    else:
        unidades = int(delta / 60)

    if unidades != 0:
        canvas.yview_scroll(-unidades, "units")

    return "break"


def rolar_com_mouse_linux(event):

    if event.num == 4:
        canvas.yview_scroll(-1, "units")

    elif event.num == 5:
        canvas.yview_scroll(1, "units")

    return "break"


# IMPORTANTE:
# Associa os eventos à identificação global de rolagem.

janela.bind_class(
    TAG_ROLAGEM,
    "<MouseWheel>",
    rolar_com_touchpad
)

janela.bind_class(
    TAG_ROLAGEM,
    "<Button-4>",
    rolar_com_mouse_linux
)

janela.bind_class(
    TAG_ROLAGEM,
    "<Button-5>",
    rolar_com_mouse_linux
)


def ativar_rolagem(widget):

    tags = widget.bindtags()

    if TAG_ROLAGEM not in tags:
        widget.bindtags(
            (TAG_ROLAGEM,) + tags
        )

    for filho in widget.winfo_children():
        ativar_rolagem(filho)


# ==========================================
# CONTROLE DOS RESULTADOS
# ==========================================

valores_resultado = {
    "RGB": "",
    "HEX": "",
    "BIN": ""
}

historico_cores = []
LIMITE_HISTORICO = 10


# ==========================================
# EFEITOS VISUAIS DOS BOTÕES
# ==========================================

def adicionar_efeito(botao, cor_normal, cor_hover):

    botao.bind(
        "<Enter>",
        lambda event: botao.config(bg=cor_hover)
    )

    botao.bind(
        "<Leave>",
        lambda event: botao.config(bg=cor_normal)
    )


# ==========================================
# FUNÇÃO PARA COPIAR RESULTADOS
# ==========================================

def copiar_resultado(formato_copia):

    texto = valores_resultado[formato_copia]

    if not texto:
        status.config(
            text="Nenhum resultado disponível para copiar.",
            fg=VERMELHO
        )
        return

    try:
        janela.clipboard_clear()
        janela.clipboard_append(texto)

        status.config(
            text=f"{formato_copia} copiado com sucesso!",
            fg=VERDE
        )

    except TclError:
        status.config(
            text="Não foi possível acessar a área de transferência.",
            fg=VERMELHO
        )


# ==========================================
# CABEÇALHO DA INTERFACE
# ==========================================

cabecalho = tk.Frame(
    conteudo,
    bg=FUNDO
)

cabecalho.pack(
    fill="x",
    padx=35,
    pady=(30, 25)
)

# Identificação do laboratório
tk.Label(
    cabecalho,
    text="● SISTEMA DE DECODIFICAÇÃO",
    font=("Arial", 9, "bold"),
    bg=FUNDO,
    fg=VERDE
).pack(anchor="w")

# Nome do projeto
titulo = tk.Label(
    cabecalho,
    text="CÓDIGO SECRETO DE CORES",
    font=("Arial", 24, "bold"),
    bg=FUNDO,
    fg=BRANCO
)

titulo.pack(
    anchor="w",
    pady=(8, 4)
)

# Descrição
subtitulo = tk.Label(
    cabecalho,
    text="LABORATÓRIO DE DECODIFICAÇÃO RGB • HEX • BIN",
    font=("Arial", 10),
    bg=FUNDO,
    fg=CINZA
)

subtitulo.pack(anchor="w")

# Linha decorativa
linha_cabecalho = tk.Frame(
    cabecalho,
    bg=AZUL,
    height=2
)

linha_cabecalho.pack(
    fill="x",
    pady=(18, 0)
)

titulo.pack(pady=(25, 5))


subtitulo = tk.Label(
    conteudo,
    text="LABORATÓRIO DE DECODIFICAÇÃO RGB • HEX • BIN",
    font=("Arial", 10),
    bg=FUNDO,
    fg=CINZA
)

subtitulo.pack(pady=(0, 25))



# ==========================================
# PAINEL DE ENTRADA DE DADOS
# ==========================================

area_principal = tk.Frame(
    conteudo,
    bg=CARD,
    padx=30,
    pady=25,
    highlightthickness=1,
    highlightbackground="#35354D"
)

area_principal.pack(
    padx=35,
    fill="x"
)


# Cabeçalho do painel

cabecalho_entrada = tk.Frame(
    area_principal,
    bg=CARD
)

cabecalho_entrada.pack(fill="x")

tk.Label(
    cabecalho_entrada,
    text="01 / ENTRADA DE DADOS",
    font=("Arial", 12, "bold"),
    bg=CARD,
    fg=BRANCO
).pack(anchor="w")

tk.Label(
    cabecalho_entrada,
    text="Informe os valores que deseja decodificar.",
    font=("Arial", 9),
    bg=CARD,
    fg=CINZA
).pack(anchor="w", pady=(5, 12))


# Linha divisória

tk.Frame(
    area_principal,
    bg="#35354D",
    height=1
).pack(fill="x", pady=(0, 18))


# Seletor de formato

tk.Label(
    area_principal,
    text="FORMATO DE ENTRADA",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=CINZA
).pack(anchor="w", pady=(0, 8))


formato = tk.StringVar(value="RGB")

seletor_formato = tk.OptionMenu(
    area_principal,
    formato,
    "RGB",
    "HEX",
    "BIN"
)

seletor_formato.config(
    bg=AZUL,
    fg=BRANCO,
    activebackground=AZUL_HOVER,
    activeforeground=BRANCO,
    font=("Arial", 11, "bold"),
    width=18,
    relief="flat",
    highlightthickness=0,
    cursor="hand2"
)

seletor_formato["menu"].config(
    bg=CARD,
    fg=BRANCO,
    activebackground=AZUL,
    activeforeground=BRANCO,
    font=("Arial", 10)
)

seletor_formato.pack(
    anchor="w",
    pady=(0, 22)
)


# ==========================================
# CAMPOS RGB
# ==========================================

area_rgb = tk.Frame(
    area_principal,
    bg=CARD
)


def criar_campo_rgb(nome, coluna):

    area_rgb.grid_columnconfigure(
        coluna,
        weight=1
    )

    tk.Label(
        area_rgb,
        text=nome,
        bg=CARD,
        fg=BRANCO,
        font=("Arial", 9, "bold")
    ).grid(
        row=0,
        column=coluna,
        padx=8,
        pady=(0, 9),
        sticky="w"
    )

    campo = tk.Entry(
        area_rgb,
        width=12,
        font=("Arial", 12, "bold"),
        justify="center",
        bg=CAMPO,
        fg=BRANCO,
        insertbackground=BRANCO,
        relief="flat",
        highlightthickness=1,
        highlightbackground="#45455F",
        highlightcolor=AZUL
    )

    campo.grid(
        row=1,
        column=coluna,
        padx=8,
        ipady=10,
        sticky="ew"
    )

    return campo


campo_vermelho = criar_campo_rgb("VERMELHO", 0)
campo_verde = criar_campo_rgb("VERDE", 1)
campo_azul = criar_campo_rgb("AZUL", 2)




# ==========================================
# CAMPO HEX
# ==========================================

rotulo_hex = tk.Label(
    area_principal,
    text="CÓDIGO HEXADECIMAL",
    bg=CARD,
    fg=BRANCO,
    font=("Arial", 9, "bold")
)

campo_hex = tk.Entry(
    area_principal,
    width=30,
    font=("Arial", 12, "bold"),
    justify="center",
    bg=CAMPO,
    fg=BRANCO,
    insertbackground=BRANCO,
    relief="flat",
    highlightthickness=1,
    highlightbackground="#45455F",
    highlightcolor=AZUL
)


# ==========================================
# CAMPO BIN
# ==========================================

rotulo_bin = tk.Label(
    area_principal,
    text="CANAIS BINÁRIOS",
    bg=CARD,
    fg=BRANCO,
    font=("Arial", 9, "bold")
)

campo_bin = tk.Entry(
    area_principal,
    width=42,
    font=("Arial", 11, "bold"),
    justify="center",
    bg=CAMPO,
    fg=BRANCO,
    insertbackground=BRANCO,
    relief="flat",
    highlightthickness=1,
    highlightbackground="#45455F",
    highlightcolor=AZUL
)



# ==========================================
# BOTÕES DE CONVERSÃO E LIMPEZA
# ==========================================

area_botoes = tk.Frame(
    area_principal,
    bg=CARD
)

area_botoes.pack(
    pady=(22, 0)
)


botao_converter = tk.Button(
    area_botoes,
    text="DECODIFICAR COR",
    bg=AZUL,
    fg=BRANCO,
    activebackground=AZUL_HOVER,
    activeforeground=BRANCO,
    font=("Arial", 11, "bold"),
    relief="flat",
    cursor="hand2",
    width=22,
    pady=11
)

botao_converter.grid(
    row=0,
    column=0,
    padx=6
)

adicionar_efeito(
    botao_converter,
    AZUL,
    AZUL_HOVER
)


botao_limpar = tk.Button(
    area_botoes,
    text="LIMPAR CAMPOS",
    bg=CAMPO,
    fg=BRANCO,
    activebackground="#45455F",
    activeforeground=BRANCO,
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2",
    width=18,
    pady=11
)

botao_limpar.grid(
    row=0,
    column=1,
    padx=6
)

adicionar_efeito(
    botao_limpar,
    CAMPO,
    "#45455F"
)


# ==========================================
# RESULTADOS
# ==========================================

area_resultados = tk.Frame(
    conteudo,
    bg=CARD,
    padx=25,
    pady=18
)

area_resultados.pack(
    padx=35,
    pady=15,
    fill="x"
)


tk.Label(
    area_resultados,
    text="RESULTADOS DA DECODIFICAÇÃO",
    font=("Arial", 11, "bold"),
    bg=CARD,
    fg=CINZA
).pack(
    anchor="w",
    pady=(0, 12)
)


resultado_rgb = tk.Label(
    area_resultados,
    text="RGB:",
    font=("Arial", 11),
    bg=CARD,
    fg=BRANCO
)

resultado_rgb.pack(
    anchor="w",
    pady=4
)


resultado_hex = tk.Label(
    area_resultados,
    text="HEX:",
    font=("Arial", 11),
    bg=CARD,
    fg=BRANCO
)

resultado_hex.pack(
    anchor="w",
    pady=4
)


resultado_bin = tk.Label(
    area_resultados,
    text="BIN:",
    font=("Arial", 10),
    bg=CARD,
    fg=BRANCO,
    wraplength=700,
    justify="left"
)

resultado_bin.pack(
    anchor="w",
    pady=4
)


# ==========================================
# BOTÕES PARA COPIAR
# ==========================================

area_copiar = tk.Frame(
    area_resultados,
    bg=CARD
)

area_copiar.pack(
    fill="x",
    pady=(12, 0)
)


def criar_botao_copiar(nome, coluna):

    botao = tk.Button(
        area_copiar,
        text=f"COPIAR {nome}",
        command=lambda: copiar_resultado(nome),
        bg=CAMPO,
        fg=BRANCO,
        activebackground=AZUL_HOVER,
        activeforeground=BRANCO,
        font=("Arial", 9, "bold"),
        relief="flat",
        cursor="hand2",
        width=14,
        pady=8
    )

    botao.grid(
        row=0,
        column=coluna,
        padx=5
    )

    adicionar_efeito(
        botao,
        CAMPO,
        "#45455F"
    )


criar_botao_copiar("RGB", 0)
criar_botao_copiar("HEX", 1)
criar_botao_copiar("BIN", 2)


# ==========================================
# STATUS
# ==========================================

status = tk.Label(
    conteudo,
    text="Aguardando decodificação...",
    font=("Arial", 9),
    bg=FUNDO,
    fg=CINZA
)

status.pack(pady=8)


# ==========================================
# VISUALIZAÇÃO DA COR
# ==========================================

area_visualizacao = tk.Frame(
    conteudo,
    bg=CARD,
    padx=25,
    pady=18
)

area_visualizacao.pack(
    padx=35,
    pady=10,
    fill="x"
)


tk.Label(
    area_visualizacao,
    text="VISUALIZAÇÃO DA COR DECODIFICADA",
    font=("Arial", 11, "bold"),
    bg=CARD,
    fg=CINZA
).pack(
    anchor="w",
    pady=(0, 12)
)


exibicao_cor = tk.Label(
    area_visualizacao,
    text="AGUARDANDO COR...",
    font=("Arial", 15, "bold"),
    bg=CAMPO,
    fg=BRANCO,
    height=5
)

exibicao_cor.pack(
    fill="x",
    pady=(0, 12)
)


tk.Label(
    area_visualizacao,
    text="CÓDIGO HEXADECIMAL",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=CINZA
).pack()


exibicao_hex = tk.Label(
    area_visualizacao,
    text="Nenhuma cor decodificada",
    font=("Consolas", 15, "bold"),
    bg=CARD,
    fg=BRANCO
)

exibicao_hex.pack(pady=(5, 0))


# ==========================================
# HISTÓRICO DE CORES
# ==========================================

area_historico = tk.Frame(
    conteudo,
    bg=CARD,
    padx=20,
    pady=15
)

area_historico.pack(
    padx=35,
    pady=15,
    fill="x"
)


tk.Label(
    area_historico,
    text="ARQUIVO DE CORES DESCOBERTAS",
    font=("Arial", 11, "bold"),
    bg=CARD,
    fg=CINZA
).pack(
    anchor="w",
    pady=(0, 5)
)


tk.Label(
    area_historico,
    text="Selecione uma cor para recuperar seus resultados.",
    font=("Arial", 9),
    bg=CARD,
    fg=CINZA
).pack(
    anchor="w",
    pady=(0, 12)
)


lista_historico = tk.Frame(
    area_historico,
    bg=CARD
)

lista_historico.pack(
    fill="x"
)


# ==========================================
# ATUALIZAR HISTÓRICO VISUAL
# ==========================================

def registrar_historico(rgb, hexadecimal, binario):

    nova_cor = {
        "RGB": rgb,
        "HEX": hexadecimal,
        "BIN": binario
    }

    if historico_cores and historico_cores[0]["HEX"] == hexadecimal:
        return

    historico_cores.insert(0, nova_cor)

    if len(historico_cores) > LIMITE_HISTORICO:
        historico_cores.pop()

    atualizar_historico()


def atualizar_historico():

    for widget in lista_historico.winfo_children():
        widget.destroy()

    for indice, cor in enumerate(historico_cores):

        linha = tk.Frame(
            lista_historico,
            bg=CAMPO,
            padx=10,
            pady=8,
            cursor="hand2"
        )

        linha.pack(
            fill="x",
            pady=3
        )

        amostra = tk.Label(
            linha,
            bg=cor["HEX"],
            width=4,
            height=2
        )

        amostra.pack(
            side="left",
            padx=(0, 12)
        )

        informacoes = tk.Label(
            linha,
            text=f'{cor["HEX"]}    |    RGB: {cor["RGB"]}',
            font=("Consolas", 10),
            bg=CAMPO,
            fg=BRANCO,
            anchor="w"
        )

        informacoes.pack(
            side="left",
            fill="x",
            expand=True
        )

        def selecionar(event, posicao=indice):
            recuperar_cor_historico(posicao)

        for widget in (linha, amostra, informacoes):
            widget.bind("<Button-1>", selecionar)

        # Ativa a rolagem na linha recém-criada
        ativar_rolagem(linha)


# ==========================================
# RECUPERAR COR DO HISTÓRICO
# ==========================================

def recuperar_cor_historico(indice):

    cor = historico_cores[indice]

    valores_resultado["RGB"] = cor["RGB"]
    valores_resultado["HEX"] = cor["HEX"]
    valores_resultado["BIN"] = cor["BIN"]

    resultado_rgb.config(
        text=f'RGB: {cor["RGB"]}'
    )

    resultado_hex.config(
        text=f'HEX: {cor["HEX"]}'
    )

    resultado_bin.config(
        text=f'BIN: {cor["BIN"]}'
    )

    exibicao_cor.config(
        bg=cor["HEX"],
        fg=BRANCO,
        text=cor["HEX"]
    )

    exibicao_hex.config(
        text=cor["HEX"]
    )

    status.config(
        text="Cor recuperada do arquivo de descobertas!",
        fg=VERDE
    )


# ==========================================
# LIMPAR CAMPOS E RESULTADOS
# ==========================================

def limpar_resultados():

    valores_resultado["RGB"] = ""
    valores_resultado["HEX"] = ""
    valores_resultado["BIN"] = ""

    resultado_rgb.config(text="RGB:")
    resultado_hex.config(text="HEX:")
    resultado_bin.config(text="BIN:")

    exibicao_cor.config(
        bg=CAMPO,
        fg=BRANCO,
        text="AGUARDANDO COR..."
    )

    exibicao_hex.config(
        text="Nenhuma cor decodificada"
    )


def limpar_campos():

    campo_vermelho.delete(0, tk.END)
    campo_verde.delete(0, tk.END)
    campo_azul.delete(0, tk.END)

    campo_hex.delete(0, tk.END)
    campo_bin.delete(0, tk.END)

    limpar_resultados()

    status.config(
        text="Campos e resultados limpos!",
        fg=VERDE
    )


botao_limpar.config(
    command=limpar_campos
)


# ==========================================
# MENSAGEM DE ERRO
# ==========================================

def exibir_erro(mensagem):

    limpar_resultados()

    resultado_rgb.config(
        text=mensagem
    )

    status.config(
        text="Verifique os dados informados.",
        fg=VERMELHO
    )


# ==========================================
# FUNÇÃO DE CONVERSÃO
# ==========================================

def converter():

    if formato.get() == "RGB":

        try:

            vermelho = int(campo_vermelho.get())
            verde = int(campo_verde.get())
            azul = int(campo_azul.get())

            if not validar_rgb(vermelho, verde, azul):
                exibir_erro("Valores RGB inválidos.")
                return

        except ValueError:
            exibir_erro("Digite números inteiros válidos.")
            return

    elif formato.get() == "HEX":

        hexadecimal = campo_hex.get().strip()

        if not validar_hex(hexadecimal):
            exibir_erro("Código hexadecimal inválido.")
            return

        vermelho, verde, azul = hex_para_rgb(hexadecimal)

    elif formato.get() == "BIN":

        binario = campo_bin.get().strip()

        if not validar_binario(binario):
            exibir_erro("Código binário inválido.")
            return

        vermelho, verde, azul = binario_para_rgb(binario)

    # Gera todos os formatos

    rgb = f"{vermelho}, {verde}, {azul}"

    hexadecimal = rgb_para_hex(
        vermelho,
        verde,
        azul
    )

    binario = rgb_para_binario(
        vermelho,
        verde,
        azul
    )

    # Armazena os resultados

    valores_resultado["RGB"] = rgb
    valores_resultado["HEX"] = hexadecimal
    valores_resultado["BIN"] = binario

    # Atualiza os resultados

    resultado_rgb.config(
        text=f"RGB: {rgb}"
    )

    resultado_hex.config(
        text=f"HEX: {hexadecimal}"
    )

    resultado_bin.config(
        text=f"BIN: {binario}"
    )

    # Atualiza a visualização

    exibicao_cor.config(
        bg=hexadecimal,
        fg=BRANCO,
        text=hexadecimal
    )

    exibicao_hex.config(
        text=hexadecimal
    )

    # Adiciona ao histórico

    registrar_historico(
        rgb,
        hexadecimal,
        binario
    )

    status.config(
        text="Cor decodificada com sucesso!",
        fg=VERDE
    )


# ==========================================
# ALTERAÇÃO DO FORMATO
# ==========================================

def alterar_formato(*args):

    area_rgb.pack_forget()

    rotulo_hex.pack_forget()
    campo_hex.pack_forget()

    rotulo_bin.pack_forget()
    campo_bin.pack_forget()

    limpar_resultados()

    if formato.get() == "RGB":

        area_rgb.pack(anchor="w")

    elif formato.get() == "HEX":

        rotulo_hex.pack(
            anchor="w",
            pady=(0, 8)
        )

        campo_hex.pack(
            anchor="w",
            ipady=8
        )

    elif formato.get() == "BIN":

        rotulo_bin.pack(
            anchor="w",
            pady=(0, 8)
        )

        campo_bin.pack(
            anchor="w",
            ipady=8
        )

    atualizar_area_rolagem()


# ==========================================
# ATUALIZAÇÃO AUTOMÁTICA
# ==========================================

formato.trace_add(
    "write",
    alterar_formato
)

alterar_formato()


# ==========================================
# ATALHO DA TECLA ENTER
# ==========================================

janela.bind(
    "<Return>",
    lambda event: converter()
)


# ==========================================
# EXECUÇÃO DO PROGRAMA
# ==========================================

# Ativa a rolagem em todos os elementos
ativar_rolagem(janela)

janela.update_idletasks()

canvas.configure(
    scrollregion=canvas.bbox("all")
)

janela.mainloop()
