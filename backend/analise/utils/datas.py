from datetime import datetime
from datetime import timezone


def converter_data(data):

    if not data:
        return None

    return datetime.fromisoformat(
        data.replace("Z", "+00:00")
    )


def dias_sem_movimento(data):

    data = converter_data(data)

    if not data:
        return None

    return (
        datetime.now(timezone.utc)
        - data
    ).days


def diferenca_dias(
    data_inicio,
    data_fim
):

    inicio = converter_data(
        data_inicio
    )

    fim = converter_data(
        data_fim
    )

    if not inicio or not fim:
        return None

    return round(
        (
            fim - inicio
        ).total_seconds() / 86400,
        2
    )