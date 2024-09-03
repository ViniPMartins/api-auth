import requests

API_BASE_URL = "http://127.0.0.1:5001"

# def authenticate():
#     response = requests.post(f"{API_BASE_URL}/login")
#     #print(response.text)
#     print(response.status_code)
#     if response.status_code == 200:
#         return "Requisicao Aceita" #response.json()["access_token"]
#     else:
#         return None
    
# token = authenticate()
token = ".eJw9jlFvgjAURv9LnxcjNG6pbwRjcztxExWwL6ReChYcKFUUzf67zoc9neTLyZdzJwpRW5uemkrXZEx0L3ZbjubLCFjfwJkbsFCHI_ThHapDEvmCDZ7SLYvhT3KQRpitvItcTXsVs1zFCzPzRYlU_CQ07JQbnaFsTMZZK-NRvqHzXu5ZLROxk5zlm2TqqOXz9Lre20IdIAiu3Yy5ovo-ifbTs3oyDGXEy6KjyD-23tANyBtB2-b_0S-mr6nQrcqaVB3Phvw-AO1fTBE.ZteXIQ.pE2mVULJTa6uKwqdn6V8msEzu0k"
print(token)

headers = {
    "Cookie":f"session={token}",
}
response = requests.post(f"{API_BASE_URL}/protected", headers=headers)
print(response.status_code)
print(response.text)