import json
import os


def salvar_json(
    nome_arquivo,
    dados
):

    os.makedirs(
        "frontend/json",
        exist_ok=True
    )

    caminho = os.path.join(
        "frontend/json",
        nome_arquivo
    )

    with open(
        caminho,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            dados,
            f,
            ensure_ascii=False,
            indent=4
        )

    print(
        f"Arquivo salvo: {caminho}"
    )