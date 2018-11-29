import nltk

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

#MAIN PROGRAM STARTS HERE

#Open text file
with open(input("Enter a filename: "), 'r') as f:
    file = f.read()

#Tokenize input into sentences
tokenizedInput = tokenize(file)
print("Finished tokenization")
countedInput = counting(tokenizedInput)
print("Finished counting")

for a in countedInput:
    print(a)