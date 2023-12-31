import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)
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

content = """
Below you can find some of the apps I've built in Python!
"""
st.subheader(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv('data.csv', sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")