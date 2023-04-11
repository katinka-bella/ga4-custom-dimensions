# Run GA4 API to generate Custom Dimensions

## Steps
1. xx
2. 
3. go google developer page
![Alt text](/pix/playground.png)

4. copy the token and curl

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
https://developers.google.com/oauthplayground/