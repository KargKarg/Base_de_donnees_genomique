import pandas as pd
from Bio import Entrez
import assembly
import sample
import genomes


Entrez.email = 'random@randint.com'

#assembly.donnees('Staphylococcus xylosus', 100)

df1 = pd.read_csv('Table/assembly.txt', sep=';')

#sample.donnees(df1['BioSampleId'].tolist())

df2 = pd.read_csv('Table/biosample.txt', sep=';')

#genomes.donnes(df1['AssemblyAccession'])

df3 = pd.read_csv('Table/genomes.txt', sep=';')

genomes.telecharger(df3['Locus'].tolist(), df3['Contigs'].tolist())

"""Télécharger les genomes, CDS et protéines REFAIRE CONTIGS"""
