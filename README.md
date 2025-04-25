#  BioNexus: Biomedical Literature Mining System

**BioNexus** is a BERT-powered biomedical literature mining and tagging system built to address the challenge of retrieving and analyzing vast biomedical text corpora from sources like **PubMed**. This project integrates **natural language processing (NLP)**, **data visualization**, and **SQL-based knowledge storage** to support efficient and intelligent literature analysis.

---

##  Motivation

Biomedical researchers often face:
-  Information overload from ever-growing publication databases
-  Inefficient search and retrieval tools
-  Poor integration between literature and structured databases

BioNexus tackles these with a seamless NLP pipeline and smart storage/annotation capabilities.

---

## ⚙️ Features

-  **Named Entity Recognition** and **Keyword Tagging**
-  **Classification** and **Information Extraction** using **fine-tuned BERT**
-  Intuitive data exploration via interactive Jupyter notebooks
-  **SQLite backend** with clean **ERD-based schema** for articles, authors, keywords, and annotations
-  Future-ready security via token access and role-based tagging (roadmap)

---

##  Tech Stack

| Layer         | Tools Used                                  |
|---------------|----------------------------------------------|
| NLP Core      | `BERT`, `NLTK`, `spaCy`                     |
| Data Analysis | `pandas`, `matplotlib`, `seaborn`           |
| Backend DB    | `SQLite` with custom schema (SQLAlchemy)    |
| Interface     | `Jupyter Notebook`, Python APIs             |

---


---

##  Key Outcomes

- Built a pipeline that **extracts biomedical concepts** from abstracts
- Linked text with structured data storage via SQL
- Identified entities like diseases, genes, chemicals from **PubMed abstracts**
- Showcased ability to **scale literature mining** using NLP and cloud-friendly architecture

---

##  Try It Out

1. Install dependencies:
   ```bash
   pip install -r requirements.txt


