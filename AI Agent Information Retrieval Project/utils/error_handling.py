# -*- coding: utf-8 -*-
"""error_handling.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10NPE16ux4mJG-_OLtgjmNtQ5HC-DApDT
"""

import streamlit as st

def handle_api_error(error_message):
    """Display error message to the user in the Streamlit app."""
    st.error(f"Error fetching data: {error_message}")