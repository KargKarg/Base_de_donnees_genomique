with open('Table/biosample.txt', 'r') as fil:
    fil.readline()
    for ligne in fil:
        print("\'\'".join(ligne.split(";")))