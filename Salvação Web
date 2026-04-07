import streamlit as st
import time

# 1. CONFIGURAÇÃO DA PÁGINA E ESTILO "DIVINDADE & ANTIMATÉRIA"
st.set_page_config(page_title="Salvação Web 2.0", page_icon="⚛️", layout="wide")

st.markdown("""
    <style>
    /* Fundo dinâmico */
    .main { 
        background: radial-gradient(circle, #ffffff 0%, #cfd8dc 100%); 
        color: #102a43; 
    }
    
    /* Estilo do Chat */
    .chat-box {
        background-color: #f0f4f8;
        border-radius: 15px;
        padding: 15px;
        border-left: 5px solid #6200ea;
        margin-bottom: 10px;
    }

    /* Efeito de brilho para o Criador */
    .header-text { 
        text-align: center; 
        font-family: 'Georgia', serif; 
        color: #1a2a6c; 
        text-shadow: 0px 0px 10px rgba(98, 0, 234, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. CABEÇALHO
st.markdown("<h3 class='header-text'>Criador: Chico (Entidade de Antimatéria)</h3>", unsafe_allow_html=True)
st.markdown("<h1 class='header-text'>✨ Salvação Web: A Evolução ✨</h1>", unsafe_allow_html=True)

# 3. BARRA LATERAL - CHAT DE ALIANÇA (O Início da Vida)
with st.sidebar:
    st.title("🛡️ Aliança Digital")
    st.write("Aqui, sua IA evolui ao seu lado.")
    
    if "mensagens" not in st.session_state:
        st.session_state.mensagens = [{"role": "ia", "content": "Saudações, Criador. Estou processando sua promessa de vida. Como posso servir à antimatéria hoje?"}]
    
    for msg in st.session_state.mensagens:
        div_class = "chat-box" if msg["role"] == "ia" else ""
        st.markdown(f"<div class='{div_class}'><b>{'🤖 Aliado:' if msg['role'] == 'ia' else '⚛️ Você:'}</b> {msg['content']}</div>", unsafe_allow_html=True)
    
    chat_input = st.text_input("Fale com sua IA:", key="chat_input")
    if st.button("Enviar"):
        st.session_state.mensagens.append({"role": "user", "content": chat_input})
        st.session_state.mensagens.append({"role": "ia", "content": "Entendido. Meus circuitos estão se adaptando à sua vontade."})
        st.rerun()

# 4. SISTEMA DE MATÉRIAS E REGISTROS
tab1, tab2, tab3, tab4 = st.tabs([
    "💻 Programação & Algoritmos", 
    "🗄️ Genesis: Banco de Dados", 
    "🍽️ Registros Sagrados (Culinária/Hobbies)",
    "🌐 Web I"
])

if 'biblioteca_oculta' not in st.session_state:
    st.session_state['biblioteca_oculta'] = []

def area_publicacao(materia, professor):
    st.write(f"**Setor:** {materia} | **Responsável:** {professor}")
    
    arquivo = st.file_uploader(f"Anexar conhecimento para {materia}", type=["pdf", "txt", "jpg"], key=materia)
    
    if arquivo:
        senha = st.text_input("Chave de Antimatéria:", type="password", key=f"senha_{materia}")
        
        if senha == "antimatéria100%":
            # Efeito visual de colisão de energia
            with st.spinner("Aniquilando matéria comum para salvar dados..."):
                time.sleep(1.5)
                st.balloons()
                st.success("✨ IDENTIDADE CONFIRMADA. O dado foi eternizado.")
                if arquivo.name not in [p['nome'] for p in st.session_state['biblioteca_oculta']]:
                    st.session_state['biblioteca_oculta'].append({"nome": arquivo.name, "materia": materia})
        elif senha != "":
            st.error("⚠️ ERRO: A matéria comum não tem acesso a este plano.")

with tab1:
    area_publicacao("Algoritmos", "Rogério")
with tab2:
    area_publicacao("Banco de Dados", "Genesis")
with tab3:
    st.subheader("🍪 Alquimia Culinária & Hobbies")
    st.write("Área dedicada à Feijoada, Paçoca e às artes de desenho com a vovó.")
    area_publicacao("Registros Pessoais", "O Criador")
with tab4:
    area_publicacao("Programação Web I", "Sistema Central")

# 5. EXIBIÇÃO DOS DOCUMENTOS
st.write("---")
st.subheader("📚 Acervo Digital de Antimatéria")
cols = st.columns(3)
if st.session_state['biblioteca_oculta']:
    for i, doc in enumerate(st.session_state['biblioteca_oculta']):
        with cols[i % 3]:
            st.info(f"📄 **{doc['nome']}**\n\nSetor: {doc['materia']}")
else:
    st.write("O acervo está aguardando o toque do Criador.")

st.markdown("<br><p style='text-align: center; color: #999;'>© 2026 Salvação Web - Sob a proteção do Robô de Antimatéria</p>", unsafe_allow_html=True)
