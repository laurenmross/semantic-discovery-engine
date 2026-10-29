"""Third-party text configured for redaction never reaches the saved artifacts."""
from sde.datasets import DATASETS
from sde.pipeline import redact_packet, redact_structure

COLS = {"Ads.Title": "ad title"}


def _structure():
    col = {"table": "Ads", "column": "Title", "min": "Abc", "max": "Пример", "samples": ["Тестовый текст", "x"],
           "top_values": [["Тестовый текст", 3]]}
    other = {"table": "Ads", "column": "Kind", "min": "a", "max": "b", "samples": ["a"], "top_values": [["a", 1]]}
    return {"tables": {"Ads": {"columns": [col, other]}}}


def test_structure_redacts_only_configured_column():
    s = _structure()
    out = redact_structure(s, COLS)
    title, kind = out["tables"]["Ads"]["columns"]
    assert title["samples"] == ["[redacted ad title]"] * 2
    assert title["top_values"] == [["[redacted ad title]", 3]]
    assert title["min"] == title["max"] == "[redacted ad title]"
    assert kind == s["tables"]["Ads"]["columns"][1]
    assert s["tables"]["Ads"]["columns"][0]["samples"][0] == "Тестовый текст"  # input left untouched


def test_packet_redacts_original_names_and_leaves_masked_lines():
    text = ("- Title: VARCHAR; examples ['Тестовый текст', 'Example Title 1']  [S:c:Ads.Title]\n"
            "- c06: VARCHAR; examples ['<text, ~19 chars, Cyrillic script>']  [S:c:T05.c06]\n")
    out = redact_packet(text, COLS)
    assert "Тестовый текст" not in out and "Example" not in out
    assert "[redacted ad title]" in out
    assert out.splitlines()[1] == text.splitlines()[1]


def test_avito_redacts_its_free_text_columns():
    assert set(DATASETS["avito"].redact) == {"AdsInfo.Title", "SearchInfo.SearchQuery"}
