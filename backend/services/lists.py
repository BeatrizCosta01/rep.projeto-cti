import requests

def obter_listas(board_id, api_key, token):

    resposta = requests.get(
        f"https://api.trello.com/1/boards/{board_id}/lists",
        params={
            "key": api_key,
            "token": token
        }
    )

    return resposta.json()