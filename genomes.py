from Bio import Entrez


def donnes(liste_ids):

    Entrez.email = 'random@randint.com'

    colonnes = [
        'Genes(total)',
        'CDSs(total)',
        'CDSs(withprotein)',
        'tRNAs',
        'rRNAs',
        'ncRNAs'
    ]

    texte = "AssemblyAccession;GenomeID;Locus;Contigs;Genes;CDS;Proteine;tRNAs;rRNAs;ncRNAs\n"

    for accession in liste_ids:

        texte += f"{accession};"

        record = Entrez.read(Entrez.esearch(db="nuccore", term=accession, retmax=10000))

        if record['IdList']:

            informations = {}

            gid = record['IdList'][0]
            contigs = len(record['IdList']) - 1 ############ a refaire

            record = Entrez.efetch(db='nuccore', id=gid, rettype='gb').read()

            locus = record.split()[1][3:]

            texte += f"{gid};{locus};{contigs};"

            g = record.find('##Genome-Annotation-Data-START##')
            d = record.find('##Genome-Annotation-Data-END##')
            brut = record[g+len("##Genome-Annotation-Data-START##")+1:d].replace(' ', '')

            for info in brut.split('\n'):
                try:
                    informations[info.split('::')[0]] = info.split('::')[1].replace(',', '.')
                except IndexError:
                    pass

            for colonne in colonnes:

                try:
                    texte += f"{informations[colonne]};"
                except KeyError:
                    texte += 'None;'
        else:
            texte += 'None;None;None;None;None;None;None;None;None;'

        texte = texte[:-1] + '\n'

    with open('Table/genomes.txt', 'w') as filout:
        filout.write(texte[:-1])


def telecharger(liste_locus, liste_contigs):
    Entrez.email = 'random@randint.com'

    for i in range(len(liste_locus)):

        if str(liste_locus[i]) != 'nan':

            for j in range(int(liste_contigs[i])):

                if str(liste_contigs) != 'nan':
                    ############################## A REFAIRE
                    suivant = str(liste_locus[i])[:-len(str(liste_contigs[j]))] + str(liste_contigs[j])
                    print(suivant)