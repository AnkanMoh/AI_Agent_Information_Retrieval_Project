# -*- coding: utf-8 -*-
"""data_processing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10NPE16ux4mJG-_OLtgjmNtQ5HC-DApDT
"""

import pandas as pd

def load_data(uploaded_file):
    """Load data from an uploaded CSV file."""
    return pd.read_csv(uploaded_file)

def process_google_sheet(google_sheets_url):
    """Load data from a Google Sheets URL."""
    try:
        sheet_data = pd.read_csv(google_sheets_url)
        return sheet_data
    except Exception as e:
        return None