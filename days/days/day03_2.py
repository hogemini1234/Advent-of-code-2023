import uuid
savedCoords=[]
mappedCords = {}
mappedNbrs = {}
filename = "input/day03.txt"

def concat_coords(nbrA, nbrB):
    return str(nbrA)+"," + str(nbrB)

def save_coord(nbrA, nbrB):
    print("Saving coords " + concat_coords(nbrA, nbrB))
    savedCoords.append(concat_coords(nbrA, nbrB))

def map_coord(guid, nbrA, nbrB):
    print("Mapping coords " + concat_coords(nbrA, nbrB))
    mappedCords[concat_coords(nbrA, nbrB)] = guid    

def map_nbr_string(guid, nbrStr):
    mappedNbrs[guid] = nbrStr

def get_nbr_string(guid):
    if guid in mappedNbrs:
        return mappedNbrs[guid]
    else:
        return ""

def get_uuid_from_map(nbrA, nbrB):
    return mappedCords[concat_coords(nbrA, nbrB)]


def coordsExistsInList(nbrA, nbrB):
    if concat_coords(nbrA, nbrB) in savedCoords:
        return True
    else:
        return False

with open(filename) as file:    
    txtList = []
    while line := file.readline():
        line = line.rstrip()
        txtList.append([*line])

    combolist = [-1, 0, 1]
    noOfCols = len(txtList[0])
    noOfRows = len(txtList)
    print("noOfCols " + str(noOfCols))
    print("noOfRows " + str(noOfRows))

    for i in range(noOfRows):
        ud = ""
        lastCoordWasDigit = False
        for j in range(noOfCols):
            adjacentString = ""

            elm = txtList[i][j]
            print(elm)

            if elm.isdigit():
                if lastCoordWasDigit == False:
                    ud = str(uuid.uuid4())
                lastCoordWasDigit = True
                map_coord(ud, i, j)
                oldnbrstr = get_nbr_string(ud)
                newnbrstr = oldnbrstr + elm
                map_nbr_string(ud, newnbrstr)
            else:
                lastCoordWasDigit = False
    for key, val in mappedCords.items():
        print(key + " " + val)



with open(filename) as file: 
    summer = 0
    txtList = []
    while line := file.readline():
        line = line.rstrip()
        txtList.append([*line])

    combolist = [-1, 0, 1]
    noOfCols = len(txtList[0])
    noOfRows = len(txtList)
    print("noOfCols " + str(noOfCols))
    print("noOfRows " + str(noOfRows))

    for i in range(noOfRows):
        ud = ""
        lastCoordWasDigit = False
        for j in range(noOfCols):
            adjacentString = ""

            elm = txtList[i][j]

            if elm == '*':
                adjacentGuids = []
                for k_elm in combolist:
                    for l_elm in combolist:
                        rowcoord = i + k_elm
                        colcoord = j + l_elm
                        prtstring = ""
                        prtstring = "(" + str(k_elm) + ", " + str(l_elm) + ")" + "(" + str(rowcoord) + ", " + str(colcoord) + ")"
                        if rowcoord>=0 and rowcoord<noOfRows and colcoord>=0 and colcoord<noOfCols and not (k_elm==0 and l_elm==0):
                            adjacentString = txtList[rowcoord][colcoord]
                            if adjacentString.isdigit():
                                udd = get_uuid_from_map(rowcoord, colcoord)
                                if len(udd)>10:
                                    adjacentGuids.append(udd)
                            prtstring += " VALID " + txtList[rowcoord][colcoord]
                noDupesList = list(set(adjacentGuids))
                noOfUniqueGuids = len(noDupesList)


                if noOfUniqueGuids ==2:
                    guidA = noDupesList[0]
                    guidB = noDupesList[1]
                    summer += int(get_nbr_string(noDupesList[0]))*int(get_nbr_string(noDupesList[1]))

    print("ANSWER")
    print(summer)