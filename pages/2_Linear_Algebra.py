import streamlit as st
from base import Base


class LinAlgPage(Base):
    def __init__(self):
        super().__init__(page_title="Linear Algebra")
        self.app()
    
    def app(self):
        st.markdown("Streamlit page for Linear Algebra")

if __name__=="__main__":
    LinAlgPage()
