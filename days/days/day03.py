savedCoords=[]

def concat_coords(nbrA, nbrB):
    return str(nbrA)+"," + str(nbrB)

def save_coord(nbrA, nbrB):
    print("Saving coords " + concat_coords(nbrA, nbrB))
    savedCoords.append(concat_coords(nbrA, nbrB))

def coordsExistsInList(nbrA, nbrB):
    if concat_coords(nbrA, nbrB) in savedCoords:
        return True
    else:
        return False

with open("input/day03.txt") as file: 
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
        for j in range(noOfCols):
            adjacentString = ""

            elm = txtList[i][j]



            if elm.isdigit():
                for k_elm in combolist:
                    for l_elm in combolist:
                        rowcoord = i + k_elm
                        colcoord = j + l_elm
                        prtstring = ""
                        prtstring = "(" + str(k_elm) + ", " + str(l_elm) + ")" + "(" + str(rowcoord) + ", " + str(colcoord) + ")"
                        if rowcoord>=0 and rowcoord<noOfRows and colcoord>=0 and colcoord<noOfCols and not (k_elm==0 and l_elm==0):
                            adjacentString += txtList[rowcoord][colcoord]
                            prtstring += " VALID " + txtList[rowcoord][colcoord]

                strp = adjacentString.replace('.', '')
                strp = ''.join([i for i in strp if not i.isdigit()])


                if len(strp)>0 and coordsExistsInList(i, j)==False:
                    save_coord(i, j)

                    nbrStr = elm
                    lastElm = elm

                    jj = j
                    lastElmIsNumber = True

                    while lastElmIsNumber:
                        jj = jj-1
                        if jj>=0:
                            lastElm = txtList[i][jj]
                        else:
                            break
                        if lastElm.isdigit() and coordsExistsInList(i, jj)==False:
                            nbrStr = lastElm + nbrStr
                            lastElmIsNumber = True
                            save_coord(i, jj)
                        else:
                            lastElmIsNumber = False

                    jj = j
                    lastElmIsNumber = True
                    while lastElmIsNumber:
                        jj = jj+1
                        if jj<noOfCols:
                            lastElm = txtList[i][jj]
                        else:
                            break
                        if lastElm.isdigit() and coordsExistsInList(i, jj)==False:
                            nbrStr = nbrStr + lastElm
                            lastElmIsNumber = True
                            save_coord(i, jj)
                        else:
                            lastElmIsNumber = False

                    print("NUMBER " + nbrStr)       
                    summer += int(nbrStr)    

    print(summer)