import requests

def obter_membros(board_id, api_key, token):

    resposta = requests.get(
        f"https://api.trello.com/1/boards/{board_id}/members",
        params={
            "key": api_key,
            "token": token
        }
    )

    return resposta.json()