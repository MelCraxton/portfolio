import streamlit as st

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