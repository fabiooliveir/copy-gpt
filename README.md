# Gerador de Copys para Anúncios

Um aplicativo de Streamlit para gerar copys personalizados para anúncios do Facebook e Google Ads usando a API do OpenAI.

## Funcionalidades

- Geração de copys para anúncios do Facebook e Google Ads.
- Personalize os copys com base no objetivo da campanha e nome do produto.
- Interface simples e interativa desenvolvida com Streamlit.

## Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/) para a criação da interface web.
- [OpenAI](https://openai.com/) para geração de texto com modelos GPT.

## Pré-requisitos

- Python 3.7 ou superior
- Uma chave de API do OpenAI

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Windows use: venv\Scripts\activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure a chave da API do OpenAI. Crie um arquivo `secrets.toml` na raiz do projeto e adicione a chave da API:

    ```toml
    [openai]
    api_key = "YOUR_API_KEY"
    ```

   Substitua `YOUR_API_KEY` pela sua chave de API do OpenAI.

## Uso

1. Execute o aplicativo Streamlit:

    ```bash
    streamlit run app.py
    ```

2. Acesse o aplicativo em seu navegador em [http://localhost:8501](http://localhost:8501).

3. Selecione a plataforma (Facebook ou Google Ads), o objetivo da campanha e insira o nome do produto para gerar os copys personalizados.

## Contribuição

Sinta-se à vontade para contribuir com melhorias! Abra uma issue ou envie um pull request para compartilhar suas sugestões ou correções.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

