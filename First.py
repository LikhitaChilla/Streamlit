import streamlit as st
import pandas as pd
from PIL import Image
st.set_page_config(page_title='BTS',page_icon=':purple-heart:',layout='wide')
# st.text("This is a BTS web page")
# # st.markdown('##This is a markdown title')
# st.write("Hello Army :)")
st.title("We love BTS",anchor='Apress')
input=st.text_input("Enter your bias")
st.write(f"Your bias is {input}")
df=pd.DataFrame({
    'bias':['jk','v','suga','jin','hope','rm','jimin'],
    'song':['my you','love wins all','that that','moon','wonder','wild flower','filter']
})
st.dataframe(df)
st.table(df)
hello=st.button("Buy your bias")
if hello:
    st.write('''Don't you know your bias to not easy to be bought with money but i can display
             your bias picture if you provide me
             ''')
uploaded_file=st.file_uploader("Chose a file",type=['jpg','jpeg','png'])
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption='Uploaded Image',use_column_width=True)
number=st.number_input("Enter a number",min_value=0,max_value=100)
upload=st.file_uploader("Enter a csv file",type=['csv'])
if upload:
    dff=pd.read_csv(upload)
    st.write(dff)

