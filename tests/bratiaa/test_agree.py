from bratiaa.agree import *
from bratiaa.utils import tokenize
from functools import partial
import pytest


def test_avg_total():
    root = 'data/agreement/agree-2'
    labels = ['PER', 'LOC', 'ORG', 'MISC']

    e = F1Agreement(partial(input_generator, root), labels)

    f1, f1_std = e.mean_sd_total()
    assert f1 == pytest.approx(0.787878, 0.0001)
    assert f1_std == 0.0


def test_avg_type():
    root = 'data/agreement/agree-2'
    labels = ['PER', 'LOC', 'ORG', 'MISC']

    e = F1Agreement(partial(input_generator, root), labels)

    f1, _ = e.mean_sd_per_label()
    assert f1.shape == (len(e.labels),)


def test_avg_doc():
    root = 'data/agreement/agree-2'
    labels = ['PER', 'LOC', 'ORG', 'MISC']

    e = F1Agreement(partial(input_generator, root), labels)

    f1, _ = e.mean_sd_per_document()
    assert f1.shape == (2,)


def test_one_vs_all_smoke():
    root = 'data/agreement/agree-2'
    labels = ['PER', 'LOC', 'ORG', 'MISC']

    e = F1Agreement(partial(input_generator, root), labels)
    e.mean_sd_total_one_vs_rest('ann-1')


def test_instance_iaa_report_smoke():
    root = 'data/agreement/agree-2'
    iaa_report(compute_f1_agreement(root))


def test_token_iaa_report_smoke():
    root = 'data/agreement/agree-2'
    iaa_report(compute_f1_agreement(root, token_func=tokenize))


def test_collect_redundant_files():
    root = Path('data/agreement/agree-2')
    assert len(collect_redundant_files(root, ['ann1', 'ann2'])) == 2
