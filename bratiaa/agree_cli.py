import logging

import argparse

from bratiaa.agree import iaa_report, compute_f1_agreement
from bratiaa.utils import tokenize


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('project_root',
                        help='Root directory of the Brat annotation project')
    parser.add_argument('--heatmap',
                        help='Output path for F1-agreement heatmap',
                        dest='heatmap_path')
    parser.add_argument('-p', '--precision',
                        help='Precision of results (number of digits following the decimal point)',
                        dest='precision',
                        default=3)
    parser.add_argument('-s', '--silent',
                        help='Set log level on ERROR',
                        action='store_true')
    parser.add_argument('-t', '--tokenize',
                        help='Token-based evaluation (tokenizer splits on whitespace)',
                        action='store_true')
    return parser.parse_args()


def main():
    args = parse_args()
    log_level = logging.WARNING
    if args.silent:
        log_level = logging.ERROR
    logging.basicConfig(level=log_level,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    token_func = None
    if args.tokenize:
        token_func = tokenize

    f1_agreement = compute_f1_agreement(args.project_root, token_func=token_func)
    iaa_report(f1_agreement, args.precision)
    if args.heatmap_path:
        f1_agreement.draw_heatmap(args.heatmap_path)


if __name__ == '__main__':
    main()
