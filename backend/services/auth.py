import webbrowser

def obter_token(api_key):

    link_oauth = (
        f"https://trello.com/1/authorize"
        f"?expiration=1day"
        f"&name=PipelineCTI"
        f"&scope=read"
        f"&response_type=token"
        f"&key={api_key}"
    )

    print("Abrindo navegador...")
    webbrowser.open(link_oauth)

    return input(
        "\nCole o token gerado: "
    ).strip()