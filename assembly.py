from Bio import Entrez

def donnees(champ, limite):

    texte = "AssemblyAccession;AssemblyName;Strain;AssemblyStatus;ContigN50;ScaffoldN50;WGS;BioSampleId;Coverage;AsmReleaseDate_GenBank;SubmitterOrganization;Metagenome\n"
    categorie = texte.split(";")[:-1]
    Entrez.email = 'random@randint.com'
    handle = Entrez.esearch(db="assembly", term=champ, retmax=limite)
    record = Entrez.read(handle)

    for id in record['IdList']:

        esummary_handle = Entrez.esummary(db="assembly", id=id)
        esummary_record = Entrez.read(esummary_handle)

        for cle in categorie:
            if cle == 'Strain':
                try:
                    texte += f"{esummary_record['DocumentSummarySet']['DocumentSummary'][0]['Biosource']['InfraspeciesList'][0]['Sub_value']};"
                except IndexError:
                    texte += ';'
            else:
                texte += f"{esummary_record['DocumentSummarySet']['DocumentSummary'][0][cle]};"

        if len(esummary_record['DocumentSummarySet']['DocumentSummary'][0]['ExclFromRefSeq']) > 0 and 'metagenome' in esummary_record['DocumentSummarySet']['DocumentSummary'][0]['ExclFromRefSeq'][0]:
            texte += 'YES\n'

        else:
            texte += 'NO\n'

    with open("Table/assembly.txt", 'w') as filout:
        filout.write(texte)

donnees("Staphylococcus xylosus", 220)
