from spellchecker import SpellChecker

spell = SpellChecker()

def main():
    print("Spell Checker!")
    print("What file would you like to spell check!")
    filename = input()
    listOfWords = openFile(filename)

    possibleMispelled = spell.unknown(listOfWords)
    print("Here are the possible mispelled words")
    print()
    for word in possibleMispelled:
        print(word, " and you might have meant ", spell.correction(word))

def openFile(filename):
    with open(filename) as contentFile:
        fileList = contentFile.read().strip().split()
        return fileList

if __name__ == "__main__":
    main()
