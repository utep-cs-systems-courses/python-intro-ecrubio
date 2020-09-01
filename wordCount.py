import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists

#Checking that the correct format is used when running the program.
#When running the file it should also have the input and output files in the argument
def argumentCheck():

    if len(sys.argv) is not 3:
        print("Correct usage: wordCount.py <input text file> <output file>")
        exit()
    else:
        inputFile = sys.argv[1]
        outputFile = sys.argv[2]

    return inputFile, outputFile

#Checking if the files provided in the arguments exist
def fileCheck(inputFile, outputFile):

    if not os.path.exists(inputFile):
        print ("text file input %s doesn't exist. Exiting" % inputFile)
        exit()

    if not os.path.exists(outputFile):
        print("output file %s doesn't exist. Exiting" % outputFile)
        exit()

#By creating a new dictionary and splitting the lines into words then inserting
#the word into dictionary and adding 1 to the count of the word
def openFile(mainFile):

    wordDict = {}
    
    with open(mainFile, 'r') as inputFile:
        for line in inputFile:
            #get rid of newline characters
            line = line.strip()
            #split line on whitespace and punctuation
            wordList = re.split('[ \t]', line)
            for word in wordList:
                word = word.lower()
                if word in wordDict.keys():
                    wordDict[word] += 1
                else:
                    wordDict[word] = 1
    print(wordDict)

def main():

    print("main")
    mainInput, mainOutput = argumentCheck()
    fileCheck(mainInput, mainOutput)
    openFile(mainInput)

if __name__ == '__main__':
    main()
