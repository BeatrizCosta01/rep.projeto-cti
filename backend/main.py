import json
import os

from config import API_KEY

from services.auth import obter_token
from services.boards import obter_boards
from services.lists import obter_listas
from services.members import obter_membros
from services.cards import obter_cards
from services.actions import obter_actions

from models.consolidacao import consolidar_card
from models.movimentacoes import extrair_movimentacoes


def salvar_json(nome_arquivo, dados):

    os.makedirs("data", exist_ok=True)

    with open(
        f"data/{nome_arquivo}",
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            dados,
            arquivo,
            ensure_ascii=False,
            indent=4
        )


def main():

    print("=" * 70)
    print("PIPELINE TRELLO - EXTRAÇÃO COMPLETA")
    print("=" * 70)

    token = obter_token(API_KEY)

    print("\nBuscando quadros...")

    boards = obter_boards(
        API_KEY,
        token
    )

    print(
        f"\n{len(boards)} quadros encontrados."
    )

    cards_consolidados = []

    actions_bruto = []

    movimentacoes = []

    for board in boards:

        board_id = board["id"]

        print(
            f"\nProcessando quadro: {board['name']}"
        )

        listas = obter_listas(
            board_id,
            API_KEY,
            token
        )

        membros = obter_membros(
            board_id,
            API_KEY,
            token
        )

        cards = obter_cards(
            board_id,
            API_KEY,
            token
        )

        mapa_listas = {
            lista["id"]: lista["name"]
            for lista in listas
        }

        mapa_membros = {
            membro["id"]: membro["fullName"]
            for membro in membros
        }

        print(
            f"{len(cards)} cards encontrados."
        )

        for card in cards:

            # ---------------------
            # CARD CONSOLIDADO
            # ---------------------

            cards_consolidados.append(

                consolidar_card(
                    board,
                    card,
                    mapa_listas,
                    mapa_membros
                )

            )

            # ---------------------
            # HISTÓRICO DO CARD
            # ---------------------

            try:

                actions = obter_actions(
                    card["id"],
                    API_KEY,
                    token
                )

                actions_bruto.append({

                    "projeto":
                        board["name"],

                    "card_id":
                        card["id"],

                    "card":
                        card["name"],

                    "actions":
                        actions
                })

                movimentos = extrair_movimentacoes(
                    actions
                )

                movimentacoes.append({

                    "projeto":
                        board["name"],

                    "card_id":
                        card["id"],

                    "card":
                        card["name"],

                    "movimentos":
                        movimentos
                })

            except Exception as erro:

                print(
                    f"Erro no card "
                    f"{card['name']}: {erro}"
                )

    print("\nSalvando arquivos...")

    salvar_json(
        "cards.json",
        cards_consolidados
    )

    salvar_json(
        "actions_bruto.json",
        actions_bruto
    )

    salvar_json(
        "movimentacoes.json",
        movimentacoes
    )

    print("\nExtração concluída!")

    print(
        f"\nCards exportados: "
        f"{len(cards_consolidados)}"
    )

    print(
        f"Históricos exportados: "
        f"{len(actions_bruto)}"
    )

    print(
        "\nArquivos gerados:"
    )

    print("- data/cards.json")
    print("- data/actions_bruto.json")
    print("- data/movimentacoes.json")


if __name__ == "__main__":
    main()