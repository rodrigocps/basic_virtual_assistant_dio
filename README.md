# Assistente Virtual com Python

> **Nota:** Este projeto foi desenvolvido como parte de um desafio para criar um sistema de assistência virtual inteligente utilizando Processamento de Linguagem Natural (PLN) e bibliotecas de áudio do Python.

## Objetivo

O objetivo principal deste projeto é desenvolver um sistema capaz de interagir com o usuário através de comandos de voz. O fluxo de funcionamento baseia-se em três pilares:

1.  **Ouvir:** Capturar a voz do usuário através do microfone e transformá-la em texto (*Speech-to-Text*).
2.  **Processar:** Identificar comandos específicos na frase transcrita.
3.  **Responder:** Executar a tarefa solicitada e fornecer um feedback auditivo (*Text-to-Speech*).

### Funcionalidades
O assistente é capaz de realizar as seguintes tarefas automatizadas:
* Abrir vídeos no **YouTube**.
* Consultar resumos na **Wikipedia**.
* Localizar farmácias próximas (via Maps).
* Fornecer a **data e hora** atuais.
* Contar piadas (via biblioteca Pyjokes).

---

## Metodologia

O desenvolvimento do projeto seguiu um fluxo de trabalho estruturado para garantir a integração correta das bibliotecas de áudio e processamento.

* **Configuração do Ambiente:** Utilização do **Anaconda** para gerenciamento de ambientes virtuais e pacotes, garantindo a compatibilidade das bibliotecas. O código foi escrito e testado no **VS Code**.
* **Captura de Áudio:** Implementação da biblioteca `SpeechRecognition` para ouvir o microfone e utilizar a API do Google para transcrever o áudio em texto.
* **Lógica de Controle:** Criação de um loop principal (`while`) que analisa o texto transcrito em busca de palavras-chave (ex: "Wikipedia", "YouTube", "Piada").
* **Síntese de Voz:** Utilização da biblioteca `gTTS` (Google Text-to-Speech) para gerar arquivos de áudio MP3 com as respostas do assistente.
* **Reprodução de Áudio:** Implementação do `pygame` para reproduzir as respostas geradas localmente sem a necessidade de players externos.

---

## Tecnologias e Bibliotecas Utilizadas

| Tecnologia / Biblioteca | Tipo | Descrição |
| :--- | :--- | :--- |
| **Python** | Linguagem | Linguagem base do projeto. |
| **Anaconda** | Gerenciador | Utilizado para gerenciar o ambiente virtual e dependências. |
| **VS Code** | IDE | Ambiente de desenvolvimento integrado. |
| **SpeechRecognition** | Biblioteca | Responsável por converter áudio (fala) em texto. |
| **gTTS** | Biblioteca | Google Text-to-Speech, converte texto em arquivos de áudio. |
| **Pygame** | Biblioteca | Utilizada aqui especificamente para reproduzir os arquivos de áudio gerados (mixer). |
| **Wikipedia** | Biblioteca | API para realizar buscas e obter resumos da Wikipedia. |
| **Pyjokes** | Biblioteca | Gerador de piadas aleatórias (*One-liners*). |
| **Webbrowser** | Módulo Nativo | Permite abrir o navegador padrão do sistema em URLs específicas. |
| **Datetime** | Módulo Nativo | Fornece data e hora atuais. |

---

## 🚀 Como Executar

Para rodar este projeto localmente, siga os passos abaixo:

### 1. Pré-requisitos
Certifique-se de ter o **Python** e o **Anaconda** (opcional, mas recomendado) instalados em sua máquina.

### 2. Instalação das Dependências
Abra o seu terminal e instale as bibliotecas necessárias executando o seguinte comando:

```bash
pip install SpeechRecognition gTTS wikipedia pyjokes pygame pyaudio
```

Obs: A instalação do pyaudio pode requerer passos adicionais dependendo do seu sistema operacional (especialmente no Windows ou Linux). Caso encontre erros, verifique a documentação do PyAudio.

### 3. Executando o Assistente
Com as dependências instaladas, execute o script principal:
```bash
app.py
```
