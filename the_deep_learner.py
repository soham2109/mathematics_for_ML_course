import os
import streamlit as st


class MainApp:
    def __init__(self):
        self.app()
    
    def app(self):
        st.markdown("<h1 style='text-align: center; color: red;'>thedeeplearners.com</h1>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("""
Guidebook  
----  
""")

if __name__=="__main__":
    app = MainApp()       
