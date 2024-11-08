# -*- coding: utf-8 -*-
"""serp_api.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10NPE16ux4mJG-_OLtgjmNtQ5HC-DApDT
"""

import requests

def fetch_search_results(query, api_key):
    try:
        response = requests.get(
            "https://serpapi.com/search",
            params={"q": query, "api_key": api_key, "engine": "google"}
        )
        result = response.json()
        snippet = result.get("organic_results", [{}])[0].get("snippet", "No snippet available")
        return {"snippet": snippet}
    except Exception as e:
        return {"Error": str(e)}