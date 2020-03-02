pathForGcodeFile = (
    "D:/SMP/Singapore University of Technology and Design/Theo Victor Calais - Article/Article-2_Sleeve/Sleeve_Gcodes/191220_New Design of Gripper/191222/191220_New Design of Gripper/Sortaclear/bottom_del.gcode")

#location of text file, note the different '/' and '\'

textFile = open(pathForGcodeFile, 'r').read()
lines = textFile.split('\n')

def RemoveExtraSpaceBetweenLines(pathForGcodeFile):
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

RemoveExtraSpaceBetweenLines(pathForGcodeFile)


def CheckFor_Alternate_M7M9(pathForGcodeFile):
    textFile = open(pathForGcodeFile, 'r').read()
    with open(pathForGcodeFile, "w") as f:
        lines = textFile.split('\n')
        dataarray = []
        for line in lines:
            dataarray.append(line)
        #linenumber = 0
        #global linenumber
        # print(lines)
        for i in range(0, len(dataarray)):
            if dataarray[i] == 'M7':
                f.write('M7')
                f.write('\n')
                countM7 = 0
                for j in range(i, len(dataarray)):
                    if dataarray[j] == 'M7' and countM7 == 0:
                        if j == i + 1:
                            print("Check the line")
                            print(i + 1)



            elif dataarray[i] == 'M9':
                f.write('M9')
                f.write('\n')
                countM9 = 0
                for j in range(i+1, len(dataarray)):
                    if dataarray[j] == 'M9' and countM9 == 0:
                        if j == i + 1:
                            print("Check the line")
                            print(i + 1)

            else:
                f.write(dataarray[i])
                f.write('\n')

CheckFor_Alternate_M7M9(pathForGcodeFile)


def CheckFor_Missing_M7M9(pathForGcodeFile):
    textFile = open(pathForGcodeFile, 'r').read()
    with open(pathForGcodeFile, "w") as f:
        lines = textFile.split('\n')
        dataarray = []
        for line in lines:
            dataarray.append(line)
        #linenumber = 0
        #global linenumber
        # print(lines)
        for i in range(0, len(dataarray)):
            if dataarray[i] == 'M7':
                f.write('M7')
                f.write('\n')
                countM7 = 0
                for j in range(i+1, len(dataarray)):
                    if dataarray[j] != 'M9' and countM7 == 0:
                        countM7 = countM7 + 1
                        print("Check the line", end = " ")
                        print(i + 1, end = " ")
                        print("and", end = " ")
                        print(j + 1)




            elif dataarray[i] == 'M9':
                f.write('M9')
                f.write('\n')
                countM9 = 0
                for j in range(i+1, len(dataarray)):
                    if dataarray[j] == 'M9' and countM9 == 0:
                        if j == i + 1:
                            print("Check the line")
                            print(i + 1)

            else:
                f.write(dataarray[i])
                f.write('\n')

CheckFor_Missing_M7M9(pathForGcodeFile)