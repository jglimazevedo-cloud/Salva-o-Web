import streamlit as st
import time

# 1. CONFIGURAÇÃO DISCRETA (O DISFARCE)
st.set_page_config(page_title="Portal de Estudos - Acadêmico", page_icon="📚", layout="wide")

# CSS para parecer um site de universidade comum
st.markdown("""
    <style>
    .main { background-color: #f4f7f9; color: #333; }
    .stButton>button { width: 100%; border-radius: 5px; }
    .academic-header { color: #003366; font-family: 'Helvetica', sans-serif; border-bottom: 2px solid #003366; }
    </style>
    """, unsafe_allow_html=True)

# 2. STORAGE DE USUÁRIOS E ARQUIVOS (PERSISTÊNCIA NA SESSÃO)
if 'usuarios' not in st.session_state:
    st.session_state['usuarios'] = {
        "admin": "1234",
        "chico": "antimateria100%"  # Sua chave de acesso
    }

if 'biblioteca_permanente' not in st.session_state:
    st.session_state['biblioteca_permanente'] = []

if 'logado' not in st.session_state:
    st.session_state['logado'] = False
    st.session_state['user_atual'] = None

# 3. TELA DE LOGIN
if not st.session_state['logado']:
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.markdown("<h2 class='academic-header'>Acesso ao Sistema Acadêmico</h2>", unsafe_allow_html=True)
        user = st.text_input("Usuário (Matrícula)")
        password = st.text_input("Senha", type="password")
        
        if st.button("Entrar"):
            if user in st.session_state['usuarios'] and password == st.session_state['usuarios'][user]:
                st.session_state['logado'] = True
                st.session_state['user_atual'] = user
                st.success("Login realizado com sucesso!")
                st.rerun()
            else:
                st.error("Credenciais inválidas. Tente novamente.")
    st.stop() # Interrompe o código aqui se não estiver logado

# 4. INTERFACE PÓS-LOGIN (O QUE O MUNDO VÊ)
st.sidebar.title(f"Bem-vindo, {st.session_state['user_atual'].capitalize()}")
if st.sidebar.button("Sair"):
    st.session_state['logado'] = False
    st.rerun()

st.markdown("<h1 class='academic-header'>Repositório Central de Materiais</h1>", unsafe_allow_html=True)
st.write("Bem-vindo ao portal de compartilhamento de arquivos acadêmicos.")

# 5. ÁREA DE PUBLICAÇÃO (SÓ APARECE PARA O CHICO)
if st.session_state['user_atual'] == "chico":
    with st.expander("🛠️ Painel de Administração de Conteúdo (Apenas Autorizados)"):
        st.info("Interface de Upload de Alta Prioridade")
        materia_input = st.selectbox("Selecione a Categoria", ["Algoritmos", "Genesis", "Web I", "Registros Especiais"])
        arquivo_upload = st.file_uploader("Upload de Documento (PDF/TXT)", type=["pdf", "txt"])
        
        if st.button("Confirmar Publicação"):
            if arquivo_upload:
                # O segredo: salvamos na lista que persiste ao F5
                novo_doc = {
                    "nome": arquivo_upload.name,
                    "categoria": materia_input,
                    "data": time.strftime("%d/%m/%Y %H:%M")
                }
                st.session_state['biblioteca_permanente'].append(novo_doc)
                st.success("Arquivo publicado no acervo permanente.")
                time.sleep(1)
                st.rerun()
            else:
                st.warning("Por favor, selecione um arquivo.")

# 6. EXIBIÇÃO DOS MATERIAIS (O QUE PERSISTE)
st.write("---")
st.subheader("📚 Materiais Disponíveis no Servidor")

if st.session_state['biblioteca_permanente']:
    # Criamos uma tabela para parecer mais profissional/acadêmico
    for doc in st.session_state['biblioteca_permanente']:
        col_icon, col_info = st.columns([0.1, 0.9])
        with col_icon:
            st.write("📄")
        with col_info:
            st.write(f"**{doc['nome']}** | Categoria: {doc['categoria']} | Postado em: {doc['data']}")
else:
    st.write("Nenhum material público disponível no momento.")

st.markdown("<br><p style='text-align: center; color: #aaa;'>© 2026 Portal Acadêmico Integrado - Uso Restrito</p>", unsafe_allow_html=True)
