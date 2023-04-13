# Run GA4 API to generate Custom Dimensions

## Steps
1. Create Google Cloud project
https://console.cloud.google.com/welcome

2. Enable API (GCP)
![Alt text](/pix/enableapi.png)
- Google+ API
- Google Analytics API
- Google Analytics Admin API

3. Create Credentials (GCP)
- Create API Key
- Setup OAuth consent screen (You will need to enable Google Analytics API minimum scopes - https://www.googleapis.com/auth/analytics and https://www.googleapis.com/auth/analytics.edit)
- Create OAuth 2.0 Client ID (You will need to list the URL https://developers.google.com/oauthplayground as a valid redirect URI in your Google APIs Console's project);

4. Go google developer page https://developers.google.com/oauthplayground/

5. Setup OAuth 2.0 configuration
![Alt text](/pix/oauthplay.png)

6. In 'Step 1 Select & authorize APIs', select https://www.googleapis.com/auth/analytics and https://www.googleapis.com/auth/analytics.edit and click "Authorize APIs"
![Alt text](/pix/playground.png)

7. Authorize the application 

![Alt text](/pix/google_accounts.png)

8. Under 'Step 2 Exchange authorization code for tokens'
- Select the check box Auto-refresh the token before it expires
- Click "Exchange authorization code for tokens"

9. Copy the access token that you get using https://developers.google.com/oauthplayground and curl listed below

```bash
# [PROPERTY_ID] - GA4 property ID
# [YOUR_API_KEY] - API key for your Google Cloud project
# [YOUR_ACCESS_TOKEN] - access token from step 8
# [displayName] - a unique name for the dimension;
# [parameterName] - an item parameter when you choose the Item scope or an event parameter when you choose the Event scope or a user property when you choose the User scope;
# [scope] - specifies to which data the custom dimension or metric will be applied; there are 3 possible values: "EVENT" for an event-scoped dimension, "USER" for a user-scoped dimensio and "ITEM" for an item-scoped dimension;
# [description] - an optional text used to identify a custom dimension;

curl --request POST \
  'https://analyticsadmin.googleapis.com/v1alpha/properties/[PROPERTY_ID]/customDimensions?key=[YOUR_API_KEY]' \
  --header 'Authorization: Bearer [YOUR_ACCESS_TOKEN]' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{"description":"test13","[description]":"[displayName]","scope":"[scope]","parameterName":"[parameterName]"}' \
  --compressed

```

![Alt text](/pix/cdcreate.png)

10. Go to terminal and run curl
