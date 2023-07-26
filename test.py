from Bio import Entrez

Entrez.email = 'random@randint.com'

record = Entrez.read(Entrez.esearch(db="nucleotide", term=f"GCF_024422955.1 chromosome", sort="relevance"))

print(record)
