# GA4 custom-dimensions API

## 1. Create Google Cloud project
https://console.cloud.google.com/welcome

### Enable API (GCP)
![Alt text](/pix/enableapi.png)
- Google+ API
- Google Analytics API
- Google Analytics Admin API

### Create Credentials (GCP)
- Create API Key
- Setup OAuth consent screen (You will need to enable Google Analytics API minimum scopes - https://www.googleapis.com/auth/analytics and https://www.googleapis.com/auth/analytics.edit)
- Create OAuth 2.0 Client ID (You will need to list the URL https://localhost:8080/callback as a valid redirect URI in your Google APIs Console's project);
- Download Client secret JSON file and rename it to "client_secret.json"

## 2. Get ENV variables
- PROPERTY_ID - GA4 property ID
- API_KEY - API key for your Google Cloud project
- CLIENT_ID - OAuth 2.0 Client ID for your Google Cloud project
- CLIENT_SECRET - OAuth 2.0 Client secret for your Google Cloud project

## 3. Create "variables.env" file
You should create a new file in your project directory and name it "variables.env". In this file, you will store the environment variables in the format VARIABLE_NAME=value, one variable per line. You need to add the following lines with your own values to "variables.env":
```bash
PROPERTY_ID=your_property_id
API_KEY=your_api_key
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
```
Make sure there are no spaces around the = sign, and that each variable is defined on a separate line.

## 3. Create custom dimensions list
You need to update "input_file.xlsx" and list there custom dimensions that need to be created. There are 4 columns in the file:
- "displayName" - a unique name for the dimension;
- "parameterName" - an item parameter when you choose the Item scope or an event parameter when you choose the Event scope or a user property when you choose the User scope;
- "scope" - specifies to which data the custom dimension or metric will be applied; there are 3 possible values: "EVENT" for an event-scoped dimension, "USER" for a user-scoped dimensio and "ITEM" for an item-scoped dimension;
- "description" - an optional text used to identify a custom dimension;
![Alt text](/pix/cdcreate.png)

## 4. Create custom dimensions

### Project setup
Place in your project directory:
- main.py
- utils.py
- client_secret.json
- requirements.txt
- input_file.xlsx
- variables.env

### Setup environment
```bash
#create virtual environment
python -m venv kvenv
#activate virtual environment
source kvenv/bin/activate
#install Python packages 
pip install -r requirements.txt
```

### Run Python code

```bash
python main.py
```
After running the code and inputting variables values, it will open up the authorization URL in a web browser.
![Alt text](/pix/google_accounts.png)

You'll need to authorize the application, which will redirect you to a callback URL and enter the full callback URL in the prompt.