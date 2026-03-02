# Generative AI–Driven Analysis of Research Trends in Biomedical Informatics

## Overview

Accurately characterizing research trends is critical for identifying emerging scientific breakthroughs and informing strategic research priorities. This repository provides a **generative AI–based pipeline** for large-scale retrospective analysis of scientific research domains, with a particular focus on **topic taxonomy construction, trend analysis, and topic evolution**.

As a case study, the pipeline is applied to **two decades (2004–2024) of keyword data from submissions to the *Journal of Biomedical Informatics (JBI)***, enabling systematic analysis of methodological innovations and health domain trends in biomedical informatics.

---

## Objectives

The goals of this project are to:

- Automatically construct **topic taxonomies** from large collections of manuscript keywords
- Distinguish and analyze **methodological innovations** and **health domain topics**
- Track **topic emergence, evolution, and decline** over time
- Analyze **keyword evolution within topics**
- Identify **co-occurring topics** and cross-cutting research themes
- Provide **quantitative and human-validated evaluations** of generated topic structures

---

## Methods

### Data Collection

- Keywords were collected from **all JBI submissions between 2004 and 2024**

### Topic Construction Pipeline

The pipeline leverages **large language models (LLMs)** to:

1. Categorize keywords into:
   - Methodological innovation topics
   - Health domain topics
2. Identify latent topics from keyword groupings
3. Assign interpretable topic names
4. Construct **hierarchical topic taxonomies**
5. Analyze temporal dynamics and topic relationships

### Automated Topic Evaluation

- Topic quality is assessed using **Medical Subject Headings (MeSH)** as an external knowledge base
- Keyword-derived MeSH terms are compared against:
  - MeSH terms assigned by the National Library of Medicine (NLM) for accepted publications

### Human Evaluation

- A structured human survey evaluates:
  - Topic name appropriateness
  - Interpretability of methodological and health domain topics

---

## Results

### Topic Statistics

**Methodological Innovations**
- 2,276 distinct topics
- Median of:
  - 6 keywords per topic (Q1: 2, Q3: 25)
  - 10 submissions per topic (Q1: 2, Q3: 60)

**Health Domains**
- 1,687 distinct topics
- Median of:
  - 6 keywords per topic (Q1: 2, Q3: 35)
  - 9 submissions per topic (Q1: 2, Q3: 71.75)

### Validation Findings

- Among **2,984 accepted JBI submissions**:
  - **85.1% (2,539)** show overlap between keyword-derived MeSH terms and NLM-assigned MeSH terms
- Human evaluation scores:
  - Methodological topic names: **3.78 / 5**
  - Health domain topic names: **4.19 / 5**

### Trend Analyses

The pipeline enables:
- Identification of prominent research areas
- Longitudinal analysis of submission volume by topic
- Keyword distribution shifts within topics
- Detection of co-occurring and interdisciplinary research themes

---

## Key Contributions

- A **generalizable, LLM-driven framework** for large-scale research trend analysis
- Automated construction and evaluation of **topic taxonomies**
- Integration of **external biomedical ontologies (MeSH)** for validation
- Empirical insights into the **evolution of biomedical informatics research** over 20 years

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

## Contact

For questions, collaboration, or extensions to other domains, please open an issue or contact the project maintainers.
