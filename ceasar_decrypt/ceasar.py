import json
import re
import time

def main():

    # define globals
    dictionary = list(json.loads(open('dict.json').read()) )
    phrase = userprompt()

    # utilize solve function and measure time elapsed
    start = time.time()
    solveKey = solve(phrase, dictionary)
    end = time.time()
    timeElapsed = end - start

    if solveKey:
        solvePhrase = encrypt(phrase, solveKey)
        print("\nPHRASE SOLVED IN " + str(round(timeElapsed, 7)) + " SECONDS:\n" + solvePhrase)
        print("\nENCRYPTION KEY: " + str(26 - solveKey) + "\n")
    else:
        print("ERROR: UNABLE TO SOLVE PHRASE, TIME ELAPSED: " + str(timeElapsed) )    

def solve(phrase, dictionary):
    """
    Usage: Takes in (phrase, dictionary) and returns the key to decrypt
    the string
    """
    # iterate for each possible key
    for i in range(26):
        # make new encryption with key i, break it into list of words
        newEncryption = encrypt(phrase, i)
        wordList = re.sub("[^\w]", " ",  newEncryption).split()

        # count number of english words
        counter = 0
        for word in wordList:
            newBool = binarySearch(dictionary, word.lower())
            if newBool:
                counter += 1

        # check if more than 20% are english words
        percentCorrect = counter / len(wordList)
        if percentCorrect > 0.45:
            return i
    return False

def userprompt():
    """
    Usage: Prompts user for key and phrase, no arguments
    required
    """
    phrase = input("Input the encrypted text: ")
    if not isinstance(phrase, str):
        exit("ERROR: Make sure phrase is a string")
    
    return phrase

def encrypt(phrase, key):
    """
    Usage: Enter unencrypted phrase and encryption key
    in format (phrase, key) to return encrypted phrase
    """
    newPhrase = ""

    for i in range(len(phrase)):
        char = phrase[i]

        if phrase[i].isupper():
            if ord(char) + key > 90:
                diff = 90 - (ord(char) + key)
                char = chr(64 + abs(diff) )
            else:
                char = chr(ord(char) + key)

        if phrase[i].islower():
            if ord(char) + key > 122:
                diff = 122 - (ord(char) + key)
                char = chr(96 + abs(diff) )
            else:
                char = chr(ord(char) + key)
        
        newPhrase += char

    return newPhrase

# def decrypt(phrase, key):
#     """
#     Usage: Enter unencrypted phrase and encryption key
#     in format (phrase, key) to return encrypted phrase
#     """
#     newPhrase = ""

#     for i in range(len(phrase)):
#         char = phrase[i]

#         if phrase[i].isupper():
#             if ord(char) - key < 65:
#                 diff = 65 - (ord(char) - key)
#                 char = chr(91 - abs(diff) )
#             else:
#                 char = chr(ord(char) - key)

#         if phrase[i].islower():
#             if ord(char) - key < 97:
#                 diff = 97 - (ord(char) - key)
#                 char = chr(123 - abs(diff) )
#             else:
#                 char = chr(ord(char) - key)
        
#         newPhrase += char

#     return newPhrase

def binarySearch(alist, item):
    """
    Usage: Searches list list for item, returns true
    if item is in alist (alist, item), and false
    otherwise
    """
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return (found)

if __name__ == "__main__":
    main()