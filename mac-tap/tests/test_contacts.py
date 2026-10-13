import pytest

from tc_tap.contacts import is_personal, load_categories, normalize_contact


def test_normalize_contact_variants():
    # Fable M2: E.164 across iMessage handles / CSV / FUB formats
    assert normalize_contact("+17141234567") == "+17141234567"
    assert normalize_contact("7141234567") == "+17141234567"
    assert normalize_contact("(714) 123-4567") == "+17141234567"
    assert normalize_contact("1-714-123-4567") == "+17141234567"
    assert normalize_contact("Pat.Example@iCloud.com") == "pat.example@icloud.com"
    assert normalize_contact("627499") == "627499"  # short code preserved
    assert normalize_contact("") is None


def test_load_categories_matches_imessage_handles(tmp_path):
    csv = tmp_path / "cats.csv"
    csv.write_text(
        "Category,Name,Contact,Total Msgs\n"
        "Friends & Family,Mom,7145550142,9148\n"
        "Clients (Borrowers),Client One,9495550123,1146\n"
    )
    cats = load_categories(csv)
    assert cats["+17145550142"] == "Friends & Family"  # iMessage handle format resolves
    assert is_personal(cats["+17145550142"]) is True
    assert is_personal(cats["+19495550123"]) is False


def test_name_map_resolves_handles_excluding_blanks(monkeypatch):
    # tap v2: handle -> Contacts display name; blanks and handle-less rows out
    from tc_tap import contacts

    monkeypatch.setattr(
        contacts,
        "read_contacts",
        lambda home=None: [
            {"name": "Client Two", "contact": "+15625550188", "birthday": None},
            {"name": "", "contact": "+13105550000", "birthday": None},
            {"name": "No Handle", "contact": None, "birthday": None},
        ],
    )
    assert contacts.name_map() == {"+15625550188": "Client Two"}
