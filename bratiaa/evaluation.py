"""
Functions for computing the difference between two sets of annotations.
"""
from collections import namedtuple, Counter

import bratsubset.annotation as bs

Annotation = namedtuple('Annotation', ['type', 'label', 'offsets'])


def exact_match_instance_evaluation(ann_path_1, ann_path_2, tokens=None):
    exp = set(_read_textbound_annotations(ann_path_1))
    pred = set(_read_textbound_annotations(ann_path_2))
    tp = exp.intersection(pred)
    return tp, exp, pred


def _read_textbound_annotations(ann_path):
    with bs.Annotations(ann_path.as_posix(), read_only=True) as annotations:
        for annotation in annotations.get_textbounds():
            yield Annotation('T', annotation.type, tuple(annotation.spans))


def exact_match_token_evaluation(ann_path_1, ann_path_2, tokens=None):
    """
    Annotations are split into token-sized bits before evaluation.

    Sub-token annotations are expanded to full tokens. Long annotations will influence the results more than short
    annotations. Boundary errors for adjacent annotations with the same label are ignored!
    """
    exp_list = list(_read_token_annotations(ann_path_1, tokens))
    pred_list = list(_read_token_annotations(ann_path_2, tokens))
    tp = counter2list(Counter(exp_list) & Counter(pred_list))
    return tp, exp_list, pred_list


def counter2list(c):
    for elem, cnt in c.items():
        for i in range(cnt):
            yield (elem)


def _read_token_annotations(ann_path, tokens):
    """
    Yields a new annotation for each token overlapping with an annotation. If annotations are overlapping each other,
    there will be multiple annotations for a single token.
    """
    for annotation in set(_read_textbound_annotations(ann_path)):
        for start, end in annotation.offsets:
            for ts, te in tokens.overlapping_tokens(start, end):
                yield Annotation(annotation.type, annotation.label, ((ts, te),))
