# Flask Blog API

Este é um simples API em Flask para um blog, utilizando SQLAlchemy para gerenciamento do banco de dados.

## Sumário

- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Banco de Dados](#estrutura-do-banco-de-dados)
- [Inicialização](#inicialização)
- [Contribuições](#contribuições)
- [Licença](#licença)

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seunome/flask-blog-api.git
    cd flask-blog-api
    ```

2. Crie um ambiente virtual:

    ```bash
    python -m venv venv
    ```

3. Ative o ambiente virtual:

    - No Windows:

        ```bash
        venv\Scripts\activate
        ```

    - No macOS e Linux:

        ```bash
        source venv/bin/activate
        ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Execute a aplicação:

    ```bash
    python app.py
    ```

2. Acesse a API em `http://127.0.0.1:5000/`.

## Estrutura do Banco de Dados

### Tabela Postagem

- `id_postagem`: Inteiro, Chave Primária
- `titulo`: String
- `id_a
