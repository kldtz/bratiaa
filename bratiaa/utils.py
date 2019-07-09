import re

import numpy as np

ENCODING = 'utf-8'

TOKEN = re.compile(r'\S+')


def tokenize(text):
    for match in re.finditer(TOKEN, text):
        yield match.start(), match.end()


def read(path, encoding=ENCODING, newline='\r\n', mode='r'):
    with open(path, newline=newline, encoding=encoding, mode=mode) as fin:
        return fin.read()


class TokenOverlap:
    """
    Data structure for quick lookup of tokens overlapping with given span.
    Assumes that the provided list of tokens is sorted by indices!
    """

    def __init__(self, text, tokens):
        self.tokens = tokens
        self.char2token = self.compute_mapping(len(text), tokens)

    @staticmethod
    def compute_mapping(text_length, tokens):
        char2token = np.zeros(text_length, dtype=int)
        i = 0
        for token_idx, (start, end) in enumerate(tokens):
            char2token[i:start] = token_idx - 1
            char2token[start:end] = token_idx
            i = end
        char2token[i:text_length] = len(tokens) - 1
        return char2token

    def overlapping_tokens(self, start, end):
        assert end <= len(self.char2token), f'End index {end} > text length {len(self.char2token)}!'
        if end < 1 or start >= end:
            return []
        start_token = self.char2token[start]
        if start_token == -1: # start offset before first token
            start_token = 0
        if self.tokens[start_token][1] <= start: # start offset between two tokens
            start_token += 1
        end_token = self.char2token[end - 1] # end offset is exclusive
        if end_token < 0 or end_token < start_token:
            return []
        return self.tokens[start_token:end_token + 1]
