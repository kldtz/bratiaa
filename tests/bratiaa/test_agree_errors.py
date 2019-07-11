from bratiaa.agree import *
from functools import partial
import pytest


def test_missing_label():
    with pytest.raises(ValueError, match='Encountered unkown label MISC!.*'):
        root = 'data/agreement/agree-2'
        labels = ['PER', 'LOC', 'ORG']  # missing label
        docs = ['esp.train-doc-29.ann', 'esp.train-doc-46.ann']
        annotators = ['ann1', 'ann2']
        F1Agreement(partial(input_generator, root), labels, annotators=annotators, documents=docs)


def test_missing_document():
    with pytest.raises(AssertionError, match='Input generator yields more documents than expected!'):
        root = 'data/agreement/agree-2'
        labels = ['PER', 'LOC', 'ORG', 'MISC']
        docs = ['esp.train-doc-29.ann']  # missing document
        annotators = ['ann1', 'ann2']
        F1Agreement(partial(input_generator, root), labels, annotators=annotators, documents=docs)


def test_single_annotator():
    with pytest.raises(AssertionError, match='At least two annotators are necessary to compute agreement!'):
        root = 'data/agreement/agree-2-unterschiede'
        labels = ['PER', 'LOC', 'ORG', 'MISC']
        docs = ['esp.train-doc-29.ann', 'esp.train-doc-46.ann']
        annotators = ['ann1']
        F1Agreement(partial(input_generator, root), labels, annotators=annotators, documents=docs)
