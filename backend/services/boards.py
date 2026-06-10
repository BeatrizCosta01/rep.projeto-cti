import requests

def obter_boards(api_key, token):

    url = "https://api.trello.com/1/members/me/boards"

    resposta = requests.get(
        url,
        params={
            "key": api_key,
            "token": token,
            "fields": "id,name,dateLastActivity"
        }
    )

    return resposta.json()