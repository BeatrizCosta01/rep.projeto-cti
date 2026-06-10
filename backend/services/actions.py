import requests

def obter_actions(card_id, api_key, token):

    url = f"https://api.trello.com/1/cards/{card_id}/actions"

    resposta = requests.get(
        url,
        params={
            "key": api_key,
            "token": token,
            "filter": "all",
            "limit": 1000
        }
    )

    return resposta.json()