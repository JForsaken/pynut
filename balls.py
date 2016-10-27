# -*- coding: utf-8 -*-

import paths
import nltk
from nltk import *

class Smegment:
    def __init__(self, tag, text):
        self.tag = tag
        self.text = text

def getParams(string, shouldExistList):
    print(shouldExistList)
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


# Grammar rules
with open (paths.DICTIONARY_FILE, "r") as myfile:
    grammaireText = myfile.read()

# Text source
with open (paths.STORY_FILE, "r") as myfile:
    textSource = myfile.read()

grammar = grammar.FeatureGrammar.fromstring(grammaireText)
parser = nltk.ChartParser(grammar)
sentences = textSource[:-1].split('.')
for sentence in sentences:
    print(sentence)
    tokens = sentence.split()
    parser = parse.FeatureEarleyChartParser(grammar)
    trees = parser.parse(tokens)
    #print(trees[0].node['SEM'])
    for tree in trees:
     #   print(tree.label().node['SEM'])
        #print(tree)
        #nltk.draw.tree.draw_trees(tree)
        smegmantique = str(tree.label()['SEM'])
        print(smegmantique)
        jess_rule = check(smegmantique, [Smegment('opt', 'personnage'), Smegment('man', 'possede')])
        print(jess_rule)
        #if ("possede" in smegmantique):
        #   paramX = smegmantique.replace("possede", "")
        #  paramX = paramX.replace("(", "")
           # paramX = paramX.replace(")", "")
            #paramX = paramX.split(',')
            #personnage = paramX[0]
            #objet = paramX[1]
            #sentence = "(personnage " + personnage + " possede objet " + objet + ")"
            #print(sentence)
                #if (semantique.find("poseede") == 0):
        #print(smegmantique.parse())
        #print(type(semantique))
        #semantiques = "possede slut sale"
        #boolean = "possede" in semantiques
        #print(boolean)
        #print(semantique)

        #for bleh in tree:
         #   print(bleh)
        #for bleh in tree:
         #   for ee in bleh:
          #      for ff in ee:
                    #print(ff)


