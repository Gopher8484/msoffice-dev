import requests
import json
import os

def get_token():
    headers={
        'Content-Type':'application/x-www-form-urlencoded'
    }
    
    data={
        'grant_type': 'refresh_token',
        'refresh_token': os.environ["REFRESH_TOKEN"],
        'client_id': os.environ["CLIENT_ID"],
        'client_secret': os.environ["CLIENT_SECRET"],
        'redirect_uri':'http://localhost:53682/'
    }

    r = requests.post('https://login.microsoftonline.com/common/oauth2/v2.0/token',data=data,headers=headers)
    token_json = r.json()
    access_token = token_json['access_token']

    return access_token

def main(access_token):
    headers={
    'Authorization':access_token,
    'Content-Type':'application/json'
    }
    try:
        requests.get(r'https://graph.microsoft.com/v1.0/me/drive/root', headers=headers)
        requests.get(r'https://graph.microsoft.com/v1.0/me/drive', headers=headers)
        requests.get(r'https://graph.microsoft.com/v1.0/drive/root', headers=headers)
        requests.get(r'https://graph.microsoft.com/v1.0/users', headers=headers)
        requests.get(r'https://graph.microsoft.com/v1.0/me/messages', headers=headers)    
        requests.get(r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules', headers=headers)    
        requests.get(r'https://graph.microsoft.com/v1.0/me/mailFolders/Inbox/messages/delta', headers=headers)
        requests.get(r'https://graph.microsoft.com/v1.0/me/drive/root/children', headers=headers)
        requests.get(r'https://api.powerbi.com/v1.0/myorg/apps', headers=headers) 
        requests.get(r'https://graph.microsoft.com/v1.0/me/mailFolders', headers=headers)
        requests.get(r'https://graph.microsoft.com/v1.0/me/outlook/masterCategories', headers=headers)
    except:
        print("error")
        pass

token = get_token()

for i in range(5):
    main(token)
