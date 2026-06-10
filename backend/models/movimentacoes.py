from datetime import datetime

def extrair_movimentacoes(actions):

    movimentos = []

    for action in actions:

        if action.get("type") != "updateCard":
            continue

        data = action.get("data", {})

        if (
            "listBefore" in data
            and
            "listAfter" in data
        ):

            movimentos.append({

                "data":
                    action["date"],

                "origem":
                    data["listBefore"]["name"],

                "destino":
                    data["listAfter"]["name"]
            })

    return movimentos