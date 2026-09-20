import pickle
import os

def readFileToNodeBrain():
    global nodeBrain
    with open('saveFile.pkl', 'rb') as filePath:
        nodeBrain = pickle.load(filePath)

def writeNodeBrainToFile():
    global nodeBrain
    with open("saveFile.pkl", 'wb') as filePath:
        pickle.dump(nodeBrain, filePath)

nodeBrain = {}
         
def initialize():
    if os.path.isfile('saveFile.pkl'): #checks if saveFile already exists
        readFileToNodeBrain()
    else:
        nodeBrain[1] = {
            'question': 'Is it alive?',
            'childYes': 2,
            'childNo': 3 
            }
        nodeBrain[2] = {
            'answer': 'Elephant',
            }
        nodeBrain[3] = {
            'answer': 'Car'
            }
    global nodeBrainLength_CurrentRun
    nodeBrainLength_CurrentRun = len(nodeBrain)

def validateResponse(x):
    if x == 'y':
        return True
    elif x =='n':
        return True
    else:
        return False

def askQuestion(node):
    print(nodeBrain[node]['question'])
    while True == True:
        global response 
        response = input()
        if validateResponse(response) == True:
            break
        else:
            print("Response must be [y/n]")

def finalQuestion(node):
    print(f'Are you thinking of {nodeBrain[node]['answer']}?')
    while True == True:
        global response 
        response = input()
        if validateResponse(response) == True:
            break
        else:
            print("Response must be [y/n]")

initialize()
currentNodeID = 1
gameRunning = True
response = str()

while gameRunning == True:
    askQuestion(currentNodeID)
    if response == 'y':
        currentNodeID = nodeBrain[currentNodeID]['childYes']
    elif response == 'n':
        currentNodeID = nodeBrain[currentNodeID]['childNo']
    if 'question' in nodeBrain[currentNodeID]:
        continue
    else:
        finalQuestion(currentNodeID)
        if response == 'y':
            print("I win!")
            gameRunning = False
        elif response == 'n':
            print("You win. What where you thinking of?")
            newAnswer = input()
            print(f'What can I ask to tell the difference between "{newAnswer}" and "{nodeBrain[currentNodeID]['answer']}"')
            newQuestion = input()
            print(f'If I ask "{newQuestion}" about "{newAnswer}" is the answer y or n?')
            while True == True:
                    newQuestionResponse = input()
                    if validateResponse(response) == True:
                        break
                    else:
                        print("Response must be [y/n]")
            print('Thank you!')
            nodeBrain[currentNodeID]['question'] = newQuestion
            nodeBrain[currentNodeID]['childYes'] = nodeBrainLength_CurrentRun + 1
            nodeBrain[currentNodeID]['childNo'] = nodeBrainLength_CurrentRun + 2
            if newQuestionResponse == 'y':
                nodeBrain[nodeBrainLength_CurrentRun + 1] = {'answer': newAnswer}
                nodeBrain[nodeBrainLength_CurrentRun + 2] = {'answer': nodeBrain[currentNodeID]['answer']}
            else:
                nodeBrain[nodeBrainLength_CurrentRun + 1] = {'answer': nodeBrain[currentNodeID]['answer']}
                nodeBrain[nodeBrainLength_CurrentRun + 2] = {'answer': newAnswer}
            writeNodeBrainToFile()
            gameRunning = False

                

        