import streamlit as st
st.title("Hey, buddy :sunglasses:")

st.header("This is a test bot :pizza:")

st.subheader("What is your name? ")
#code= '''print("Hello world")'''
#st.code(code , language="python")
st.warning("test test test ",icon="⚠️")

btn_clk=st.button("click")
if btn_clk==True:
    st.subheader("have some :coffee:")
    st.snow()
    st.balloons()
    

