import pandas as pd
from Bio import Entrez
import assembly
import contigs
import sample
import genomes


Entrez.email = 'random@randint.com'

#assembly.donnees('Staphylococcus xylosus', 100)

df1 = pd.read_csv('Table/assembly.txt', sep=';', dtype=str)

#sample.donnees(df1['BioSampleId'].tolist())

df2 = pd.read_csv('Table/biosample.txt', sep=';', dtype=str)

#genomes.donnees(df1['AssemblyAccession'].tolist(), df1['AssemblyStatus'].tolist())

df3 = pd.read_csv('Table/genomes.txt', sep=';', dtype=str)

fusion = pd.merge(df1, df3, on='AssemblyAccession')

contigs.donnees(fusion["Locus"].tolist(), fusion["Contigs"].tolist(), fusion['AssemblyStatus'].tolist(), fusion['GenomeID'].tolist())

"""Télécharger les genomes, CDS et protéines.
    Programmation système pour améliorer les performances.
    Faire avec le CLI une interface basique."""
