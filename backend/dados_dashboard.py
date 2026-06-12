from analise.utils.trello_parser import (
    carregar_cards,
    carregar_movimentacoes
)

from analise.utils.exportador_json import (
    salvar_json
)

from analise.geral.volumetria_geral import (
    gerar_volumetria_geral
)

from analise.geral.atividade_geral import (
    gerar_atividade_geral
)

from analise.geral.saude_operacional import (
    gerar_saude_operacional
)

from analise.geral.ranking_projetos import (
    gerar_ranking_projetos
)

from analise.geral.velocidade_projetos import (
    gerar_velocidade_projetos
)

from analise.geral.maturidade_projetos import (
    gerar_maturidade_projetos
)


def main():

    print("=" * 60)
    print("GERANDO DASHBOARD ANALÍTICO")
    print("=" * 60)

    print("\nCarregando dados...")

    cards = carregar_cards()

    movimentacoes = carregar_movimentacoes()

    print("Gerando volumetria...")
    volumetria = gerar_volumetria_geral(
        cards
    )

    print("Gerando atividade...")
    atividade = gerar_atividade_geral(
        movimentacoes
    )

    print("Gerando saúde operacional...")
    saude = gerar_saude_operacional(
        cards
    )

    print("Gerando ranking de projetos...")
    ranking = gerar_ranking_projetos(
        movimentacoes
    )

    print("Gerando velocidade dos projetos...")
    velocidade = gerar_velocidade_projetos(
        movimentacoes
    )

    print("Gerando maturidade dos projetos...")
    maturidade = gerar_maturidade_projetos(
        cards
    )

    dashboard = {

        "volumetria": volumetria,

        "atividade": atividade,

        "saude_operacional": saude,

        "ranking_projetos": ranking,

        "velocidade_projetos": velocidade,

        "maturidade_projetos": maturidade

    }

    salvar_json(
        "dashboard_geral.json",
        dashboard
    )

    print(
        "\nDashboard gerado com sucesso!"
    )

    print(
        "\nArquivo criado:"
    )

    print(
        "frontend/json/dashboard_geral.json"
    )


if __name__ == "__main__":
    main()