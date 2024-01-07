from seasons import convert
import pytest
from datetime import date
from datetime import timedelta


def test_convert():
    assert (
        convert(str(date.today() - timedelta(days=365)), date.today())
        == "Five hundred twenty-five thousand, six hundred minutes"
    )
    assert (
        convert(str(date.today() - timedelta(days=730)), date.today())
        == "One million, fifty-one thousand, two hundred minutes"
    )
    with pytest.raises(SystemExit):
        convert("May 1", date.today())
