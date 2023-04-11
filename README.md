# GA4 custom-dimensions API

## 1. Create Google Cloud progect
https://console.cloud.google.com/welcome

## Enable API
![Alt text](/pix/playground.png)

-
-
-

## Create Credentials (GCP)
- API Key
- OAuth 2.0 Client ID (You will need to list the URL https://developers.google.com/oauthplayground as a valid redirect URI in your Google APIs Console's project; Enable Google Analytics API minimum scopes - https://www.googleapis.com/auth/analytics and https://www.googleapis.com/auth/analytics.edit)

## Create access token

## Create custom dimention

### create CD via Python script
```bash
#create virtual environment
python -m venv kvenv
#activate virtual environment
source kvenv/bin/activate
#install Python packages 
pip install -r requirements.txt

