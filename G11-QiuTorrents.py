from rdflib import Graph, Namespace, RDF, RDFS, Literal
from rdflib.namespace import XSD

# Create graph and namespace ----------------------------

g = Graph()

EX = Namespace("http://qiu-torrents-kg/biomedical/")
g.bind("", EX)
g.bind("rdf", RDF)
g.bind("rdfs", RDFS)

# RDFS MODEL / SCHEMA ----------------------------

# Classes
Drug = EX.Drug
Disease = EX.Disease

AntiInflammatory = EX.AntiInflammatory
Antibiotic = EX.Antibiotic

Inflammatory = EX.Inflammatory
Infectious = EX.Infectious

# Properties
Affects = EX.Affects
Treats = EX.Treats
Relieves = EX.Relieves
Worsens = EX.Worsens

# Class hierarchy
g.add((AntiInflammatory, RDFS.subClassOf, Drug))
g.add((Antibiotic, RDFS.subClassOf, Drug))

g.add((Inflammatory, RDFS.subClassOf, Disease))
g.add((Infectious, RDFS.subClassOf, Disease))

# Property hierarchy
g.add((Treats, RDFS.subPropertyOf, Affects))
g.add((Relieves, RDFS.subPropertyOf, Affects))
g.add((Worsens, RDFS.subPropertyOf, Affects))

# Domain and range only on the general property
g.add((Affects, RDFS.domain, Drug))
g.add((Affects, RDFS.range, Disease))

# FACTS FROM SECTION A ----------------------------

Ibuprofen = EX.Ibuprofen
Amoxicillin = EX.Amoxicillin

Arthritis = EX.Arthritis
BacterialInfection = EX.BacterialInfection
GastricUlcer = EX.GastricUlcer

# Drug types
g.add((Ibuprofen, RDF.type, AntiInflammatory))
g.add((Amoxicillin, RDF.type, Antibiotic))

# Drug-disease relations
g.add((Ibuprofen, Relieves, Arthritis))
g.add((Amoxicillin, Treats, BacterialInfection))
g.add((Ibuprofen, Worsens, GastricUlcer))

# 100 instances ----------------------------

anti_inflammatory_drugs = [
    "Aspirin", "Naproxen", "Diclofenac", "Celecoxib", "Ketoprofen",
    "Indomethacin", "Meloxicam", "Piroxicam", "Etodolac", "Sulindac",
    "Flurbiprofen", "Nabumetone", "MefenamicAcid", "Oxaprozin", "Tolmetin",
    "Lornoxicam", "Aceclofenac", "Dexibuprofen", "Fenoprofen", "TiaprofenicAcid"
]

antibiotic_drugs = [
    "Penicillin", "Azithromycin", "Ciprofloxacin", "Doxycycline", "Clarithromycin",
    "Cephalexin", "Levofloxacin", "Metronidazole", "Erythromycin", "Gentamicin",
    "Vancomycin", "Tetracycline", "Ceftriaxone", "Meropenem", "Linezolid",
    "Rifampicin", "Nitrofurantoin", "Clindamycin", "Ampicillin", "Trimethoprim"
]

inflammatory_diseases = [
    "RheumatoidArthritis", "Osteoarthritis", "Psoriasis", "CrohnsDisease", "UlcerativeColitis",
    "Tendinitis", "Bursitis", "Lupus", "Asthma", "Dermatitis",
    "Sinusitis", "Gout", "Vasculitis", "Myositis", "Spondylitis",
    "Conjunctivitis", "Pancreatitis", "Hepatitis", "Nephritis", "Carditis"
]

infectious_diseases = [
    "Pneumonia", "Tuberculosis", "UrinaryTractInfection", "Meningitis", "Cellulitis",
    "OtitisMedia", "StrepThroat", "Salmonellosis", "Cholera", "LymeDisease",
    "Gonorrhea", "Syphilis", "Sepsis", "Bronchitis", "Tonsillitis",
    "Impetigo", "BacterialSinusitis", "BacterialConjunctivitis", "WoundInfection", "Endocarditis"
]

ulcer_related_diseases = [
    "PepticUlcer", "DuodenalUlcer", "Esophagitis", "Gastritis", "GastrointestinalBleeding",
    "AcidReflux", "StomachIrritation", "Dyspepsia", "ColitisFlare", "IntestinalBleeding"
]

# Add drug instances
for drug in anti_inflammatory_drugs:
    g.add((EX[drug], RDF.type, AntiInflammatory))

for drug in antibiotic_drugs:
    g.add((EX[drug], RDF.type, Antibiotic))

# Add disease instances with specific subclasses
for disease in inflammatory_diseases:
    g.add((EX[disease], RDF.type, Inflammatory))

for disease in infectious_diseases:
    g.add((EX[disease], RDF.type, Infectious))

# Add extra disease instances only as Disease-related facts through inference
for disease in ulcer_related_diseases:
    g.add((EX[disease], RDF.type, Disease))

# Create relations
for i, drug in enumerate(anti_inflammatory_drugs):
    disease = inflammatory_diseases[i % len(inflammatory_diseases)]
    g.add((EX[drug], Relieves, EX[disease]))

for i, drug in enumerate(antibiotic_drugs):
    disease = infectious_diseases[i % len(infectious_diseases)]
    g.add((EX[drug], Treats, EX[disease]))

for i, drug in enumerate(anti_inflammatory_drugs[:10]):
    disease = ulcer_related_diseases[i % len(ulcer_related_diseases)]
    g.add((EX[drug], Worsens, EX[disease]))

# SERIALIZE TO TURTLE ----------------------------

output_file = "G11-QiuTorrents.ttl" 
g.serialize(destination=output_file, format="turtle")

print(f"Graph generated successfully: {output_file}")
print(f"Number of asserted triples: {len(g)}")