# -*- coding: utf-8 -*-

import paths
import sys
import nltk
from nltk import *

# Grammar rules
with open (paths.DICTIONARY_FILE, "r") as myfile:
    grammaireText = myfile.read()

# Text source
with open (paths.STORY_FILE, "r") as myfile:
    textSource = myfile.read()

def print_header():
    print("\n")
    print("==================")
    print("=== Traitement ===")
    print("==================")

def process_fact(file, fact):
    print('fact')
    fo.write('Fact')

print_header()

# New fact file
fo = open(paths.FACTS_FILE, "w")

grammar = grammar.FeatureGrammar.fromstring(grammaireText)
parser = nltk.ChartParser(grammar)
sentences = textSource[:-1].split('.')

for i, sentence in enumerate(sentences):
    print("\n",i + 1,". ",sentence)
    tokens = sentence.split()
    parser = parse.FeatureEarleyChartParser(grammar)
    trees = parser.parse(tokens)

    for tree in trees:
        process_fact(fo, "fact")

fo.close();
