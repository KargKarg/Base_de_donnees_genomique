import mysql.connector


def table() -> None:
    """

        Fonction qui crée les tables SQL permettant de stocker les données issues du scrapping NCBI.
        Le modèle entité association ainsi que le relationnel sont disponibles sur le fichier "schema.pdf".
        La connexion à Mysql est réalisée.

        Arguments:
            - None.

        Retour:
            - None.
    """
    login = mysql.connector.connect(user='admin', host='localhost', database='ncbi')
    cursor = login.cursor()

    requete = "DROP TABLE IF EXISTS Contigs;"
    cursor.execute(requete)

    requete = "DROP TABLE IF EXISTS Genomes;"
    cursor.execute(requete)

    requete = "DROP TABLE IF EXISTS Assembly;"
    cursor.execute(requete)

    requete = "DROP TABLE IF EXISTS Biosample;"
    cursor.execute(requete)

    requete = "CREATE TABLE Biosample(SampleID varchar(128), " \
              "host varchar(128), " \
              "sample_type varchar(128), " \
              "env_medium varchar(32), " \
              "isolation_source varchar(128), " \
              "host_disease varchar(128), " \
              "geo_loc_name varchar(128), " \
              "collection_date varchar(128),  " \
              "Primary key (SampleID));"
    cursor.execute(requete)

    requete = "CREATE TABLE Assembly(AssemblyAccession varchar(128), " \
              "AssemblyName varchar(128), " \
              "Strain varchar(128), " \
              "AssemblyStatus varchar(128), " \
              "Length int, " \
              "Contigs int, " \
              "ContigN50 int, " \
              "ScaffoldN50 int, " \
              "WGS varchar(128), " \
              "BioSampleId varchar(128), " \
              "Coverage int, " \
              "AsmReleaseDate_GenBank varchar(128), " \
              "SubmitterOrganization varchar(128), " \
              "Metagenome varchar(128), " \
              "Primary key (AssemblyAccession), " \
              "Foreign key (BioSampleId) references Biosample(SampleID) ON DELETE CASCADE ON UPDATE CASCADE);"
    cursor.execute(requete)

    requete = "CREATE TABLE Genomes(AssemblyAccession varchar(128), " \
              "GenomeID varchar(128), " \
              "Locus varchar(128), " \
              "Genes int, " \
              "CDS int, " \
              "Proteine int, " \
              "tRNAs int, " \
              "rRNAs varchar(128), " \
              "ncRNAs int, " \
              "Primary key (GenomeID), " \
              "Foreign key (AssemblyAccession) references Assembly(AssemblyAccession) ON DELETE CASCADE ON UPDATE CASCADE);"
    cursor.execute(requete)

    requete = "CREATE TABLE Contigs(GenomeID varchar(128), " \
              "ContigsID varchar(128), " \
              "Primary key (ContigsID), " \
              "Foreign key (GenomeID) references Genomes(GenomeID) ON DELETE CASCADE ON UPDATE CASCADE);"
    cursor.execute(requete)

    cursor.close()
    login.close()


def donnees() -> None:
    """

        Fonction qui remplie les tables avec les données récupérées grâce au scrapping de la NCBI.
        Les tables peuvent être ensuite utilisées.

        Arguments:
            - None.

        Retour:
            - None.
    """
    login = mysql.connector.connect(user='admin', host='localhost', database='ncbi')
    cursor = login.cursor()

    with open('Table/biosample.txt', 'r') as fil:
        fil.readline()
        for ligne in fil:
            ligne = ligne.split(';')
            data = '('
            for elem in ligne:
                elem = elem.replace('\n', '').replace('\'', '')
                data += f"\'{elem}\',"
            data = data[:-1] + ')'
            try:
                requete = "INSERT INTO Genomes VALUES " + data
                cursor.execute(requete)
            except:
                pass

    with open('Table/assembly.txt', 'r') as fil:
        fil.readline()
        for ligne in fil:
            ligne = ligne.split(';')
            data = '('
            for elem in ligne:
                elem = elem.replace('\n', '').replace('\'', '')
                if elem == '':
                    elem = 0
                data += f"\'{elem}\',"
            data = data[:-1] + ')'
            try:
                requete = "INSERT INTO Genomes VALUES " + data
                cursor.execute(requete)
            except:
                pass

    with open('Table/genomes.txt', 'r') as fil:
        fil.readline()
        for ligne in fil:
            ligne = ligne.split(';')
            data = '('
            for elem in ligne:
                elem = elem.replace('\n', '').replace('\'', '')
                if elem == '' or elem == 'None':
                    elem = 0
                data += f"\'{elem}\',"
            data = data[:-1] + ')'
            try:
                requete = "INSERT INTO Genomes VALUES " + data
                cursor.execute(requete)
            except:
                pass

    with open('Table/contigs.txt', 'r') as fil:
        fil.readline()
        for ligne in fil:
            ligne = ligne.split(';')
            data = '('
            for elem in ligne:
                elem = elem.replace('\n', '').replace('\'', '')
                data += f"\'{elem}\',"
            data = data[:-1] + ')'
            try:
                requete = "INSERT INTO Contigs VALUES " + data
                cursor.execute(requete)
            except:
                pass

    cursor.close()
    login.close()
