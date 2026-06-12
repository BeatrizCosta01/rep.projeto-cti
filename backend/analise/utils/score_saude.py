def calcular_score_saude(
    total_cards,
    sem_responsavel,
    vencidos,
    estagnados
):

    if total_cards == 0:
        return 100

    score = 100

    score -= (
        sem_responsavel
        / total_cards
    ) * 40

    score -= (
        vencidos
        / total_cards
    ) * 30

    score -= (
        estagnados
        / total_cards
    ) * 30

    return round(
        max(score, 0),
        2
    )



