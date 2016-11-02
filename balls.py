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
    for existString in shouldExistList:
        string = string.replace(existString.text, "")

    return string.split(",")


def check(smegmantique, shouldExistList):
    sentence = "("
    for removeString in ["(", ")"]:
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
        nodeDef = "".join(str(node[1]).split())[1:-1].replace("[", "") #remove whitespaces and split for ','
        nodeType = str(node[1]).split("'")[1]
        nodeDef = nodeDef.split("]")
        hasCategoryFlag = [s for s in nodeDef if "CAT=" in s] #only the words with a CAT flag
        category = ""
        if (len(hasCategoryFlag) > 0):
            category = hasCategoryFlag[0][:-1].split("'")[1]
        currentSentence.append((node[0], nodeType, category)) #(word, wordtype, category)

    return currentSentence


def check_rules(fileHandler, smegmantique):
    jess_rule = check(smegmantique, [Smegment("opt", "personnage"), Smegment("man", "possede")])
    if jess_rule != -1:
      fileHandler.write(jess_rule)

    jess_rule = check(smegmantique, [Smegment("opt", "cours"), Smegment("man", "apprend")])
    if jess_rule != -1:
      fileHandler.write(jess_rule)


def sentence_parser(sentences):
    curSentences = list(sentences)
    lastSubject = ""

    for sentenceIndex, sentence in enumerate(curSentences):
        tokens = sentence.split()
        trees = parser.parse(tokens)
        for treeIndex, tree in enumerate(trees):
            if (treeIndex == 0):
                destructured = destructure_sentence(tree.pos())
                for wordTuple in destructured:
                    word = wordTuple[0]
                    wordType = wordTuple[1]
                    category = wordTuple[2]
                    if (wordType == "NProp" and category == 'v'):
                        lastSubject = word
                    elif (wordType == "Pro"):
                        curSentences[sentenceIndex] = sentence.replace(word, lastSubject)
    return curSentences


# Grammar rules
with open (paths.DICTIONARY_FILE_PATH, "r") as myfile:
    grammaireText = myfile.read()

# Text source
with open (paths.STORY_FILE_PATH, "r") as myfile:
    textSource = myfile.read()

fileHandler = FileHandler(paths.FACTS_FILE_PATH)

grammar = grammar.FeatureGrammar.fromstring(grammaireText)
parser = parse.FeatureEarleyChartParser(grammar)
sentences = textSource.split(".")[:-1] #removes last item from list, an empty string because of last split
sentences = sentence_parser(sentences)

for sentence in sentences:
    tokens = sentence.split()
    trees = parser.parse(tokens)
    nltk.draw.tree.draw_trees(tree)
    for index, tree in enumerate(trees):
        check_rules(fileHandler, str(tree.label()["SEM"]))

fileHandler.dispose()
