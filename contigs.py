from Bio import Entrez


def donnees(liste_locus, liste_contigs, liste_status, liste_genomes):

    Entrez.email = 'random@randint.com'

    for i in range(len(liste_locus)):

        locus = str(liste_locus[i])

        if locus != 'nan':

            for j in range(1, int(liste_contigs[i])+1):

                contigs = str(liste_contigs[i])

                if contigs == 'nan':
                    break

                if liste_status[i] == 'Complete Genome':
                    print(locus)
                    break

                contigs = locus[:-len(str(j))] + str(j)