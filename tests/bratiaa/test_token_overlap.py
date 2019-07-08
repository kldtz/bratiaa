from bratiaa.utils import TokenOverlap


def test_identical_spans():
    text = 'This is a sentence.'
    tokens = [(0, 4), (5, 7), (8, 9), (10, 18), (18, 19)]

    to = TokenOverlap(text, tokens)

    for start, end in tokens:
        overlap = to.overlapping_tokens(start, end)
        assert len(overlap) == 1
        assert overlap[0] == (start, end)


def test_empty_overlap_at_beginning():
    text = '   This is a sentence.'
    tokens = [(3, 7), (8, 10), (11, 12), (13, 21), (21, 22)]

    to = TokenOverlap(text, tokens)

    assert len(to.overlapping_tokens(0, 2)) == 0
    assert len(to.overlapping_tokens(1, 3)) == 0
    assert len(to.overlapping_tokens(0, 3)) == 0


def test_empty_overlap_between_tokens():
    text = 'This is a sentence.'
    tokens = [(0, 4), (5, 7), (8, 9), (10, 18), (18, 19)]

    to = TokenOverlap(text, tokens)

    assert len(to.overlapping_tokens(4, 5)) == 0
    assert len(to.overlapping_tokens(7, 8)) == 0
    assert len(to.overlapping_tokens(18, 18)) == 0


def test_spans_overlapping_spaces():
    text = 'This is a sentence.'
    tokens = [(0, 4), (5, 7), (8, 9), (10, 18), (18, 19)]

    to = TokenOverlap(text, tokens)

    assert to.overlapping_tokens(5, 9) == [(5, 7), (8, 9)]
    assert to.overlapping_tokens(5, 10) == [(5, 7), (8, 9)]
    assert to.overlapping_tokens(4, 9) == [(5, 7), (8, 9)]
    assert to.overlapping_tokens(4, 10) == [(5, 7), (8, 9)]


def test_spans_overlapping_tokens():
    text = 'This is a sentence.'
    tokens = [(0, 4), (5, 7), (8, 9), (10, 18), (18, 19)]

    to = TokenOverlap(text, tokens)

    assert to.overlapping_tokens(6, 11) == [(5, 7), (8, 9), (10, 18)]
    assert to.overlapping_tokens(5, 15) == [(5, 7), (8, 9), (10, 18)]
