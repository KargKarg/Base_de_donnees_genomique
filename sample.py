from Bio import Entrez
import xml.etree.ElementTree as ET

def donnees(liste_ids):

    Entrez.email = 'random@randint.com'
    attrib_names = [
        "host",
        "sample_type",
        "env_medium",
        "isolation_source",
        "host_disease",
        "geo_loc_name",
        "collection_date"
    ]

    texte = 'SampleID;' + ';'.join(attrib_names)
    texte += '\n'

    with open('Table/biosample.txt', 'w') as filout:

        for sample_id in liste_ids:

            handle = Entrez.esummary(db="biosample", id=sample_id)
            record = Entrez.read(handle)

            xml_data = record['DocumentSummarySet']['DocumentSummary'][0]['SampleData']
            root = ET.ElementTree(ET.fromstring(xml_data)).getroot()

            texte += f"{sample_id};"

            for i in range(len(attrib_names)):
                attribute_elem = root.find(".//Attribute[@harmonized_name='" + attrib_names[i] + "']")

                if attribute_elem is not None:
                    texte += f"{attribute_elem.text};"
                else:
                    texte += ';'

            texte += '\n'

        filout.write(texte)

