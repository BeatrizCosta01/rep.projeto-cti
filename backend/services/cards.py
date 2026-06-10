import requests

def obter_cards(board_id, api_key, token):

    resposta = requests.get(
        f"https://api.trello.com/1/boards/{board_id}/cards",
        params={
            "key": api_key,
            "token": token,
            "fields": (
                "id,"
                "name,"
                "desc,"
                "dateLastActivity,"
                "due,"
                "closed,"
                "idList,"
                "idMembers,"
                "labels,"
                "url,"
                "shortUrl"
            )
        }
    )

    return resposta.json()
