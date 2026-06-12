from collections import defaultdict


def gerar_ranking_projetos(
    movimentacoes
):

    projetos = defaultdict(int)

    for card in movimentacoes:

        projeto = card["projeto"]

        projetos[projeto] += len(
            card["movimentos"]
        )

    maior_movimentacao = max(
        projetos.values(),
        default=0
    )

    ranking = []

    for projeto, qtd in projetos.items():

        percentual = 0

        if maior_movimentacao > 0:

            percentual = round(
                (
                    qtd
                    / maior_movimentacao
                ) * 100,
                2
            )

        if percentual >= 80:

            status = "Alta"

        elif percentual >= 50:

            status = "Média"

        else:

            status = "Baixa"

        ranking.append({

            "projeto": projeto,

            "movimentacoes": qtd,

            "percentual_atividade":
                percentual,

            "status":
                status

        })

    ranking.sort(
        key=lambda x:
        x["movimentacoes"],
        reverse=True
    )

    for posicao, item in enumerate(
        ranking,
        start=1
    ):

        item["ranking"] = posicao

    return ranking