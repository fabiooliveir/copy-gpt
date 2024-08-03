import streamlit as st
from openai import OpenAI

# Configuração da página
st.set_page_config(page_title="Gerador de Copys para Anúncios", page_icon="📈", layout="centered", initial_sidebar_state="auto", menu_items=None)
client = OpenAI(api_key=st.secrets["openai"]["api_key"])

st.title("Gerador de Copys para Anúncios 💬📈")
st.info("Selecione a plataforma e forneça detalhes para gerar copys personalizados.", icon="📃")

# Inicializa o histórico de mensagens
if "messages" not in st.session_state.keys():
    st.session_state.messages = []

# Função para gerar copys com o cliente
def generate_copy(platform, objective, product_name):
    if platform == "Facebook":
        prompt = (f"Crie 5 copys para anúncios do Facebook com no máximo 200 caracteres cada. "
                  f"O objetivo da campanha é '{objective}' e o produto é '{product_name}'.")
        num_copies = 5
    elif platform == "Google Ads":
        prompt = (f"Crie 15 títulos para anúncios do Google Ads com no máximo 30 caracteres cada e "
                  f"4 descrições com no máximo 90 caracteres cada. "
                  f"O objetivo da campanha é '{objective}' e o produto é '{product_name}'.")
        num_copies = 19  # 15 títulos + 4 descrições
    else:
        return "Plataforma não reconhecida."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um especialista em criação de copys para anúncios."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )
    
    # Acessar as mensagens da resposta
    response_message = response.choices[0].message.content
    return response_message

# Seleção da plataforma
platform = st.selectbox("Selecione a plataforma", ["Facebook", "Google Ads"])

# Seleção do objetivo da campanha
objective = st.selectbox(
    "Selecione o objetivo da campanha",
    ["Vendas", "Leads", "Tráfego", "Engajamento", "Reconhecimento de Marca"]
)

# Entrada de nome do produto
product_name = st.text_input("Nome do produto")

# Geração de copys
if st.button("Gerar Copys"):
    if not product_name:
        st.error("Por favor, preencha todos os campos.")
    else:
        with st.spinner("Gerando copys..."):
            response_content = generate_copy(platform, objective, product_name)
            st.subheader("Copys Gerados:")
            st.write(response_content)
