import csv
import xlsxwriter
import math

# dictionary set up
dicty = {'A': '', 'B': '', 'E': '', 'V': ''}

# iterator & list set up
i = 0
content = []

# open trg.csv file for training
with open('trg.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    next(reader, None)
    for row in reader:
        content.append([row[1], row[2]])
file.close()

# set up probability of each class
aCount = 0
bCount = 0
eCount = 0
vCount = 0

# categorise each article
while i < len(content):
    if content[i][0] == 'A':
        aCount += 1
        a = dicty['A'] + content[i][1]
        dicty.update(A=a)
    elif content[i][0] == 'B':
        bCount += 1
        b = dicty['B'] + content[i][1]
        dicty.update(B=b)
    elif content[i][0] == 'E':
        eCount += 1
        e = dicty['E'] + content[i][1]
        dicty.update(E=e)
    elif content[i][0] == 'V':
        vCount += 1
        v = dicty['V'] + content[i][1]
        dicty.update(V=v)
    i += 1

# calculate priors
aPrior = aCount / 4000
bPrior = bCount / 4000
ePrior = eCount / 4000
vPrior = vCount / 4000

# list of stopwords
common_words = ["a", "about", "above", "across", "after", "afterwards",
                "again", "all", "almost", "alone", "along", "already", "also",
                "although", "always", "am", "among", "amongst", "amoungst",
                "amount", "an", "and", "another", "any", "anyhow", "anyone",
                "anything", "anyway", "anywhere", "are", "as", "at", "be",
                "became", "because", "become","becomes", "becoming", "been",
                "before", "behind", "being", "beside", "besides", "between",
                "beyond", "both", "but", "by","can", "cannot", "cant", "could",
                "couldnt", "de", "describe", "do", "done", "each", "eg",
                "either", "else", "enough", "etc", "even", "ever", "every",
                "everyone", "everything", "everywhere", "except", "few",
                "find","for","found", "four", "from", "further", "get", "give",
                "go", "had", "has", "hasnt", "have", "he", "hence", "her",
                "here", "hereafter", "hereby", "herein", "hereupon", "hers",
                "herself", "him", "himself", "his", "how", "however", "i", "ie",
                "if", "in", "indeed", "is", "it", "its", "itself", "keep",
                "least", "less", "ltd", "made", "many", "may", "me",
                "meanwhile", "might", "mine", "more", "moreover", "most",
                "mostly", "much", "must", "my", "myself", "name", "namely",
                "neither", "never", "nevertheless", "next","no", "nobody",
                "none", "noone", "nor", "not", "nothing", "now", "nowhere",
                "of", "off", "often", "on", "once", "one", "only", "onto", "or",
                "other", "others", "otherwise", "our", "ours", "ourselves",
                "out", "over", "own", "part","perhaps", "please", "put",
                "rather", "re", "same", "see", "seem", "seemed", "seeming",
                "seems", "she", "should","since", "sincere","so", "some",
                "somehow", "someone", "something", "sometime", "sometimes",
                "somewhere", "still", "such", "take","than", "that", "the",
                "their", "them", "themselves", "then", "thence", "there",
                "thereafter", "thereby", "therefore", "therein", "thereupon",
                "these", "they", "this", "those", "though", "through",
                "throughout","thru", "thus", "to", "together", "too", "toward",
                "towards","under", "until", "up", "upon", "us","very", "was",
                "we", "well", "were", "what", "whatever", "when","whence",
                "whenever", "where", "whereafter", "whereas", "whereby",
                "wherein", "whereupon", "wherever", "whether", "which", "while",
                "who", "whoever", "whom", "whose", "why", "will", "with",
                "within", "without", "would", "yet", "you", "your", "yours",
                "yourself", "yourselves"]

# class A: remove duplicates, stopwords and order top 1,000 descending words
aTotal = 0
aWords = dicty['A'].split()
aFreq = {}
for word in aWords:
    if word in common_words:
        continue
    if word in aFreq:
        aFreq[word] += 1
        aTotal += 1
    else:
        aFreq[word] = 1
        aTotal += 1
aFreq = sorted(aFreq.items(), key=lambda x:x[1])
aFreq = aFreq[-1000:]

# class B: remove duplicates, stopwords and order top 1,000 descending words
bTotal = 0
bWords = dicty['B'].split()
bFreq = {}
for word in bWords:
    if word in common_words:
        continue
    if word in bFreq:
        bFreq[word] += 1
        bTotal += 1
    else:
        bFreq[word] = 1
        bTotal += 1
bFreq = sorted(bFreq.items(), key=lambda x:x[1])
bFreq = bFreq[-1000:]

# class E: remove duplicates, stopwords and order top 1,000 descending words
eTotal =0
eWords = dicty['E'].split()
eFreq = {}
for word in eWords:
    if word in common_words:
        continue
    if word in eFreq:
        eFreq[word] += 1
        eTotal += 1
    else:
        eFreq[word] = 1
        eTotal += 1
eFreq = sorted(eFreq.items(), key=lambda x:x[1])
eFreq = eFreq[-1000:]

# class V: remove duplicates, stopwords and order top 1,000 descending words
vTotal = 0
vWords = dicty['V'].split()
vFreq = {}
for word in vWords:
    if word in common_words:
        continue
    if word in vFreq:
        vFreq[word] += 1
        vTotal += 1
    else:
        vFreq[word] = 1
        vTotal += 1
vFreq = sorted(vFreq.items(), key=lambda x:x[1])
vFreq = vFreq[-1000:]

# total unique words across all classes
allWords = []
for word in aFreq:
    if word[0] in allWords:
        continue
    else:
        allWords.append(word[0])
for word in bFreq:
    if word[0] in allWords:
        continue
    else:
        allWords.append(word[0])
for word in eFreq:
    if word[0] in allWords:
        continue
    else:
        allWords.append(word[0])
for word in vFreq:
    if word[0] in allWords:
        continue
    else:
        allWords.append(word[0])
allWords = len(allWords)

# open tst.csv for testing
testingData = []
with open('tst.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    next(reader, None)
    for row in reader:
        testingData.append([row[1]])

# check if words from testing file in a, b, e & v dicts
# score each word for strongest class match
aFreq, bFreq, eFreq, vFreq = dict(aFreq), dict(bFreq), dict(eFreq), dict(vFreq)
finalA, finalB, finalE, finalV = 0, 0, 0, 0
k=0
l = 0
results = [['id', 'class']]
while k < len(testingData):
    for word in testingData[k]:
        word = word.split()
        aScore = math.log(aPrior)
        bScore = math.log(bPrior)
        eScore = math.log(ePrior)
        vScore = math.log(vPrior)
        for w in word:
            if w in dict(aFreq):
                aScore += math.log((aFreq[w]+1) / (aTotal+allWords))
            if w in dict(bFreq):
                bScore += math.log((bFreq[w]+1) / (bTotal+allWords))
            if w in dict(eFreq):
                eScore += math.log((eFreq[w]+1) / (eTotal+allWords))
            if w in dict(vFreq):
                vScore += math.log((vFreq[w]+1) / (vTotal+allWords))
        if -aScore > max(-bScore, -eScore, -vScore):
            results.append([l+1, 'A'])
            finalA += 1
        if -bScore > max(-aScore, -eScore, -vScore):
            results.append([l+1, 'B'])
            finalB += 1
        if -eScore > max(-aScore, -bScore, -vScore):
            results.append([l+1, 'E'])
            finalE += 1
        if -vScore > max(-aScore, -bScore, -eScore):
            results.append([l+1, 'V'])
            finalV += 1
        l+=1
        k+=1

# compare testing classification results to the training class probability
finalA = finalA / 1000
finalB = finalB / 1000
finalE = finalE / 1000
finalV = finalV / 1000

print(finalA, aPrior)
print(finalB, bPrior)
print(finalE, ePrior)
print(finalV, vPrior)

# set up .csv for results
with open('kben560.csv', 'wt', newline='') as outfile:
    writer = csv.writer(outfile)
    for row in results:
        writer.writerow([row[0],row[1]])
outfile.close()

print("Done!")
