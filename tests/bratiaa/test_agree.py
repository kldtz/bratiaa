import pytest

from bratiaa.agree import *
from bratiaa.utils import tokenize

AGREE_2_ROOT = 'data/agreement/agree-2'


@pytest.fixture(scope='module')
def agree_2():
    labels = ['PER', 'LOC', 'ORG', 'MISC']

    return F1Agreement(partial(input_generator, AGREE_2_ROOT), labels)


def test_avg_total(agree_2):
    f1, f1_std = agree_2.mean_sd_total()
    assert f1 == pytest.approx(0.787878, 0.0001)
    assert f1_std == 0.0


def test_avg_type(agree_2):
    f1, _ = agree_2.mean_sd_per_label()
    assert f1.shape == (len(agree_2.labels),)


def test_avg_doc(agree_2):
    f1, _ = agree_2.mean_sd_per_document()
    assert f1.shape == (2,)


def test_one_vs_all_smoke(agree_2):
    agree_2.mean_sd_total_one_vs_rest('ann-1')


def test_instance_iaa_report_smoke():
    iaa_report(compute_f1_agreement(AGREE_2_ROOT))


def test_token_iaa_report_smoke():
    iaa_report(compute_f1_agreement(AGREE_2_ROOT, token_func=tokenize))


def test_collect_redundant_files():
    assert len(collect_redundant_files(Path(AGREE_2_ROOT), ['ann1', 'ann2'])) == 2
