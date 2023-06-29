import requests

def generate_ga4_custom_dimensions(
    property_ids: list,
    custom_dimensions: list,
    access_token: str,
    api_key: str
):

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    for property_id in property_ids:
        url = f'https://analyticsadmin.googleapis.com/v1alpha/properties/{property_id}/customDimensions?key={api_key}'
        print(property_id)
        for item in custom_dimensions:
            data = {
                'description': item.get("description"),
                'displayName': item.get("displayName"),
                'scope': item.get("scope"),
                'parameterName': item.get("parameterName")
            }

            response = requests.post(url, headers=headers, json=data)
            print(response.content)

def get_access_token(
    CLIENT_ID, CLIENT_SECRET, SCOPES, PATH_SECRETS_FILE, REDIRECT_URL
    ):
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow

    # create the flow object
    flow = InstalledAppFlow.from_client_secrets_file(
        PATH_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URL)

    # get authorization URL
    auth_url, _ = flow.authorization_url(access_type='offline')

    # open authorization URL in a web browser and authorize the application
    print("Please go to this URL: {}".format(auth_url))
    authorization_response = input("Enter the full callback URL: ")

    # get the authorization code from the response
    flow.fetch_token(authorization_response=authorization_response)

    # create credentials object from the flow object
    creds = flow.credentials

    return creds.token
