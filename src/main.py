import pandas as pd
import os
import utils
from dotenv import load_dotenv

if __name__ == '__main__':

    # Load environment variables from .env file
    dotenv_path = os.path.join(os.path.dirname(__file__), 'variables.env')
    load_dotenv(dotenv_path)

    # ENV for Generate CDs
    PROPERTY_ID = os.getenv("PROPERTY_ID")
    API_KEY = os.getenv("API_KEY")

    # ENV for Acess Token
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    SCOPES = [
        "https://www.googleapis.com/auth/analytics", 
        "https://www.googleapis.com/auth/analytics.edit"
    ]
    PATH_SECRETS_FILE = "client_secret.json"
    REDIRECT_URL = "https://localhost:8080/callback"

    # Read the xlsx file into a pandas dataframe
    df = pd.read_excel("input_file.xlsx", sheet_name='Tabelle1')

    # Create a new list of dictionaries with the desired keys
    custom_dimention = []
    for index, row in df.iterrows():
        custom_dimention.append({
            "displayName": row["displayName"] if not pd.isna(row["displayName"]) else "",
            "parameterName": row["parameterName"] if not pd.isna(row["parameterName"]) else "",
            "scope": row["scope"] if not pd.isna(row["scope"]) else "",
            "description": row["description"] if not pd.isna(row["description"]) else ""
        })
        
    access_token = utils.get_access_token(CLIENT_ID, CLIENT_SECRET, SCOPES, PATH_SECRETS_FILE, REDIRECT_URL)
    
    utils.generate_ga4_custom_dimensions(
        PROPERTY_ID, custom_dimention, access_token, API_KEY
    )
