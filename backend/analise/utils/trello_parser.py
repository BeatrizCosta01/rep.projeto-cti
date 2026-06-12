
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]

DATA_DIR = BASE_DIR / "data"


def carregar_cards():
    with open(
        DATA_DIR / "cards.json",
        encoding="utf-8"
    ) as f:
        return json.load(f)


def carregar_movimentacoes():
    with open(
        DATA_DIR / "movimentacoes.json",
        encoding="utf-8"
    ) as f:
        return json.load(f)


def carregar_actions():
    with open(
        DATA_DIR / "actions_bruto.json",
        encoding="utf-8"
    ) as f:
        return json.load(f)