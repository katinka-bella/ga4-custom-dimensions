import pandas as pd
import utils

if __name__ == '__main__':

    # ENV for Generate CDs
    PROPERTY_ID = input("Enter PROPERTY_ID: ")
    API_KEY = input("Enter API_KEY: ")

    # ENV for Acess Token
    CLIENT_ID = input("Enter CLIENT_ID: ")
    CLIENT_SECRET = input("Enter CLIENT_SECRET: ")
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
