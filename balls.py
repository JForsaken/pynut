# -*- coding: utf-8 -*-

import nltk
from nltk import *

# Grammar rules
with open ("shaft.cfg", "r") as myfile:
    grammaireText = myfile.read()

# Text source
with open ("jizz.txt", "r") as myfile:
    textSource = myfile.read()

grammar = grammar.FeatureGrammar.fromstring(grammaireText)
parser = nltk.ChartParser(grammar)
sentences = textSource.split('.')
for sentence in sentences:
    print(sentence)
    tokens = sentence.split()
    parser = parse.FeatureEarleyChartParser(grammar)
    trees = parser.parse(tokens)
    for tree in trees:
        print(tree)
        #nltk.draw.tree.draw_trees(tree)
        #print(tree.label()['SEM'])
