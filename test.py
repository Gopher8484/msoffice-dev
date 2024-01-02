import requests
import os
import random
import string

def get_token():
    headers = {
        'Content-Type':'application/x-www-form-urlencoded'
    }
    
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': os.environ["REFRESH_TOKEN"],
        'client_id': os.environ["CLIENT_ID"],
        'client_secret': os.environ["CLIENT_SECRET"],
        'redirect_uri':'http://localhost:53682/'
    }

    r = requests.post('https://login.microsoftonline.com/common/oauth2/v2.0/token', data=data, headers=headers)
    print(r.text)
    r.raise_for_status()
    access_token = r.json()['access_token']

    return access_token

def main(access_token):
    endpoints = [
        r'https://graph.microsoft.com/v1.0/me/drive/root',
        r'https://graph.microsoft.com/v1.0/me/drive',
        r'https://graph.microsoft.com/v1.0/drive/root',
        r'https://graph.microsoft.com/v1.0/users',
        r'https://graph.microsoft.com/v1.0/me/messages',
        r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules',
        r'https://graph.microsoft.com/v1.0/me/mailFolders/Inbox/messages/delta',
        r'https://graph.microsoft.com/v1.0/me/drive/root/children',
        # r'https://api.powerbi.com/v1.0/myorg/apps',
        r'https://graph.microsoft.com/v1.0/me/mailFolders',
        r'https://graph.microsoft.com/v1.0/me/outlook/masterCategories'
    ]

    headers = {
        'Authorization':access_token,
        'Content-Type':'application/json'
    }

    readme = []
    for endpoint in endpoints:
        try:
            r = requests.get(endpoint, headers=headers)
            print(r.status_code, endpoint)
            r.raise_for_status()
            
            readme.append(f"- [X] {endpoint}")
        except:
            readme.append(f"- [ ] {endpoint}")
    
    with open("README.md", "w") as f:
        f.write("\n".join(readme))
    
    with open("token.txt", "w") as f:
        f.write(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(128)))
            
main(get_token())
