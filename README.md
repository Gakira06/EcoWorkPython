Este é um ótimo exemplo\! Ele utiliza Markdown avançado, emblemas (badges), e uma estrutura clara e atraente.

Como seu projeto é um **Sistema de Console em Python** (não IoT com ESP32), vou adaptar o README para focar nas funcionalidades de software (menu, validações, dicionários) e na proposta de valor de **Gestão de Sustentabilidade** dentro do contexto do seu código.

Aqui está o README responsivo, adaptado e completo para o seu projeto **Sistema de Gestão EcoWork**:

-----

# 📊💡 Sistema de Gestão EcoWork

**Tagline:** *A visibilidade que sua empresa precisa para transformar consumo de energia em sustentabilidade e produtividade.*

<p align="center">
<img src="[https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Python-3776AB%3Fstyle%3Dfor-the-badge%26logo%3Dpython%26logoColor%3Dwhite)" alt="Linguagem Python" />
<img src="[https://img.shields.io/badge/Console%20Application-lightgrey?style=for-the-badge\&logo=terminal\&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/Console%2520Application-lightgrey%3Fstyle%3Dfor-the-badge%26logo%3Dterminal%26logoColor%3Dwhite)" alt="Aplicação de Console" />
<img src="[https://img.shields.io/badge/Data%20Structure-Dictionary-blue?style=for-the-badge](https://www.google.com/search?q=https://img.shields.io/badge/Data%2520Structure-Dictionary-blue%3Fstyle%3Dfor-the-badge)" alt="Dicionários Python" />
<img src="[https://img.shields.io/badge/Usability-4.5%2F5.0-green?style=for-the-badge](https://www.google.com/search?q=https://img.shields.io/badge/Usability-4.5%252F5.0-green%3Fstyle%3Dfor-the-badge)" alt="Usabilidade Alta" />
<img src="[https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge\&logo=youtube\&logoColor=white](https://www.google.com/search?q=https://img.shields.io/badge/YouTube-FF0000%3Fstyle%3Dfor-the-badge%26logo%3Dyoutube%26logoColor%3Dwhite)" alt="Vídeo no YouTube" />
</p>

-----

## 📖 Sobre o Projeto: Gestão da Pegada de Carbono Individual

O **Sistema de Gestão EcoWork** é uma aplicação de console desenvolvida em **Python** para atender aos requisitos da **Global Solution** da FIAP. Seu objetivo é simular a gestão e o monitoramento do consumo de energia elétrica **(kWh)**, focando na sustentabilidade e na otimização de recursos no ambiente de trabalho.

### O Problema:

Em um cenário onde a responsabilidade ambiental (ESG) é crucial, as empresas precisam de ferramentas para medir e incentivar o uso consciente de energia. A dificuldade reside em **individualizar o consumo** e transformá-lo em dados acionáveis.

### A Solução:

O EcoWork simula a coleta de dados de **"EcoWork Hubs"** (dispositivos de medição de energia) associados a cada funcionário. O sistema centraliza a entrada de dados, realiza cálculos e gera relatórios que permitem à gestão:

1.  **Medir:** Obter o consumo exato por colaborador.
2.  **Gerenciar:** Promover campanhas de economia e identificar *gargalos* de consumo.
3.  **Premiar:** Reconhecer os colaboradores com o menor consumo.

[Image of a person analyzing energy consumption data on a computer]

-----

## ✨ Funcionalidades e Requisitos Técnicos

O projeto foi construído para demonstrar a aplicação correta das principais estruturas de programação em Python, garantindo a funcionalidade e a boa experiência do usuário.

### ⚙️ Funcionalidades de Negócio

  * **1. Cadastrar Novo Funcionário:** Permite adicionar novos colaboradores (`RM`, `Nome`, `Departamento`, `ID Hub`) à base de dados.
  * **2. Registrar Consumo de Energia (kWh):** Adiciona um valor incremental de consumo ao registro de um funcionário específico.
  * **3. Listar Funcionários:** Exibe todos os dados (incluindo o consumo acumulado) de todos os colaboradores cadastrados.
  * **4. Gerar Relatório de Consumo:** Calcula e exibe estatísticas vitais:
      * **Consumo TOTAL** da empresa.
      * **Consumo MÉDIO** por funcionário.
      * Identificação do funcionário de **Maior Consumo** (o "campeão" de energia).

### 🧱 Estruturas de Programação Aplicadas

| Requisito do Projeto | Implementação e Destaque no Código |
| :--- | :--- |
| **Base de Dados** | Utilização de um **Dicionário Global (`db_funcionarios`)** para simular um banco de dados em memória, onde o **RM** é a chave primária. |
| **Funções Modulares** | Funções como `cadastrar_funcionario` e `gerar_relatorio` organizam o fluxo. A função `calcular_totais` demonstra **funções com retorno (`Tuple`)** e **passagem de parâmetros**. |
| **Validação e Exceção** | Funções de utilidade como `solicitar_opcao_int()` e `solicitar_float_positivo()` utilizam **`try-except ValueError`** e **loops (`while`)** para garantir que a entrada do usuário seja sempre válida e não quebre o sistema. |
| **Menu e Fluxo** | Estrutura de menu com **repetição (`while True`)** para manter o sistema rodando e **decisão (`if/elif`)** para direcionar o usuário para as funcionalidades. |

-----

## 🐍 Como Executar o Sistema

Para rodar a aplicação, você só precisa ter o Python instalado em sua máquina.

### Pré-requisitos

  * **Python 3.x**
  * **Nenhuma biblioteca externa** é necessária, apenas bibliotecas nativas (`typing`).

### 🚀 Passos para Execução

1.  **Baixe o Código:** Obtenha o arquivo `main.py` (ou o nome do seu arquivo Python).

2.  **Abra o Terminal/Prompt:** Navegue até a pasta onde o arquivo foi salvo.

3.  **Execute o Script:** Use o comando abaixo:

    ```bash
    python main.py
    ```

4.  O menu do **Sistema de Gestão EcoWork** será exibido, e você poderá começar a cadastrar e registrar dados\!

-----

## 📺 Demonstração em Vídeo

Assista ao vídeo para ver o sistema em funcionamento, desde o cadastro de um novo funcionário até a geração do relatório de consumo, e confira o código sendo explicado:

[](https://youtu.be/O8Gxjsm-vco)

**Link do Vídeo:** `https://youtu.be/O8Gxjsm-vco`

-----

## 👨‍💻 Desenvolvedores

Este projeto foi desenvolvido pelos seguintes alunos da FIAP (1ESPJ):

| Nome | RM | GitHub |
| :--- | :--- | :--- |
| **Gustavo Santos** | 561820 | [Link do GitHub](https://www.google.com/search?q=https://github.com/Seu-User-Gustavo) |
| **Gabriel Akira** | 565191 | [Gakira06](https://github.com/Gakira06) |
| **Mauro Carlos** | 556645 | [Link do GitHub](https://www.google.com/search?q=https://github.com/Seu-User-Mauro) |

-----

## 📄 Licença

Este projeto é de natureza acadêmica, desenvolvido para a Global Solution da FIAP, e está sob uma licença aberta para estudo e demonstração.