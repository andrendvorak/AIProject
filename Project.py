import nltk
import math
from random import randint

#Takes string input and returns array with each index another sentence
def tokenize(f):
    a = [] #Stores tokenized sentences
    start = 0 #Stores starting location
    current = 0 #Stores current location
    for q in f:
        if(q=='.' or q=='!' or q=='?'):
            a.append(f[start:current])
            start = current+2
        current += 1
    return a

#Takes array of sentences as input and returns array of how many nouns and verbs are in each sentence
def counting(f):
    z = [] #Stores output array
    current = 0 #Stores current position
    for sentence in tokenizedInput:
        numNouns = 0
        numVerbs = 0
        a = nltk.pos_tag(nltk.word_tokenize(sentence)) #Generate a tag for each word in sentence
        #Count number of nouns and verbs
        for word in a:
            if(word[1][0] == "N"):
                numNouns += 1
            elif(word[1][0] == "V"):
                numVerbs += 1
        #Add results to list
        z.append([])
        z[current].append(numNouns)
        z[current].append(numVerbs)
        z[current].append(-1) #Add -1 to store closest centroid value later on
        current += 1
    return z

#Takes counted input and number of sentences requested as input and returns the final summarized sentences as output
def clustering(cin, numCentroids):
    finalSentences = []
    minNoun, minVerb, maxNoun, maxVerb = cin[0][0], cin[0][1], cin[0][0], cin[0][1]
    for a in cin:
        if(a[0]<minNoun):
            minNoun = a[0]
        elif(a[0]>maxNoun):
            maxNoun = a[0]
        if(a[1]<minVerb):
            minVerb = a[1]
        elif(a[1]>maxVerb):
            maxVerb = a[1]
    #print("minNoun = " + str(minNoun) + " minVerb " + str(minVerb) + " maxNoun " + str(maxNoun) + " maxVerb " + str(maxVerb))
    centroidPosition = []
    count = 0
    #Initialize centroid position to be within bounds of numNouns and numVerbs
    for i in range(numCentroids):
        centroidPosition.append([])
        centroidPosition[count].append(randint(minNoun, maxNoun))
        centroidPosition[count].append(randint(minVerb, maxVerb))
        count += 1
    #Repeats k-means 10 times
    for i in range(10):
        #Loop through list to find closest centroid
        for n in cin:
            n[2] = closestNode(n, centroidPosition)
            #print(n) #Uncomment this line in order to print each node after every iteration
        currCluster = 0
        #Find mean to place centroids for next run
        for c in centroidPosition:
            totalN, totalV, count = 0, 0, 0
            #Iterates through the nodes
            for n in cin:
                if n[2] == currCluster: #if this node is in the current cluster
                    totalN = totalN + n[0]
                    totalV = totalV + n[1]
                    count += 1
            #Reassign centroid position to be mean of the nodes in that cluster
            try:
                c[0] = totalN/count
                c[1] = totalV/count
            except ZeroDivisionError: #No nodes in current cluster if this exception is met
                print()
            currCluster += 1
    #Iterates through final lists to find closest sentences
    currCluster, chosenNode = 0, 0
    for c in centroidPosition:
        count = 0
        minDistance = 10000 #Assign min distance to be large so it will be replaced
        for n in cin:
            if n[2] == currCluster: #If node is in cluster
                f = distance(n, c)
                if(f<minDistance):
                    minDistance = f
                    chosenNode = count
            count += 1
        if finalSentences.count(chosenNode) == 0:
            finalSentences.append(chosenNode) #Add node with minimum distance to the final sentences for output
        currCluster += 1
    return finalSentences

#Takes two points and returns the distance between them
def distance(i, c):
    dist = math.sqrt(((c[0]-i[0])**2) + ((c[1]-i[1])**2))
    return dist

#Takes current sentence position and centroid positions as input and returns what centroid is the closest
def closestNode(input, centroids):
    closestNode = -1
    count = 0
    closestDistance = distance(input, centroids[0])
    for c in centroids:
        f = distance(input, c)
        if(f<=closestDistance):
            closestDistance = f
            closestNode = count
        count += 1
    return closestNode

#MAIN PROGRAM STARTS HERE

#Open text file
with open(input("Enter a filename: "), 'r') as f:
    file = f.read()

percent = int(input("Percentage to keep (0-100): "))

#Tokenize input into sentences
tokenizedInput = tokenize(file)
print("Finished tokenization")

numSentences = int(len(tokenizedInput)*(percent/100))

countedInput = counting(tokenizedInput)
print("Finished counting")

'''for a in countedInput:
    print(a)'''

final = clustering(countedInput, numSentences)

#Print final output
for f in final:
    print(tokenizedInput[f])