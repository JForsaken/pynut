# -*- coding: utf-8 -*-

import paths
import nltk
from nltk import *


def destructure_sentence(sentence):
    currentSentence = []
    for node in sentence:
        currentSentence.append((node[0], str(node[1]).split("'")[1]))

    return currentSentence


# Grammar rules
with open (paths.DICTIONARY_FILE, "r") as myfile:
    grammaireText = myfile.read()

# Text source
with open (paths.STORY_FILE, "r") as myfile:
    textSource = myfile.read()

grammar = grammar.FeatureGrammar.fromstring(grammaireText)
parser = nltk.ChartParser(grammar)
sentences = textSource[:-1].split('.')
sentenceTrace = []

for sentence in sentences:
    print(sentence)
    tokens = sentence.split()
    parser = parse.FeatureEarleyChartParser(grammar)
    trees = parser.parse(tokens)
    for index, tree in enumerate(trees):
        print(tree)
        if index == 0:
            sentenceTrace.append(destructure_sentence(tree.pos()))
        #nltk.draw.tree.draw_trees(tree)
        #print(tree.label()['SEM'])

print(sentenceTrace)
