from collections import Counter


def analisar_movimentacoes(movimentacoes):

    contador = Counter()
    historico_por_card = {}

    for card in movimentacoes:

        nome_card = card["card_id"]

        historico_card = []

        for mov in card["movimentos"]:

            fluxo = (
                f"{mov['origem']} -> "
                f"{mov['destino']}"
            )

            contador[fluxo] += 1

            historico_card.append({

                "data": mov["data"],
                "transicao": fluxo

            })

        historico_por_card[
            nome_card
        ] = historico_card

    return {

        "contagem_fluxos":
            dict(contador),

        "historico_por_card":
            historico_por_card
    }