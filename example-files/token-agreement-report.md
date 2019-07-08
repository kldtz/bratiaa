# Inter-Annotator Agreement Report

* Token-based F1 agreement

## Project Setup

* 4 annotators: Lisa, Maria, Max, Peter
* 7 documents: esp.train-doc-100.ann, esp.train-doc-46.ann, esp.train-doc-503.ann, esp.train-doc-896.ann, esp.train-doc-423.ann, esp.train-doc-1400.ann, esp.train-doc-29.ann
* 4 labels: LOC, MISC, ORG, PER

## Agreement per Document

| Document               |   Mean F1 |   SD F1 |
|------------------------|-----------|---------|
| esp.train-doc-100.ann  |     0.972 |   0.009 |
| esp.train-doc-46.ann   |     0.945 |   0.034 |
| esp.train-doc-503.ann  |     0.928 |   0.047 |
| esp.train-doc-896.ann  |     0.943 |   0.035 |
| esp.train-doc-423.ann  |     0.974 |   0.013 |
| esp.train-doc-1400.ann |     0.977 |   0.010 |
| esp.train-doc-29.ann   |     0.952 |   0.020 |

## Agreement per Label

| Label   |   Mean F1 |   SD F1 |
|---------|-----------|---------|
| LOC     |     0.963 |   0.013 |
| MISC    |     0.918 |   0.045 |
| ORG     |     0.972 |   0.015 |
| PER     |     0.983 |   0.006 |

## Overall Agreement

* Mean F1: 0.964, SD F1: 0.015

