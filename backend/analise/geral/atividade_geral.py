from collections import defaultdict


def gerar_atividade_geral(movimentacoes):

    projetos = defaultdict(
        lambda: {
            "total_movimentacoes": 0,
            "ultimas_movimentacoes": []
        }
    )

    for card in movimentacoes:

        projeto = card["projeto"]

        for mov in card["movimentos"]:

            projetos[projeto][
                "total_movimentacoes"
            ] += 1

            projetos[projeto][
                "ultimas_movimentacoes"
            ].append({

                "card": card["card"],

                "origem":
                    mov["origem"],

                "destino":
                    mov["destino"],

                "data":
                    mov["data"]

            })

    resultado = []

    for projeto, dados in projetos.items():

        movimentacoes_ordenadas = sorted(
            dados["ultimas_movimentacoes"],
            key=lambda x: x["data"],
            reverse=True
        )

        resultado.append({

            "projeto": projeto,

            "total_movimentacoes":
                dados[
                    "total_movimentacoes"
                ],

            "ultimas_movimentacoes":
                movimentacoes_ordenadas[:10]

        })

    resultado.sort(
        key=lambda x:
        x["total_movimentacoes"],
        reverse=True
    )

    return resultado