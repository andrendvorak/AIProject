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

#Open text file
with open(input("Enter a filename: "), 'r') as f:
    file = f.read()

#Tokenize input into sentences
tokenizedInput = tokenize(file)
print("Finished tokenization")



#print("Finished cleaning")