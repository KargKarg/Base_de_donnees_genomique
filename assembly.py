from Bio import Entrez


def donnees(champ: str, limite: int) -> None:
    """
    Fonction qui télécharge et parse les données d'assembly d'un taxon donné.
    Sauvegarde les résultats sous format .txt avec séparateur ';' afin de pouvoir génèrer une table de ce texte.

    Les colonnes seront:

        - AssemblyAccesion
        - AssemblyName
        - Strain
        - AssemblyStatus
        - ContigN50
        - ScaffoldN50
        - WGS
        - BioSampleID
        - Coverage
        - AsmReleaseDate_Genbank
        - SubmitterOrganization
        - Metagenome

    Arguments:
        - champ (str): Le nom du taxon.
        - limite (int): Le nombre limite de génomes à traiter.

    Retour:
        - None.
    """
    texte = "AssemblyAccession;AssemblyName;Strain;AssemblyStatus;ContigN50;ScaffoldN50;WGS;BioSampleId;Coverage;AsmReleaseDate_GenBank;SubmitterOrganization;Metagenome\n"

    categorie = texte.split(";")[:-1]
    Entrez.email = 'random@randint.com'
    resultat_brut = Entrez.esearch(db="assembly", term=champ, retmax=limite)
    resultat = Entrez.read(resultat_brut)

    for accession in resultat['IdList']:

        esummary_resultat_brut = Entrez.esummary(db="assembly", id=accession)
        essumary_resultat = Entrez.read(esummary_resultat_brut)

        for cle in categorie:
            if cle == 'Strain':
                try:
                    texte += f"{essumary_resultat['DocumentSummarySet']['DocumentSummary'][0]['Biosource']['InfraspeciesList'][0]['Sub_value']};"
                except IndexError:
                    texte += ';'
            else:
                texte += f"{essumary_resultat['DocumentSummarySet']['DocumentSummary'][0][cle]};"

        if len(essumary_resultat['DocumentSummarySet']['DocumentSummary'][0]['ExclFromRefSeq']) > 0 and 'metagenome' in essumary_resultat['DocumentSummarySet']['DocumentSummary'][0]['ExclFromRefSeq'][0]:
            texte += 'YES\n'

        else:
            texte += 'NO\n'

    with open("Table/assembly.txt", 'w') as filout:
        filout.write(texte)
