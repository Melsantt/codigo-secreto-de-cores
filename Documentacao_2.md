# CÓDIGO SECRETO DE CORES
**Hackathon de Arquitetura e Organização de Computadores – 2026**

**Tema:** 02 – Código Secreto de Cores  
**Grupo:** GP02  
**Instituição:** Universidade de Cuiabá – UNIC Beira Rio  
**Disciplina:** Arquitetura e Organização de Computadores  
**Professor:** Daniel Cássio

## 1. Problema e objetivo do projeto

O projeto Código Secreto de Cores foi desenvolvido com o objetivo de demonstrar como as cores digitais podem ser representadas e interpretadas por diferentes sistemas numéricos.

A ferramenta permite converter valores entre os formatos RGB decimal, hexadecimal e binário, facilitando a compreensão de como os computadores representam as informações relacionadas às cores.

O sistema também realiza a validação dos valores informados e apresenta visualmente a cor correspondente à conversão.

## 2. Requisitos adotados

O desenvolvimento considerou os seguintes requisitos:

- Converter valores entre RGB, HEX e BIN.
- Permitir conversões entre todos os formatos disponíveis.
- Validar os valores dos canais RGB, respeitando o intervalo de 0 a 255.
- Identificar entradas inválidas nos formatos HEX e BIN.
- Apresentar visualmente a cor resultante.
- Disponibilizar uma interface interativa e de fácil utilização.
- Permitir copiar os resultados das conversões.
- Manter um histórico das conversões realizadas durante a utilização.

## 3. Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento.
- **Tkinter:** biblioteca utilizada para construção da interface gráfica.
- **Unittest:** biblioteca utilizada para execução dos testes automatizados.
- **GitHub:** plataforma destinada ao armazenamento e compartilhamento do código-fonte.
- **IA:** Auxílio na construção do código no quesito funcionamento e interface.

## 4. Funcionamento da solução

O usuário seleciona o formato de entrada desejado e informa os valores correspondentes.

O sistema realiza a validação dos dados, executa a conversão matemática e apresenta os resultados nos demais formatos.

A interface também exibe a representação visual da cor, permitindo relacionar os valores numéricos com o resultado apresentado na tela.

## 5. Fundamentação teórica

O projeto utiliza três sistemas de representação numérica:

**RGB decimal:** representa uma cor por meio de três canais, vermelho, verde e azul. Cada canal possui valores entre 0 e 255.

**Sistema hexadecimal:** utiliza os símbolos de 0 a 9 e de A a F para representar os valores. Cada canal RGB pode ser representado por dois caracteres hexadecimais.

**Sistema binário:** utiliza apenas os algarismos 0 e 1. Cada canal RGB é representado por 8 bits.

Dessa forma, uma cor RGB completa utiliza 24 bits, sendo 8 bits para cada canal.

## 6. Testes e validação

Foram desenvolvidos testes automatizados utilizando a biblioteca Unittest do Python.

Até o momento, foram executados sete testes, todos aprovados.

Os testes realizados verificaram:

1. Conversão das cores primárias.
2. Limites mínimos e máximos dos canais RGB.
3. Conversão de hexadecimal para RGB.
4. Conversão de binário para RGB.
5. Validação de valores RGB.
6. Validação de códigos hexadecimais.
7. Validação de códigos binários.

**Resultado obtido:** sete testes aprovados, sem falhas.

Também foi preparado um teste adicional para verificar outras direções de conversão, cuja execução deverá ser registrada posteriormente.

## 7. Limitações e possibilidades de evolução

O projeto está concentrado nas conversões entre RGB, hexadecimal e binário.

Atualmente, o histórico de conversões é mantido apenas durante a execução do programa, não permanecendo salvo após seu encerramento.

Como possibilidades de evolução, podem ser implementados o armazenamento permanente do histórico, a seleção de cores por meio de uma paleta visual e a exportação dos resultados.

## 8. Declaração de uso de inteligência artificial

Foram utilizadas ferramentas de inteligência artificial como apoio durante o desenvolvimento do projeto, principalmente para esclarecimento de conceitos, auxílio na programação, organização do código, identificação de possíveis erros e elaboração de testes.

As ferramentas foram utilizadas como suporte ao aprendizado e ao desenvolvimento, sendo necessário que os integrantes compreendam o funcionamento da solução e estejam aptos a explicar suas decisões técnicas.

## 9. Integrantes e contribuições

**Grupo:** GP02

**Integrante 1:** [Mel Karolliny]  
**Contribuição:** [Construção do Programa + Roteiro de Defesa.]

**Integrante 2:** [Ygor]  
**Contribuição:** [Construção da documentação + Testes.]

**Integrante 3:** [Anna Bezerra]  
**Contribuição:** [Apresentação.]

**Integrante 4:** [Thiago Matias]  
**Contribuição:** [Apresentação.]

**Integrante 5:** [Daniel]  
**Contribuição:** [Apresentação.]

## 10. Instruções de acesso e execução

Para executar o projeto:

1. Instalar o Python no computador.
2. Baixar ou clonar o repositório do GitHub.
3. Abrir a pasta do projeto no Visual Studio Code.
4. Executar o arquivo principal utilizando o comando:

`python main.py`

Para executar os testes automatizados:

`python testes.py`

Os arquivos necessários são:

- main.py
- conversoes.py
- validacoes.py
- testes.py
