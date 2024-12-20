import pytest

from az_text_extractions.models.sentence import Sentence


def test_init_start_err():
    with pytest.raises(ValueError, match="start must be greater than or equal to 0"):
        Sentence(content="content", start=-1)


def test_includes():
    assert (
        Sentence.includes(
            [Sentence(content="hello ", start=0), Sentence(content="world", start=6)], 0
        )
        == "hello "
    )

    assert (
        Sentence.includes(
            [Sentence(content="hello ", start=0), Sentence(content="world", start=6)],
            10,
        )
        == "world"
    )

    assert not Sentence.includes(
        [Sentence(content="hello ", start=0), Sentence(content="world", start=6)], 100
    )
