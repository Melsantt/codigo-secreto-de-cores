# Código Secreto de Cores

Um conversor de cores feito em Python com interface em Tkinter. Você digita uma cor em RGB, HEX ou binário e o programa mostra ela nos três formatos, além de pintar uma amostra na tela pra você ver se é mesmo a cor que esperava.

A ideia surgiu de um exercício simples de conversão de bases numéricas (decimal, hexadecimal e binário) e acabou virando um "laboratório de decodificação", com histórico e botão de copiar.

## O que precisa pra rodar

Só o Python 3. O Tkinter já vem junto na instalação padrão do Windows e do macOS. No Linux às vezes ele vem separado, aí é só instalar:

```
sudo apt install python3-tk
```

Não tem nenhuma biblioteca externa, então não precisa de `pip install`.

## Como usar

Dentro da pasta do projeto:

```
python main.py
```

A janela abre maximizada. A partir daí:

1. Escolha o formato de entrada no menu azul (RGB, HEX ou BIN).
2. Preencha o campo que aparecer.
3. Clique em **DECODIFICAR COR** ou aperte Enter.

O resultado aparece nos três formatos, junto com a amostra da cor. Cada formato tem seu botão de copiar, e o botão **LIMPAR CAMPOS** zera tudo.

As últimas 10 cores ficam guardadas no "Arquivo de cores descobertas", lá embaixo. Clicando em uma delas, os resultados voltam pra tela. Esse histórico só existe enquanto o programa estiver aberto; fechou, perdeu.

### Como digitar cada formato

| Formato | Exemplo | Regra |
|---|---|---|
| RGB | `255` `136` `0` | três números inteiros de 0 a 255, um em cada campo |
| HEX | `#FF8800` ou `ff8800` | seis caracteres hexadecimais, com ou sem `#` |
| BIN | `11111111 10001000 00000000` | três grupos de 8 bits separados por espaço |

No binário os zeros à esquerda são obrigatórios: `1010` não passa, tem que ser `00001010`.

## Como o código está dividido

- **`main.py`** – toda a interface: janela, campos, botões, histórico e a função `converter()`, que junta as peças.
- **`conversoes.py`** – as funções que fazem as contas de verdade (`rgb_para_hex`, `rgb_para_binario`, `hex_para_rgb`, `binario_para_rgb`). Não dependem do Tkinter, então dá pra usar em outro projeto.
- **`validacoes.py`** – confere se o que foi digitado faz sentido antes de converter.
- **`testes.py`** – testes com `unittest` pras conversões e validações.

A lógica sempre passa pelo RGB no meio do caminho: se você digita em HEX, o programa converte pra RGB e, a partir do RGB, gera o HEX e o binário de novo. Isso deixa o código mais simples, porque só existem quatro funções de conversão em vez de seis.

## Testes

```
python testes.py
```

São 8 testes e todos passam. Rode de dentro da pasta do projeto, senão o Python não acha os módulos.
