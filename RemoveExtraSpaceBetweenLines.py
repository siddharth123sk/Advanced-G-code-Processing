pathForGcodeFile = (
    "D:/SMP/Singapore University of Technology and Design/Theo Victor Calais - Article/Article-2_Sleeve/Sleeve_Gcodes/191220_New Design of Gripper/191222/191220_New Design of Gripper/Sortaclear/bottom.gcode")
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
