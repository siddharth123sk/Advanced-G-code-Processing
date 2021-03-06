pathForGcodeFile = (
    "D:/SMP/Singapore University of Technology and Design/Theo Victor Calais - Article/Article-2_Sleeve/Sleeve_Gcodes/191220_New Design of Gripper/191222/191220_New Design of Gripper/Sortaclear/bottom_del.gcode")


# location of text file, note the different '/' and '\'


def RemoveExtraSpaceBetweenLines(pathForGcodeFile):
    print("Started removing irrelevant spaces")
    textFile = open(pathForGcodeFile, 'r').read()
    with open(pathForGcodeFile, "w") as f:
        lines = textFile.split('\n')
        # print(lines)
        for line in lines:
            # print(line)
            if line != "":
                f.write(line)
                f.write('\n')
                # print(line)
                #print("Working")

    print("Successful")

RemoveExtraSpaceBetweenLines(pathForGcodeFile)

# def storeTextFile(pathForGcodeFile):
#     global textArray
#     textArray = []
#     textFile = open(pathForGcodeFile, 'r').read()
#     with open(pathForGcodeFile, "w") as f:
#         lines = textFile.split('\n')
#         # print(lines)
#         for line in lines:
#             #print(line)
#             textArray.append(line)
#     print(textArray)
#
# storeTextFile(pathForGcodeFile)


def CleanRepetitiveM7M9(pathForGcodeFile):
    global textArray
    textArray = []
    textFile = open(pathForGcodeFile, 'r').read()
    with open(pathForGcodeFile, "w") as f:
        lines = textFile.split('\n')
        # print(lines)
        for line in lines:
            # print(line)
            textArray.append(line)
    print(textArray)
    with open(pathForGcodeFile, "w") as f:
        lines = textFile.split('\n')
        text = lines
        # print(lines[1])
        lineNumber = -1
        countM7 = 0
        countM9 = 0
        stop = 0
        for line in lines:
            f.write(line)
            f.write('\n')
            lineNumber = lineNumber + 1
            print(line)
            if ((line[0:2] == 'M9')):
                for i in range(lineNumber, len(textArray)):
                    if stop == 0:
                        if ((textArray[i]) == 'M7'):
                            countM7 = countM7 + 1
                            M7location = i
                            stop = stop + 1

                        elif((textArray[i]) == 'M9'):
                            countM9 = countM9 + 1
                            M9location = i
                            stop = stop + 1
                if (M7location < M9location):
                    print("Repetitive M9 between line number ", end = "")
                    print(M9location, end = " ")
                    print("and", end = " ")
                    print(M7location, end = " ")
        # f.write(line)
        # f.write('\n')



CleanRepetitiveM7M9(pathForGcodeFile)
