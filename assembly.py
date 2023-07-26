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
    colonnes = [
        "AssemblyAccession",
        "AssemblyName",
        "Strain",
        "AssemblyStatus",
        'Lenght',
        'Contigs',
        "ContigN50",
        "ScaffoldN50",
        "WGS",
        "BioSampleId",
        "Coverage",
        "AsmReleaseDate_GenBank",
        "SubmitterOrganization",
    ]
    texte = "AssemblyAccession;AssemblyName;Strain;AssemblyStatus;Length;Contigs;ContigN50;ScaffoldN50;WGS;BioSampleId;Coverage;AsmReleaseDate_GenBank;SubmitterOrganization;Metagenome\n"
    Entrez.email = 'random@randint.com'
    resultat = Entrez.read(Entrez.esearch(db="assembly", term=champ, retmax=limite))

    for accession in resultat['IdList']:

        esummary_resultat = Entrez.read(Entrez.esummary(db="assembly", id=accession))

        for colonne in colonnes:
            if colonne == 'Strain':
                try:
                    texte += f"{esummary_resultat['DocumentSummarySet']['DocumentSummary'][0]['Biosource']['InfraspeciesList'][0]['Sub_value']};"
                except IndexError:
                    texte += 'None;'

            elif colonne == 'Contigs':
                contigs = esummary_resultat['DocumentSummarySet']['DocumentSummary'][0]['Meta']
                txt_contigs_g = '<Stat category="contig_count" sequence_tag="all">'
                contigs = contigs[contigs.find(txt_contigs_g) + len(txt_contigs_g):]
                contigs = contigs[:contigs.find('</Stat>')]
                texte += f"{contigs};"

            elif colonne == 'Lenght':
                length = esummary_resultat['DocumentSummarySet']['DocumentSummary'][0]['Meta']
                txt_length_g = '<Stat category="total_length" sequence_tag="all">'
                length = length[length.find(txt_length_g) + len(txt_length_g):]
                length = length[:length.find('</Stat>')]
                texte += f"{length};"

            else:
                texte += f"{esummary_resultat['DocumentSummarySet']['DocumentSummary'][0][colonne]};"

        if len(esummary_resultat['DocumentSummarySet']['DocumentSummary'][0]['ExclFromRefSeq']) > 0 and 'metagenome' in esummary_resultat['DocumentSummarySet']['DocumentSummary'][0]['ExclFromRefSeq'][0]:
            texte += 'YES\n'

        else:
            texte += 'NO\n'

    with open("Table/assembly.txt", 'w') as filout:
        filout.write(texte)
