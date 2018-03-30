import os
import sys

def slices(s, positions):
    position = 0
    for length in positions:
        yield s[position:position + length]
        position += length


def convertFixedWidthToDemilited(textFilePath, textFileName, demiliter):

    with open(textFilePath+textFileName, 'r') as inFile, \
            open(textFilePath+textFileName.replace(".dat", "_comma.txt"), 'w') as outFile:
        lastLine = (inFile.readlines())[-1]
        inFile.seek(0)
        print(lastLine)
        for line in inFile:
            if line.startswith("lengths:"):
                positions = line[line.index("lengths:") + len("lengths:"):]
                print(positions)
                positions = [int(s) for s in positions.split(',')]
                print(positions)
                continue
            sliceData = slices(line, positions)
            outLine = ''
            for i in sliceData:
                outLine = outLine + i.strip() + demiliter
            outLine = outLine[:-1]
            if(line != lastLine):
                outLine = outLine + '\n'
            outFile.write(outLine)


# fixedWidthFilePath = "../data/test.dat"
# delimitedFilePath = "../data/testOut_comma.txt"
delimiter = ','
# convertFixedWidthToDemilited(fixedWidthFilePath, delimitedFilePath,delimiter)

strScriptLoc = str(os.getcwd())
strTextLocPhysical = os.path.join(strScriptLoc, str(sys.argv[1])) #feature text file path

textFilePath =  strTextLocPhysical + "/"
textFileList = os.listdir(strTextLocPhysical)
 
for textfile in textFileList:
    if textfile.endswith(".dat"):
        convertFixedWidthToDemilited(textFilePath,textfile, delimiter)
