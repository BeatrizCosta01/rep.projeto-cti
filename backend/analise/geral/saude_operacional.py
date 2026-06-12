from collections import defaultdict

from analise.utils.datas import (
    dias_sem_movimento
)

from analise.utils.score_saude import (
    calcular_score_saude
)


def gerar_saude_operacional(cards):

    projetos = defaultdict(
        lambda: {
            "cards_total": 0,
            "sem_responsavel": 0,
            "vencidos": 0,
            "estagnados": 0
        }
    )

    for card in cards:

        projeto = card["projeto"]

        projetos[projeto]["cards_total"] += 1

        # Sem responsável
        if not card.get("responsaveis"):
            projetos[projeto][
                "sem_responsavel"
            ] += 1

        # Vencidos
        if (
            card.get("vencido")
            is True
        ):
            projetos[projeto][
                "vencidos"
            ] += 1

        # Estagnados
        dias = dias_sem_movimento(
            card.get(
                "ultima_atividade"
            )
        )

        if (
            dias is not None
            and dias > 15
        ):
            projetos[projeto][
                "estagnados"
            ] += 1

    resultado = []

    for projeto, dados in projetos.items():

        score = calcular_score_saude(

            dados["cards_total"],

            dados["sem_responsavel"],

            dados["vencidos"],

            dados["estagnados"]

        )

        resultado.append({

            "projeto": projeto,

            "score_saude": score,

            "cards_total":
                dados["cards_total"],

            "sem_responsavel":
                dados[
                    "sem_responsavel"
                ],

            "vencidos":
                dados["vencidos"],

            "estagnados":
                dados["estagnados"]

        })

    resultado.sort(
        key=lambda x:
        x["score_saude"],
        reverse=True
    )

    return resultado