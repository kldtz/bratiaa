import numpy.testing as npt
import pytest

from bratiaa.agree import *
from bratiaa.utils import tokenize

EXAMPLE_PROJECT = 'example-files/example-project'


@pytest.fixture(scope='module')
def instance_f1():
    labels = sorted(['PER', 'LOC', 'ORG', 'MISC'])
    return F1Agreement(partial(input_generator, 'example-files/example-project'), labels)


@pytest.fixture(scope='module')
def token_f1():
    labels = sorted(['PER', 'LOC', 'ORG', 'MISC'])
    return F1Agreement(partial(input_generator, 'example-files/example-project'), labels,
                       eval_func=exact_match_token_evaluation, token_func=tokenize)


def test_instance_total(instance_f1):
    mean, sd = instance_f1.mean_sd_total()
    assert mean == pytest.approx(0.8903501)
    assert sd == pytest.approx(0.0526314)


def test_instance_per_label(instance_f1):
    mean, sd = instance_f1.mean_sd_per_label()
    npt.assert_array_almost_equal(mean, [0.8191061, 0.84004593, 0.9059579, 0.93782234])
    npt.assert_array_almost_equal(sd, [0.13102913, 0.08971284, 0.05325575, 0.03875493])


def test_instance_per_document(instance_f1):
    mean, sd = instance_f1.mean_sd_per_document()
    npt.assert_array_almost_equal(mean,
                                  [0.79807203, 0.89395898, 0.90550807, 0.90580505, 0.93571596, 0.90673964, 0.87339767])
    npt.assert_array_almost_equal(sd,
                                  [0.1669697, 0.03874385, 0.07164957, 0.03713651, 0.0232565, 0.05167786, 0.06287414])


def test_token_total(token_f1):
    mean, sd = token_f1.mean_sd_total()

    assert mean == pytest.approx(0.9639787)
    assert sd == pytest.approx(0.01498979)


def test_token_per_label(token_f1):
    mean, sd = token_f1.mean_sd_per_label()
    npt.assert_array_almost_equal(mean, [0.963268, 0.918178, 0.972434, 0.982987])
    npt.assert_array_almost_equal(sd, [0.012501, 0.044941, 0.015136, 0.006485])


def test_token_per_document(token_f1):
    mean, sd = token_f1.mean_sd_per_document()
    npt.assert_array_almost_equal(mean,
                                  [0.971772, 0.945131, 0.927706, 0.942524, 0.973579, 0.976562, 0.951711])
    npt.assert_array_almost_equal(sd,
                                  [0.008875, 0.033929, 0.046871, 0.035116, 0.01296, 0.009569, 0.019581])
