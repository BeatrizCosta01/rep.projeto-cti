from collections import defaultdict
from datetime import datetime
from datetime import timezone

from analise.utils.datas import (
    converter_data
)


def gerar_velocidade_projetos(
    movimentacoes
):

    projetos = defaultdict(
        lambda: {
            "cards": 0,
            "movimentacoes": 0,
            "primeira_data": None,
            "ultima_data": None,
            "tempos_cards": [],
            "tempos_movimentacoes": []
        }
    )

    for card in movimentacoes:

        projeto = card["projeto"]

        movimentos = sorted(
            card["movimentos"],
            key=lambda x: x["data"]
        )

        if not movimentos:
            continue

        projetos[projeto]["cards"] += 1

        projetos[projeto]["movimentacoes"] += len(
            movimentos
        )

        primeira_card = converter_data(
            movimentos[0]["data"]
        )

        ultima_card = converter_data(
            movimentos[-1]["data"]
        )

        # vida útil do card

        duracao_card = (
            ultima_card - primeira_card
        ).total_seconds() / 86400

        projetos[projeto][
            "tempos_cards"
        ].append(
            round(duracao_card, 2)
        )

        # datas globais do projeto

        if (
            projetos[projeto][
                "primeira_data"
            ] is None
            or primeira_card <
            projetos[projeto][
                "primeira_data"
            ]
        ):

            projetos[projeto][
                "primeira_data"
            ] = primeira_card

        if (
            projetos[projeto][
                "ultima_data"
            ] is None
            or ultima_card >
            projetos[projeto][
                "ultima_data"
            ]
        ):

            projetos[projeto][
                "ultima_data"
            ] = ultima_card

        # tempo entre movimentações

        for i in range(
            len(movimentos) - 1
        ):

            atual = converter_data(
                movimentos[i]["data"]
            )

            proxima = converter_data(
                movimentos[i + 1]["data"]
            )

            tempo = (
                proxima - atual
            ).total_seconds() / 86400

            projetos[projeto][
                "tempos_movimentacoes"
            ].append(
                round(tempo, 2)
            )

    resultado = []

    agora = datetime.now(
        timezone.utc
    )

    for projeto, dados in projetos.items():

        dias_projeto = (
            dados["ultima_data"]
            - dados["primeira_data"]
        ).days

        dias_sem_movimento = (
            agora
            - dados["ultima_data"]
        ).days

        media_card = round(

            sum(
                dados[
                    "tempos_cards"
                ]
            )

            /

            len(
                dados[
                    "tempos_cards"
                ]
            ),

            2

        )

        media_mov = 0

        if dados[
            "tempos_movimentacoes"
        ]:

            media_mov = round(

                sum(
                    dados[
                        "tempos_movimentacoes"
                    ]
                )

                /

                len(
                    dados[
                        "tempos_movimentacoes"
                    ]
                ),

                2

            )

        movimentacoes_dia = round(

            dados["movimentacoes"]

            /

            max(
                dias_projeto,
                1
            ),

            2

        )

        # índice de velocidade

        velocidade = round(

            movimentacoes_dia
            * 10,

            2

        )

        velocidade = min(
            velocidade,
            100
        )

        resultado.append({

            "projeto":
                projeto,

            "cards":
                dados["cards"],

            "movimentacoes":
                dados[
                    "movimentacoes"
                ],

            "dias_projeto":
                dias_projeto,

            "primeira_movimentacao":
                dados[
                    "primeira_data"
                ].isoformat(),

            "ultima_movimentacao":
                dados[
                    "ultima_data"
                ].isoformat(),

            "dias_sem_movimento":
                dias_sem_movimento,

            "movimentacoes_por_dia":
                movimentacoes_dia,

            "tempo_medio_card_dias":
                media_card,

            "tempo_medio_movimentacao_dias":
                media_mov,

            "menor_tempo_card":
                min(
                    dados[
                        "tempos_cards"
                    ]
                ),

            "maior_tempo_card":
                max(
                    dados[
                        "tempos_cards"
                    ]
                ),

            "indice_velocidade":
                velocidade

        })

    resultado.sort(
        key=lambda x:
        x["indice_velocidade"],
        reverse=True
    )

    return resultado