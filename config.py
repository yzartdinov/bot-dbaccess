import requests

# REST API

# https://directline.botframework.com/v3/directline/tokens/generate
URL_AUTH = ('https://directline.botframework.com/v3/directline/tokens/generate')

# https://directline.botframework.com/v3/directline/tokens/refresh
URL_REFRESH = ('https://directline.botframework.com/v3/directline/tokens/refresh')

# https://dev.botframework.com/
SECRET_KEYS = ('')

header_auth = {'Authorization': 'Bearer ' + SECRET_KEYS}
auth = requests.post(URL_AUTH, headers=header_auth)
#auth_token = auth.json()

if auth.status_code == 200:
    token = auth.json

#header_refresh = {'Authorization': 'Bearer ' + auth_token['token']}
#refresh = requests.post(URL_REFRESH, headers=header_refresh)
#refresh_token = refresh.json()