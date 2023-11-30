import streamlit as st
import pandas as pd

from PIL import Image 
import pickle

# Datasets:
corpus_info = pd.read_csv("data/corpus_info.csv", index_col='title')
corpus_info = corpus_info.iloc[:,1:]
corpus_content_normal = pd.read_csv('./data/corpus_content_normal.csv', index_col='Unnamed: 0')
corpus_content_normal_10 = corpus_content_normal.iloc[:,:10].copy()
corpus_prueba = corpus_content_normal.loc['Misericordia'].copy()
df = pd.DataFrame({',':0.01,'de':0.01,'.':0.01,'.':0.01,'y':0.01,'que':0.01}, index=['Libro'])

#Modelo:
with open('./data/gbc_streamlit.pickle', 'rb') as gb:
    gbc = pickle.load(gb)

with open('./data/dt2_streamlit.pickle', 'rb') as dt:
    dt2 = pickle.load(dt)


st.set_page_config(page_title="Estilometría")
seleccion = st.sidebar.selectbox("Selecciona menu", ['Home','Jugar con datos'])





if seleccion == "Home":
    st.title("Estilometría")
    st.write("Aplicación para deducir quién ha escrito un texto.\nEn este caso se han comparado veintiuna novelas de Juan Valera, Emilia Pardo Bazán y Benito Pérez Galdós.")

    img = Image.open("data/textos-corpus.png")
    st.image(img)

    st.write('A continuación puedes ver información general del corpus:')
    st.write(corpus_info)

elif seleccion == "Jugar con datos":  
    st.write('En esta tabla puedes ver los datos reales los tokens más usados:')
    st.write(corpus_content_normal.iloc[:,:5])
    st.write('Puedes modificar los datos en esta tabla:')

    df = st.data_editor(df)

    if st.sidebar.button('DTC'):
        st.write('Esta es la predicción:')
        st.write(dt2.predict(df))
        
    if st.sidebar.button('GBC'):
        st.write('Esta es la predicción:')
        st.write(gbc.predict(df))



    