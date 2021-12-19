
def getText(path, fileName):
    inputFile = path + "\\" + fileName
    txt = ""
    with open(inputFile, "r") as file_object:
        txt = file_object.read()
    return txt


# receives the input file and goes through the text file - it assumes that
# each line contains a word
# path: path to the folder containing the file - ".\" points to the current folder
# fileName: the name of the file
def getListOfWords(path, fileName):
    words = []
    inputFile = path + "\\" + fileName
    with open(inputFile, "r") as file_object:
        lines = file_object.read().splitlines()
        for _, line in enumerate(lines):
            words.append(line)
    return words