import nltk
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
        current += 1
    return z

#Takes counted input and number of sentences requested as input and returns the final summarized sentences as output
def clustering(cin, numCentroids):
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
    #for i in range(10):
    #    print(minNoun)

#MAIN PROGRAM STARTS HERE

#Open text file
with open(input("Enter a filename: "), 'r') as f:
    file = f.read()

percent = int(input("How much summarization? "))

#Tokenize input into sentences
tokenizedInput = tokenize(file)
print("Finished tokenization")

numSentences = int(len(tokenizedInput)*(percent/100))

countedInput = counting(tokenizedInput)
print("Finished counting")

for a in countedInput:
    print(a)

clustering(countedInput, numSentences)