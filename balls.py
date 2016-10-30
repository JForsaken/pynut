# -*- coding: utf-8 -*-

import paths
from filehandler import FileHandler
import nltk
from nltk import *

class Smegment:
    def __init__(self, tag, text):
        self.tag = tag
        self.text = text

def getParams(string, shouldExistList):
    #print(shouldExistList)
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

def check_rules(fileHandler, smegmantique):
    jess_rule = check(smegmantique, [Smegment('opt', 'personnage'), Smegment('man', 'possede')])
    fileHandler.write(jess_rule)
    jess_rule = check(smegmantique, [Smegment('opt', 'cours'), Smegment('man', 'apprend')])
    fileHandler.write(jess_rule)

# Grammar rules
with open (paths.DICTIONARY_FILE_PATH, "r") as myfile:
    grammaireText = myfile.read()

# Text source
with open (paths.STORY_FILE_PATH, "r") as myfile:
    textSource = myfile.read()

fileHandler = FileHandler(paths.FACTS_FILE_PATH)

grammar = grammar.FeatureGrammar.fromstring(grammaireText)
parser = parse.FeatureEarleyChartParser(grammar)
sentences = textSource.split('.')
sentenceTrace = []

for sentence in sentences:
    fileHandler.write(sentence)
    tokens = sentence.split()
    trees = parser.parse(tokens)
    #nltk.draw.tree.draw_trees(tree)

    for index, tree in enumerate(trees):
        check_rules(fileHandler, str(tree.label()['SEM']))
        #print(tree)

        if index == 0:
            sentenceTrace.append(destructure_sentence(tree.pos()))

fileHandler.dispose()
#print(sentenceTrace)
