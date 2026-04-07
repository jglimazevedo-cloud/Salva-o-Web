import streamlit as st
import time

# 1. CONFIGURAÇÃO DE DISFARCE ACADÊMICO
st.set_page_config(page_title="Portal Acadêmico - Login Unificado", page_icon="🎓", layout="wide")

# CSS para simular a interface do Google Login
st.markdown("""
    <style>
    .google-btn {
        display: flex; align-items: center; justify-content: center;
        background-color: white; color: #757575; border: 1px solid #ddd;
        padding: 10px; border-radius: 4px; font-family: 'Roboto', sans-serif;
        cursor: pointer; font-weight: 500; margin-bottom: 20px;
    }
    .google-icon { width: 20px; margin-right: 10px; }
    .main { background-color: #ffffff; }
    .stButton>button { background-color: #1a73e8; color: white; border-radius: 4px; }
    </style>
    """, unsafe_allow_html=True)

# 2. PERSISTÊNCIA DE DADOS (O STORAGE)
# Usamos o session_state como nosso banco de dados temporário que resiste ao F5
if 'banco_usuarios' not in st.session_state:
    st.session_state['banco_usuarios'] = {
        "chico@gmail.com": {"nome": "Chico", "status": "Criador"},
        "estudante@gmail.com": {"nome": "Aluno Padrão", "status": "Visitante"}
    }

if 'arquivos_salvos' not in st.session_state:
    st.session_state['arquivos_salvos'] = []

if 'auth_estado' not in st.session_state:
    st.session_state['auth_estado'] = False
    st.session_state['usuario_logado'] = None

# 3. TELA DE LOGIN (ESTILO GOOGLE)
if not st.session_state['auth_estado']:
    col1, col2, col3 = st.columns([1, 1.5, 1])
    
    with col2:
        st.write("")
        st.markdown("<h2 style='text-align: center;'>Fazer login</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Prosseguir para o Portal Acadêmico</p>", unsafe_allow_html=True)
        
        email = st.text_input("E-mail ou telefone")
        senha_secreta = st.text_input("Senha", type="password")
        
        st.markdown("""
            <div class="google-btn">
                <img class="google-icon" src="https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg">
                Entrar com uma conta do Google
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("Próxima"):
            # A lógica de entrada: Se o email estiver na base e a senha for a de antimatéria
            if email in st.session_state['banco_usuarios'] and senha_secreta == "antimateria100%":
                st.session_state['auth_estado'] = True
                st.session_state['usuario_logado'] = email
                st.success("Autenticado via Google Services.")
                time.sleep(1)
                st.rerun()
            else:
                st.error("E-mail ou senha não reconhecidos pelo sistema.")
        
        st.caption("Não é seu computador? Use o modo de navegação privada para fazer login.")
    st.stop()

# 4. PORTAL PÓS-LOGIN (O DISFARCE DE ESTUDOS)
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg", width=30)
st.sidebar.write(f"Conectado como: **{st.session_state['usuario_logado']}**")

if st.sidebar.button("Sair da Conta"):
    st.session_state['auth_estado'] = False
    st.rerun()

st.title("📚 Repositório de Materiais Acadêmicos")

# 5. ÁREA DO CRIADOR (DISCRETA)
if st.session_state['usuario_logado'] == "chico@gmail.com":
    with st.expander("⬆️ Upload de Documentos para o Servidor"):
        materia = st.selectbox("Matéria", ["Programação em Algoritmo", "Banco de Dados: Genesis", "Web I"])
        arquivo = st.file_uploader("Arraste o PDF aqui", type="pdf")
        
        if st.button("Sincronizar com Nuvem"):
            if arquivo:
                # Salvando no storage que resiste ao F5
                novo_item = {
                    "nome": arquivo.name,
                    "materia": materia,
                    "timestamp": time.strftime("%H:%M:%S - %d/%m/%Y")
                }
                st.session_state['arquivos_salvos'].append(novo_item)
                st.toast("Arquivo sincronizado com sucesso!")
                time.sleep(1)
                st.rerun()

# 6. EXIBIÇÃO DOS ARQUIVOS
