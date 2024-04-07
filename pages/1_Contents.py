import streamlit as st
from base import Base


class ContentsPage(Base):
    def __init__(self):
        super().__init__(page_title="Contents")
        self.app()
    
    def app(self):
        st.markdown("Welcome the course titled __Mathematical Foundations for Machine Learning__")

if __name__=="__main__":
    ContentsPage()
