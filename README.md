# Biomedical Knowledge Graph

An RDF/RDFS knowledge graph for representing drugs, diseases, and clinically meaningful relationships such as treatment, symptom relief, and adverse effects.

## What it models

- Drug and disease entities with biomedical type hierarchies
- Anti-inflammatory and antibiotic drug categories
- Inflammatory and infectious disease categories
- Treatment, relief, and worsening relationships
- RDFS subclass, subproperty, domain, and range semantics

The generated graph includes a small curated example alongside synthetic biomedical entities and relations for exploring RDF/RDFS modelling patterns.

## Contents

- `G11-QiuTorrents.py` — creates and serializes the graph
- `G11-QiuTorrents.ttl` — generated Turtle dataset
- `SDM_KG_Lab.pdf` — project report

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python G11-QiuTorrents.py
```

Running the script regenerates `G11-QiuTorrents.ttl`.

## Author

Runxiao Qiu
