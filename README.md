# AI Agent Information Retrieval Project

## Project Summary
The AI Agent Information Retrieval Project is a Streamlit-based tool designed to help users retrieve specific information about various entities, such as company names or individuals, by performing customized web searches. Users can upload a CSV file or link to a Google Sheet, select a column containing entities, and define a custom query template to search for information. This tool automates the search process, gathers relevant information, and presents the results in a structured format that can be easily downloaded for further analysis.

- **Live Demo**: [Streamlit App](https://ankanmoh-trial-streamlit-wty0rx.streamlit.app/)
- **Video Walkthrough**: [Loom Video](https://www.loom.com/share/02876d5f2ad348339312e1cc01bde1f0?sid=9398bf73-0413-45b4-acf6-f5d5b6186c9d)

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/AI_Agent_Information_Retrieval_Project.git
cd AI_Agent_Information_Retrieval_Project

```

### 2. Install Dependencies
Install the required packages by running:
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the project root to securely store your API keys:
```plaintext
SERPAPI_KEY="your_serpapi_key_here"
```
Replace `"your_serpapi_key_here"` with your actual SerpAPI key.

### 4. Run the Application
To start the Streamlit app, use the following command:
```bash
streamlit run dashboard/main.py
```

## Usage Guide

### Dashboard Overview
The app features a simple and intuitive UI designed for easy use:
1. **Upload Data**: You can upload a CSV file or enter a publicly accessible Google Sheets URL to load your data.
2. **Select Entity Column**: Choose the main column containing the entities (e.g., company names or individual names) to search for.
3. **Custom Query Input**: Define a custom query template, using `{entity}` as a placeholder. For example, "Find contact information for {entity}".
4. **Run Query and View Results**: Click "Run Query" to retrieve data. The app performs searches for each entity and displays results in a table.
5. **Download Results**: You can download the extracted data as a CSV file for further analysis.

### Working Dashboard Features
The following functionalities are built into the dashboard:
- **CSV Upload or Google Sheets Connection**: Allows users to input data from a local file or a Google Sheet.
- **Entity Column Selection**: Lets users choose the primary column for search queries.
- **Custom Prompt Input**: Supports customized prompts for tailored information retrieval.
- **Result Display and Download**: Shows extracted results in a table and enables downloading them as a CSV file.

## Third-Party APIs and Tools

- **SerpAPI**: Used to perform web searches based on custom prompts. SerpAPI enables efficient and programmatic searches, retrieving snippets of relevant information.
- **Streamlit**: Provides the framework for the app’s front-end, enabling an interactive and user-friendly experience.

## Notable Code Implementations

- **Modular Code Structure**: The project is organized into distinct modules, such as `serp_api.py` for API interactions and `data_processing.py` for data handling.
- **Error Handling**: Custom error-handling functions ensure the app notifies users of any data retrieval issues, improving reliability.
- **Environment Variables**: Sensitive data, like API keys, are securely managed using environment variables.

## Video Walkthrough
For a quick 2-minute overview, watch the [Loom Video Walkthrough](https://www.loom.com/share/02876d5f2ad348339312e1cc01bde1f0?sid=9398bf73-0413-45b4-acf6-f5d5b6186c9d), where I explain the project’s purpose, demonstrate key functionalities, and highlight notable code decisions.

## License
This project is licensed under the MIT License.
