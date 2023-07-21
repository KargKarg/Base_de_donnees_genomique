import pandas as pd
import assembly
import sample
from Bio import Entrez

Entrez.email = 'random@randint.com'

# assembly.donnees('Staphylococcus xylosus', 100)

df1 = pd.read_csv('Table/assembly.txt', sep=';')

# sample.donnees(df1['BioSampleId'].tolist())

df2 = pd.read_csv('Table/biosample.txt', sep=';')

