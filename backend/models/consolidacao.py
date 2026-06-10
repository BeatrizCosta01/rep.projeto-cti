def consolidar_card(
    board,
    card,
    mapa_listas,
    mapa_membros
):

    responsaveis = []

    for membro_id in card.get(
        "idMembers",
        []
    ):

        if membro_id in mapa_membros:

            responsaveis.append(
                mapa_membros[membro_id]
            )

    return {

        "projeto": board["name"],

        "card": card.get("name"),

        "descricao": card.get("desc"),

        "lista":
            mapa_listas.get(
                card.get("idList"),
                "Desconhecida"
            ),

        "responsaveis":
            responsaveis,

        "qtd_responsaveis":
            len(card.get("idMembers", [])),

        "ultima_atividade":
            card.get("dateLastActivity"),

        "prazo":
            card.get("due"),

        "concluido":
            card.get("closed"),

        "labels":
            card.get("labels"),

        "url":
            card.get("url")
    }