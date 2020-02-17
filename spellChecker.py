from spellchecker import SpellChecker

spell = SpellChecker()

def main():
    print("Spell Checker!")

def openFile(filename):
    with open(filename) as contentFile:
        fileList = contentFile.read().strip().split()
        return fileList


fileList = openFile("test.txt")
print(fileList)
# find those words that may be misspelled
misspelled = spell.unknown(fileList)

for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))

    # # Get a list of `likely` options
    # print(spell.candidates(word))
