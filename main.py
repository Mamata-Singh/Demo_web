import streamlit as st 
import pandas as pd
st.title("Welcome to ITC Infotech..")
st.header("Let's learn Azure OpenAI with me")
st.code("""for i in range(1,5,1):
                print("hello!Welcome to the world of Cloud...")
        """)
dataset=pd.read_csv("failed_banks.csv")
st.dataframe(dataset)
name=st.text_input("Enter your name : ")
fname=st.text_input("Enter the skills u have")
addr=st.text_area("Enter yor text")
classdata=st.selectbox("Enter your class : ",(1,2,3,4,6,7))
button=st.button("Done")
if button:
    st.markdown(""" 
    Name : {name}
    Skills : {fname}
    Address : {addr}
    Class : {classdata}                                
""")