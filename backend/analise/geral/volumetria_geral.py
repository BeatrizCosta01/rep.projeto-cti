from collections import defaultdict


def gerar_volumetria_geral(cards):

    projetos = defaultdict(
        lambda: {
            "total_cards": 0,
            "listas": {}
        }
    )

    for card in cards:

        projeto = card["projeto"]
        lista = card["lista"]

        projetos[projeto]["total_cards"] += 1

        if lista not in projetos[projeto]["listas"]:
            projetos[projeto]["listas"][lista] = 0

        projetos[projeto]["listas"][lista] += 1

    resultado = []

    for projeto, dados in projetos.items():

        resultado.append({
            "projeto": projeto,
            "total_cards": dados["total_cards"],
            "listas": dados["listas"]
        })

    return {
        "quantidade_projetos": len(projetos),
        "total_cards": len(cards),
        "projetos": resultado
    }