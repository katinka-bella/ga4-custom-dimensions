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


    custom_dimention = [
        {"displayName": "xxx10", "parameterName": "xxx10", "scope": "EVENT", "description": "blala"},
        {"displayName": "xxx11", "parameterName": "xxx11", "scope": "EVENT", "description": "blala"},
        {"displayName": "xxx12", "parameterName": "xxx12", "scope": "EVENT", "description": "blala"},
        {"displayName": "xxx13", "parameterName": "xxx13", "scope": "EVENT", "description": "blala"},
    ]
    
    access_token = utils.get_access_token(CLIENT_ID, CLIENT_SECRET, SCOPES, PATH_SECRETS_FILE, REDIRECT_URL)
    
    utils.generate_ga4_custom_dimenstions(
        PROPERTY_ID, custom_dimention, access_token, API_KEY
    )
