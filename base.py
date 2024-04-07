import os
import streamlit as st
from PIL import Image

class Base:
    def __init__(self, page_title, page_icon=None):
        self.page_title = page_title
        self.page_icon   = page_icon
        self.max_width()
    
    def max_width(self):
        st.set_page_config(layout     = "wide",
                           page_title = self.page_title,
                           page_icon  = self.page_icon
                          )

    def load_image(self, path):
        if os.path.exists(path):
            image = Image.open(path)
            image.resize((1000,1000))
            return image
        else:
            st.error(f"Error loading image from {path}")

