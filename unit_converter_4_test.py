import unit_converter_4;
import pytest

def test_unit_converter_4(monkeypatch):
    inputs = iter(['100', 'm', "km"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert unit_converter_4.unit_converter() == "100 m is 0.1 km"
