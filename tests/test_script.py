from scripts.scripts import load_data, five_items


def test_load_data():
    assert load_data() is not None


def test_five_items():
    assert five_items()