from Bio import Entrez


def donnees(liste_locus: list, liste_contigs: list, liste_status: list, liste_genomes: list) -> None:
    """
        Fonction qui télécharge et parse les données de contigs d'une liste de d'IDs de génome.
        Sauvegarde les résultats sous format .txt avec séparateur ';' afin de pouvoir génèrer une table de ce texte.

        Les colonnes seront:

            - GenomeID
            - Contig

        Arguments:
            - liste_locus (list): correspond à la liste des locus de génome.
            - liste_contigs (list): correspond à la liste des contigs de génome.
            - liste_status (list): correspond à la liste des status de génome.
            - liste_genomes (list): correspond à la liste des GenomeID.

        Retour:
            - None.
    """
    texte = "GenomeID;Contigs\n"

    Entrez.email = 'random@randint.com'

    for i in range(len(liste_locus)):

        locus = str(liste_locus[i])

        if locus != 'nan':

            for j in range(1, int(liste_contigs[i])+1):

                contigs = str(liste_contigs[i])

                if contigs == 'nan':
                    break

                if liste_status[i] == 'Complete Genome':
                    texte += f"{liste_genomes[i]};{locus}\n"
                    break

                contigs = locus[:-len(str(j))] + str(j)

                texte += f"{liste_genomes[i]};{contigs}\n"

    with open('Table/contigs.txt', 'w') as filout:
        filout.write(texte)
