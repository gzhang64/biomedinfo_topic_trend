# Generative AI–Driven Analysis of Research Trends in Biomedical Informatics

## Overview

Accurately characterizing research trends is critical for identifying emerging scientific breakthroughs and informing strategic research priorities. This repository provides a **generative AI–based pipeline** for large-scale retrospective analysis of scientific research domains, with a particular focus on **topic taxonomy construction, trend analysis, and topic evolution**.

As a case study, the pipeline is applied to **keyword data from *Journal of Biomedical Informatics (JBI)* articles indexed in PubMed (2011–2025)**, enabling systematic analysis of methodological innovations and health domain trends in biomedical informatics.

---

## Objectives

The goals of this project are to:

- Automatically construct **topic taxonomies** from large collections of manuscript keywords
- Distinguish and analyze **methodological innovations** and **health domain topics**
- Track **topic emergence, evolution, and decline** over time
- Analyze **keyword evolution within topics**
- Identify **co-occurring topics** and cross-cutting research themes
- Provide **quantitative evaluations** of generated topic structures

---

## Repository Structure

| Notebook | Description |
|---|---|
| `00_download_data.ipynb` | Download JBI records from PubMed (E-utilities), keep articles with author keywords, and write `data/raw/jbi_pubmed_2011_2025_w_keywords.csv` |
| `01_data_preprocessing.ipynb` | Normalize keywords, classify them into methodological (`M_group`) vs. health (`H_group`) domains with an LLM, and build keyword–PMID mappings |
| `02_topic_extraction.ipynb` | Embed and cluster keywords, name topics, build hierarchical taxonomies, and compute topic relationships |

---

## Methods

### Data Collection

- JBI articles are retrieved from **PubMed** for publication years **2001–2025**
- Analysis uses the subset of articles that include author keywords, which spans **2011–2025** (`data/raw/jbi_pubmed_2011_2025_w_keywords.csv`; *n* = 2,427)

### Topic Construction Pipeline

The pipeline leverages **large language models (LLMs)** and sentence embeddings to:

1. Categorize keywords into:
   - Methodological innovation topics
   - Health domain topics
2. Cluster keywords into latent topics
3. Assign interpretable topic names
4. Construct **hierarchical topic taxonomies**
5. Analyze temporal dynamics and topic relationships

### Automated Topic Evaluation

- Topic quality is assessed using **Medical Subject Headings (MeSH)** as an external knowledge base
- Keyword-derived MeSH terms are compared against:
  - MeSH terms assigned by the National Library of Medicine (NLM) for accepted publications


## Key Contributions

- A **generalizable, LLM-driven framework** for large-scale research trend analysis
- Automated construction and evaluation of **topic taxonomies**
- Integration of **external biomedical ontologies (MeSH)** for validation
- Empirical insights into the **evolution of biomedical informatics research** from 2011 to 2025

---

## Use Cases

- Meta-research and scientometrics
- Editorial and strategic planning
- Policy and funding landscape analysis
- Early detection of emerging research areas
- Retrospective analysis of scientific fields beyond biomedicine

---

## Reproducibility and Ethics

- Analyses are conducted at the **aggregate topic level**
- Designed for retrospective, descriptive analysis of research trends

---

## Citation

If you use this code, please cite:

> Fang Y, Zhang G, Tejada SS, Chen F, Shortliffe E, Patel VL, Peleg M, Weng C. A data-driven method for research trend analysis in a scientific discipline: Application to the journal of biomedical informatics. J Biomed Inform. 2026 Jun;178:105013. doi: 10.1016/j.jbi.2026.105013. Epub 2026 Mar 14. PMID: 41839246; PMCID: PMC13032062.

Paper: https://www.sciencedirect.com/science/article/pii/S1532046426000377

---

## Contact

For questions, collaboration, or extensions to other domains, please open an issue or contact the project maintainers.
