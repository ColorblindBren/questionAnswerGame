import json

# node type 0 = questionNode
# node type 1 = answerNode

#================== Intiializing nodeBrain and Starter File ==================#

node1 = {
    'question': 'Is it alive?',
    'childYes': '2',
    'childNo': '3'
    }

node2 = {
    'answer': 'Elephant'
    }

node3 = {
    'answer': 'Car'
    }

nodeBrain = {   
    'node1': node1,
    'node2': node2,
    'node3': node3
    }

#==============================================================================#

def readFileToNodeBrain():
    filePath = open('json.txt', 'r')
    nodeBrain = json.load(filePath)
    filePath.close()

def writeNodeBrainToFile():
    filePath = open('json.txt', 'w')
    json.dump(nodeBrain,filePath)
    filePath.close()

writeNodeBrainToFile()