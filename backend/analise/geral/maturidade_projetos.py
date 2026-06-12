from collections import defaultdict


PESOS_MATURIDADE = {

    "Backlog": 0,

    "A Fazer": 20,

    "To Do": 20,

    "Em andamento": 60,

    "Doing": 60,

    "Validação": 80,

    "Teste": 80,

    "Homologação": 90,

    "Concluído": 100,

    "Concluído 🎉": 100,

    "Done": 100

}


def gerar_maturidade_projetos(
    cards
):

    projetos = defaultdict(
        lambda: {
            "cards": 0,
            "pontuacao": 0
        }
    )

    for card in cards:

        projeto = card["projeto"]

        lista = card["lista"]

        peso = PESOS_MATURIDADE.get(
            lista,
            50
        )

        projetos[projeto]["cards"] += 1

        projetos[projeto][
            "pontuacao"
        ] += peso

    resultado = []

    for projeto, dados in projetos.items():

        maturidade = round(

            dados["pontuacao"]

            /

            dados["cards"],

            2

        )

        if maturidade >= 80:

            status = "Maduro"

        elif maturidade >= 50:

            status = "Em Evolução"

        else:

            status = "Inicial"

        resultado.append({

            "projeto":
                projeto,

            "cards":
                dados["cards"],

            "maturidade":
                maturidade,

            "status":
                status

        })

    resultado.sort(
        key=lambda x:
        x["maturidade"],
        reverse=True
    )

    return resultado