import requests
from xml.etree import ElementTree
import mysql.connector
import json

# Modify your parse_efetch_response and main function to insert records into the database


def perform_esearch(database, retmax, term):
    """Performs an eSearch query to PubMed."""
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": database,
        "retmax": retmax,
        "term": term
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.text
    except requests.HTTPError as http_err:
        print(f"ESearch request failed: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None

def perform_efetch(database, ids):
    """Performs an eFetch query to PubMed."""
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": database,
        "id": ",".join(ids),
        "retmode": "xml"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.text
    except requests.HTTPError as http_err:
        print(f"EFetch request failed: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None

def parse_efetch_response(response):
    root = ElementTree.fromstring(response)
    records = []
    for doc in root.iter("PubmedArticle"):
        record = {}
        pmid = doc.find(".//PMID").text
        article = doc.find(".//Article")
        record["Title"] = article.findtext(".//ArticleTitle")
        record["Abstract"] = article.findtext(".//AbstractText")
        authors = article.findall(".//Author")
        record["Authors"] = ", ".join([author.findtext(".//LastName") + " " + author.findtext(".//ForeName") for author in authors])
        record["Link"] = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"  # Construct the URL
        records.append(record)
    return records

def main():
    db_config = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "Madgame@1",  # Replace with your actual password
        "database": "bionexus_db_2"  # Replace with your actual database name
    }

    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        esearch_response = perform_esearch(database="pubmed", retmax=200, term="gene")
        if esearch_response:
            esearch_root = ElementTree.fromstring(esearch_response)
            id_list = [id_node.text for id_node in esearch_root.findall(".//Id")]
            if id_list:
                efetch_response = perform_efetch(database="pubmed", ids=id_list)
                if efetch_response:
                    records = parse_efetch_response(efetch_response)
                    for record in records:
                        insert_query = "INSERT INTO Articles (title, abstract, link) VALUES (%s, %s, %s)"
                        insert_values = (record.get("Title"), record.get("Abstract"), record.get("Link"))
                        cursor.execute(insert_query, insert_values)
                    connection.commit()
                    print("Records inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    main()
