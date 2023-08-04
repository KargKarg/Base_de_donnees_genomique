from Bio import Entrez


def donnees(liste_ids: list, liste_status: list) -> None:
    """
        Fonction qui télécharge et parse les données de génomes d'une liste de d'IDs.
        Sauvegarde les résultats sous format .txt avec séparateur ';' afin de pouvoir génèrer une table de ce texte.

        Les colonnes seront:

            - AssemblyAccession
            - GenomeID
            - Locus
            - Genes
            - CDS
            - Proteine
            - tRNAs
            - rRNAs
            - ncRNAs

        Arguments:
            - liste_ids (list): correspond à la liste des GenomeID.
            - liste_status (list): correspond à la liste des status de chaque génome.

        Retour:
            - None.
    """
    Entrez.email = 'random@randint.com'

    colonnes = [
        'Genes(total)',
        'CDSs(total)',
        'CDSs(withprotein)',
        'tRNAs',
        'rRNAs',
        'ncRNAs'
    ]

    texte = "AssemblyAccession;GenomeID;Locus;Genes;CDS;Proteine;tRNAs;rRNAs;ncRNAs\n"

    for i in range(len(liste_ids)):

        texte += f"{liste_ids[i]};"

        if liste_status[i] == 'Complete Genome':
            record = Entrez.read(Entrez.esearch(db="nuccore", term=f"{liste_ids[i]} chromosome", sort="relevance"))
        else:
            record = Entrez.read(Entrez.esearch(db="nuccore", term=f"{liste_ids[i]}", sort="relevance"))

        if record['IdList']:

            informations = {}

            gid = record['IdList'][0]

            record = Entrez.efetch(db='nuccore', id=gid, rettype='gb').read()

            access_id = record.split("ACCESSION")[1].split()[0][3:]

            g = record.find('##Genome-Annotation-Data-START##')
            d = record.find('##Genome-Annotation-Data-END##')
            brut = record[g+len("##Genome-Annotation-Data-START##")+1:d].replace(' ', '')

            for info in brut.split('\n'):
                try:
                    informations[info.split('::')[0]] = info.split('::')[1].replace(',', '.')
                except IndexError:
                    pass

            texte += f"{gid};{access_id};"

            for colonne in colonnes:

                try:
                    texte += f"{informations[colonne]};"
                except KeyError:
                    texte += 'None;'
        else:
            texte += 'None;None;None;None;None;None;None;None;'

        texte = texte[:-1] + '\n'

    with open('Table/genomes.txt', 'w') as filout:
        filout.write(texte[:-1])
