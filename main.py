import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)
container1 = st.container()

with col1:
    st.image("images/photo.png")

with col2:
    st.title('Mel Simpson')
    content = """ 
    Hi, my name is mel and I am learning python.
    This is some dummy text blabla bla - hope things are going well. I am old now.
    
    I am blonde. 
    """
    st.info(content)

with container1:
    content = """
    Below you can find some of the apps I've built in Python, feel free to contact me!
    """
    st.write(content)

col3, col4 = st.columns(2)

df = pd.read_csv('data.csv', sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])