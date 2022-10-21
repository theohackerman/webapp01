# myFirstStreamlitApp.py
#import the libraries
import streamlit as st
from PIL import Image

image01 = Image.open('queen_-_logo__reproducao.jpg')
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Bem vindo, ao trabalho de escola!")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("QUEEN")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("melhor banda ever")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Matheus John e o Ruan são os melhores")

st.subheader("------ **Desenvolvido por: Theo santos silva** -----")

menu = ["Texto_Colunas",
        "Texto_Markdown",
        "Inserir_Figura"]
choice = st.sidebar.selectbox("Menu de Opções",menu)
st.sidebar.write("John e foda em tudo")
    
if choice == "Texto_Colunas":       
    st.subheader("Ruan e o melhor em tudo")
    st.write("Matheus gay")    
    cols01 = st.columns(2)    
    cols01[0].write('Texto da Coluna 01')
    cols01[1].write('Texto da Coluna 02')
elif choice == "eu sou bom em fisica":
    st.subheader("Não sei por quê")
    st.write("Veja a seguir opção de formatação de texto Markdown")
    st.markdown(
    """
    ## *Alguns sites referências*:    
    - [Streamlit: hello world](https://calmcode.io/streamlit/hello-world.html)
    - [:star: Streamlit emoji shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlitapp.com/)
    - [Layouts and Containers](https://docs.streamlit.io/library/api-reference/layout)
   
    ##### CRONOGRAMA
    DIA | CH HORÁRIA | CONTEÚDO
    :---------: | :------: | :-------:
    Dia 1 de 2 | ?h | ? a ?
    Dia 2 de 2 | ?h | ? a ?
    """
    )
elif choice == "Inserir_Figura":
    st.image(image01, width=800, caption='Rótulo da Imagem 01') 
    
