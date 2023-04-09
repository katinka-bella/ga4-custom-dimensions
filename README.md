# GA4 custom-dimensions API

## Create Google Cloud progect

## Enable API
-
-
-

## Create Credentials (GCP)
- API Key
- OAuth 2.0 Client ID (You will need to list the URL https://developers.google.com/oauthplayground as a valid redirect URI in your Google APIs Console's project; Enable Google Analytics API minimum scopes - https://www.googleapis.com/auth/analytics and https://www.googleapis.com/auth/analytics.edit)

## Create access token

https://developers.google.com/oauthplayground/

## Create custom dimention

### create CD via Python script
```bash
#create virtual environment
python -m venv kvenv
#activate virtual environment
source kvenv/bin/activate
#install Python packages 
pip install -r requirements.txt

```
### create CD via curl fetch
```bash
curl --request POST \
  'https://analyticsadmin.googleapis.com/v1alpha/properties/360045070/customDimensions?key=[YOUR_API_KEY]' \
  --header 'Authorization: Bearer [YOUR_ACCESS_TOKEN]' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{"description":"test13","displayName":"test13","scope":"EVENT","parameterName":"test13"}' \
  --compressed
```
