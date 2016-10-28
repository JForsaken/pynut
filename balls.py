# -*- coding: utf-8 -*-

import paths
import nltk
from nltk import *

class Smegment:
    def __init__(self, tag, text):
        self.tag = tag
        self.text = text

def getParams(string, shouldExistList):
    for existString in shouldExistList:
        string = string.replace(existString.text, "")

    return string.split(',')

def check(smegmantique, shouldExistList):
    sentence = "("
    for removeString in ['(', ')']:
        smegmantique = smegmantique.replace(removeString, "")

    params = getParams(smegmantique, shouldExistList)
    for i, smegment in enumerate(shouldExistList):
        if smegment.tag == 'man' and smegment.text not in smegmantique:
            return -1

        sentence += smegment.text + ' ' + params[i] + ' '
  
    return sentence[:-1] + ")"

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
    #print(sentence)
    tokens = sentence.split()
    parser = parse.FeatureEarleyChartParser(grammar)
    trees = parser.parse(tokens)
    #nltk.draw.tree.draw_trees(tree)
    for index, tree in enumerate(trees):
        
        smegmantique = str(tree.label()['SEM'])
        #print(smegmantique)

        #Check all the rules
        jess_rule = check(smegmantique, [Smegment('opt', 'personnage'), Smegment('man', 'possede')])
        print(jess_rule)
        jess_rule = check(smegmantique, [Smegment('opt', 'cours'), Smegment('man', 'apprend')])
        print(jess_rule)

        #print(tree)
        if index == 0:
            sentenceTrace.append(destructure_sentence(tree.pos()))

#print(sentenceTrace)
