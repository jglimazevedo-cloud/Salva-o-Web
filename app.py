import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA E ESTILO "DIVINDADE"
st.set_page_config(page_title="Salvação Web", page_icon="✨", layout="wide")

# CSS para o tom de divindade, luz no mouse e esconder o administrador
st.markdown("""
    <style>
    /* Fundo e texto */
    .main { background: radial-gradient(circle, #ffffff 0%, #e0e0e0 100%); color: #2c3e50; }
    
    /* Efeito de luz seguindo o mouse (aproximação visual) */
    html, body, [data-testid="stAppViewContainer"] {
        cursor: url('https://cursors-4u.net'), auto;
    }
    
    /* Design das matérias */
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; white-space: pre-wrap; background-color: #f8f9fa;
        border-radius: 10px; border: 1px solid #ddd; padding: 10px;
    }
    
    /* Nome do Criador e Site */
    .header-text { text-align: center; font-family: 'Georgia', serif; color: #1a2a6c; }
    </style>
    """, unsafe_allow_html=True)

# 2. CABEÇALHO INOFENSIVO
st.markdown("<h3 class='header-text'>Criador: Chico</h3>", unsafe_allow_html=True)
st.markdown("<h1 class='header-text'>✨ Salvação Web ✨</h1>", unsafe_allow_html=True)

# Campo de Pesquisa abaixo do nome
st.text_input("🔍 Pesquisar no acervo de estudos...", placeholder="Ex: Algoritmos, Genesis...")

st.write("---")

# 3. SISTEMA DE MATÉRIAS (ABAS)
tab1, tab2, tab3 = st.tabs(["💻 Programação em Algoritmo", "🗄️ Banco de Dados: Genesis", "🌐 Programação Web I"])

# Inicializar armazenamento de PDFs "escondido"
if 'biblioteca_oculta' not in st.session_state:
    st.session_state['biblioteca_oculta'] = []

def area_publicacao(materia, professor):
    st.write(f"**Professor:** {professor}")
    st.write("---")
    
    # Campo de upload que parece inofensivo
    arquivo = st.file_uploader(f"Enviar material de apoio para {materia}", type="pdf", key=materia)
    
    if arquivo:
        # Acesso negado padrão para qualquer um
        st.error("❌ Acesso Negado: Você não tem permissão para publicar neste servidor.")
        
        # Entrada secreta para o Administrador (Jesus)
        senha = st.text_input("Autenticação de Autoridade:", type="password", key=f"senha_{materia}")
        
        if senha == "antimatéria100%":
            st.success("✨ Identidade Confirmada. Publicando material no Segredo Absoluto...")
            if arquivo.name not in [p['nome'] for p in st.session_state['biblioteca_oculta']]:
                st.session_state['biblioteca_oculta'].append({"nome": arquivo.name, "materia": materia})
            st.rerun()

with tab1:
    area_publicacao("Programação em Algoritmo", "Rogério")

with tab2:
    area_publicacao("Banco de Dados", "Genesis")

with tab3:
    area_publicacao("Programação Web I", "Sistema Central")

# 4. LISTA DE PDFs PUBLICADOS (Só aparece o que foi salvo)
st.write("---")
st.subheader("📚 Materiais Disponíveis")
if st.session_state['biblioteca_oculta']:
    for doc in st.session_state['biblioteca_oculta']:
        st.write(f"📄 **{doc['nome']}** (Matéria: {doc['materia']})")
else:
    st.write("Nenhum documento público disponível no momento.")

# Créditos de rodapé
st.markdown("<br><p style='text-align: center; color: #999;'>© 2026 Salvação Web - Conhecimento e Divindade</p>", unsafe_allow_html=True)
  
