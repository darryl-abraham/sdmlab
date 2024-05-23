from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS, XSD
import pandas as pd

# Create a Graph
abox = Graph()

# Define Namespaces
url = Namespace("http://sdmlab2.org/")
abox.bind("url", url)

# Add ABox Data from .csv files

author = pd.read_csv('./data_preprocessed/author.csv')
for index, row in author.iterrows():
    abox.add((URIRef(url + str(row['Author_ID'])), url.hasName, Literal(row['name'], datatype=XSD.string)))

company_affiliation = pd.read_csv('./data_preprocessed/AUTHOR_AFFILIATED_COMPANY.csv')
for index, row in company_affiliation.iterrows():
    abox.add((URIRef(url + str(row['Author_ID'])), url.worksForCompany, URIRef(url + str(row['Company_ID']))))

company = pd.read_csv('./data_preprocessed/Company.csv')
for index, row in company.iterrows():
    abox.add((URIRef(url + str(row['Company_ID'])), url.companyName, Literal(row['name'], datatype=XSD.string)))

university_affiliation = pd.read_csv('./data_preprocessed/AUTHOR_AFFILIATED_UNIVERSITY.csv')
for index, row in university_affiliation.iterrows():
    abox.add((URIRef(url + str(row['Author_ID'])), url.worksForUniversity, URIRef(url + str(row['University_ID']))))

university = pd.read_csv('./data_preprocessed/University.csv')
for index, row in university.iterrows():
    abox.add((URIRef(url + str(row['University_ID'])), url.universityName, Literal(row['name'], datatype=XSD.string)))

authored = pd.read_csv('./data_preprocessed/AUTHORED.csv')
for index, row in authored.iterrows():
    abox.add((URIRef(url + str(row['Author_ID'])), url.wrotePaper, URIRef(url + str(row['Paper_ID']))))

cites = pd.read_csv('./data_preprocessed/CITES.csv')
for index, row in cites.iterrows():
    abox.add((URIRef(url + str(row['Cited_Paper_ID'])), url.citedBy, URIRef(url + str(row['Citing_Paper_ID']))))

paper = pd.read_csv('./data_preprocessed/Paper.csv')
for index, row in paper.iterrows():
    abox.add((URIRef(url + str(row['Paper_ID'])), url.hasTitle, Literal(row['title'], datatype=XSD.string)))
    abox.add((URIRef(url + str(row['Paper_ID'])), url.hasAbstract, Literal(row['abstract'], datatype=XSD.string)))
    abox.add((URIRef(url + str(row['Author_ID'])), url.correspondingAuthor, (URIRef(url + str(row['Paper_ID'])))))

review = pd.read_csv('./data_preprocessed/REVIEWED.csv')
for index, row in review.iterrows():
    abox.add((URIRef(url + str(row['Author_ID'])), url.wroteReview, URIRef(url + str(row['REVIEWED_ID']))))
    abox.add((URIRef(url + str(row['REVIEWED_ID'])), url.reviewOf, URIRef(url + str(row['Paper_ID']))))
    abox.add((URIRef(url + str(row['REVIEWED_ID'])), url.hasText, Literal(row['review_text'], datatype=XSD.string)))

reviewers = pd.read_csv('./data_preprocessed/Reviewer.csv')
for index, row in reviewers.iterrows():
    abox.add((URIRef(url + str(row['Author_ID'])), url.relevantAuthorOf, URIRef(url + str(row['relevantAuthorOf']))))

keyword = pd.read_csv('./data_preprocessed/Keyword.csv')
for index, row in keyword.iterrows():
    abox.add((URIRef(url + str(row['Keyword_ID'])), url.isWord, Literal(row['key'], datatype=XSD.string)))
    abox.add((URIRef(url + str(row['Keyword_ID'])), url.partOfTopic, (URIRef(url + str(row['Topic_ID'])))))
    abox.add((URIRef(url + str(row['Topic_ID'])), url.isAbout, Literal(row['topic'], datatype=XSD.string)))

haskeywords = pd.read_csv('./data_preprocessed/IS_ABOUT.csv')
for index, row in haskeywords.iterrows():
    abox.add((URIRef(url + str(row['Paper_ID'])), url.hasKeyword, URIRef(url + str(row['Keyword_ID']))))

publishedIn = pd.read_csv('./data_preprocessed/PUBLISHED_IN.csv')
for index, row in publishedIn.iterrows():
    abox.add((URIRef(url + str(row['Paper_ID'])), url.publishedIn, URIRef(url + str(row['Volume_ID']))))

volume = pd.read_csv('./data_preprocessed/Volume.csv')
for index, row in volume.iterrows():
    abox.add((URIRef(url + str(row['Volume_ID'])), url.volumeName, Literal(row['name'], datatype=XSD.string)))
    abox.add((URIRef(url + str(row['Volume_ID'])), url.publicationYear, Literal(row['year'], datatype=XSD.string)))
    abox.add((URIRef(url + str(row['Volume_ID'])), url.publishedByJournal, (URIRef(url + str(row['Journal_ID'])))))

journal = pd.read_csv('./data_preprocessed/Journal.csv')
for index, row in journal.iterrows():
    abox.add((URIRef(url + str(row['Journal_ID'])), url.journalName, Literal(row['name'], datatype=XSD.string)))

presentedAt = pd.read_csv('./data_preprocessed/PRESENTED_AT.csv')
for index, row in presentedAt.iterrows():
    abox.add((URIRef(url + str(row['Paper_ID'])), url.publishedInEdition, URIRef(url + str(row['Edition_ID']))))

proceeding = pd.read_csv('./data_preprocessed/Edition.csv')
for index, row in proceeding.iterrows():
    abox.add((URIRef(url + str(row['Edition_ID'])), url.publishedByConfWork, (URIRef(url + str(row['Conference_ID'])))))
    abox.add((URIRef(url + str(row['Edition_ID'])), url.heldIn, Literal(row['city'], datatype=XSD.string)))
    abox.add((URIRef(url + str(row['Edition_ID'])), url.publicationYear, Literal(row['year'], datatype=XSD.string)))

confwork = pd.read_csv('./data_preprocessed/Conference.csv')
for index, row in confwork.iterrows():
    abox.add((URIRef(url + str(row['Conference_ID'])), url.conferenceName, Literal(row['name'], datatype=XSD.string)))

# Serialize to ttl and save
turtle_data = abox.serialize(destination='abox.ttl', format='turtle')

