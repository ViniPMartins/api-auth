import streamlit as st
import requests

# URL da API (substitua pelo endereço onde a API está rodando)
API_BASE_URL = "http://localhost:8000"

# Função para autenticar e obter o token
def authenticate():
    response = requests.post(f"{API_BASE_URL}/token")
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        st.error("Erro na autenticação.")
        return None

# Função para fazer a requisição à API protegida
def make_protected_request(token):
    headers = {
        "Authorization": f"Bearer {token}",
        "x-csrf-token": "token_csrf_gerado_aqui",  # O mesmo CSRF que está no token
        "Origin": "http://localhost:8501"  # Streamlit origin
    }
    response = requests.post(f"{API_BASE_URL}/api/sua-rota", headers=headers)
    return response

# Interface do Streamlit
st.title("Teste de API Segura")

# Autenticação
st.write("Autenticando...")
token = authenticate()

if token:
    st.success("Autenticado com sucesso!")

    # Botão para fazer a requisição
    if st.button("Fazer Requisição Protegida"):
        response = make_protected_request(token)
        if response.status_code == 200:
            st.success(response.json()["message"])
        else:
            st.error(f"Erro: {response.status_code} - {response.text}")

