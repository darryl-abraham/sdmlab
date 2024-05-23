from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS, XSD
import pandas as pd

# Create a Graph
abox = Graph()

# Define Namespaces
url = Namespace("http://sdmlab2.org/")
abox.bind("url", url)

# Add ABox Data from .csv files

author = pd.read_csv('author.csv')
for index, row in author.iterrows():
    abox.add((URIRef(url + row['Author_ID']), url.hasName, Literal(row['name'], datatype=XSD.string)))

company_affiliation = pd.read_csv('AUTHOR_AFFILIATED_COMPANY.csv')
for index, row in company_affiliation.iterrows():
    abox.add((URIRef(url + row['Author_ID']), url.worksForCompany, URIRef(url + row['Company_ID'])))

company = pd.read_csv('Company.csv')
for index, row in company.iterrows():
    abox.add((URIRef(url + row['Company_ID']), url.companyName, row['name']))

university_affiliation = pd.read_csv('AUTHOR_AFFILIATED_UNIVERSITY.csv')
for index, row in university_affiliation.iterrows():
    abox.add((URIRef(url + row['Author_ID']), url.worksForUniversity, URIRef(url + row['University_ID'])))

university = pd.read_csv('University.csv')
for index, row in university.iterrows():
    abox.add((URIRef(url + row['University_ID']), url.universityName, row['name']))

authored = pd.read_csv('AUTHORED.csv')
for index, row in authored.iterrows():
    abox.add((URIRef(url + row['Author_ID']), url.wrotePaper, URIRef(url + row['Paper_ID'])))

cites = pd.read_csv('CITES.csv')
for index, row in cites.iterrows():
    abox.add((URIRef(url + row['Cited_Paper_ID']), url.citedBy, URIRef(url + row['Citing_Paper_ID'])))

paper = pd.read_csv('Paper.csv')
for index, row in paper.iterrows():
    abox.add((URIRef(url + row['Paper_ID']), url.hasTitle, row['title']))
    abox.add((URIRef(url + row['Paper_ID']), url.hasAbstract, row['abstract']))
    abox.add((URIRef(url + row['Author_ID']), url.correspondingAuthor, (URIRef(url + row['Paper_ID']))))

review = pd.read_csv('REVIEWED.csv')
for index, row in review.iterrows():
    abox.add((URIRef(url + row['Author_ID']), url.wroteReview, URIRef(url + row['Review_ID'])))
    abox.add((URIRef(url + row['Review_ID']), url.reviewOf, URIRef(url + row['Paper_ID'])))
    abox.add((URIRef(url + row['Review_ID']), url.hasText, row['text']))

reviewers = pd.read_csv('Reviewer.csv')
for index, row in reviewers.iterrows():
    abox.add((URIRef(url + row['Author_ID']), url.relevantAuthorOf, URIRef(url + row['relevantAuthorOf'])))

keyword = pd.read_csv('Keyword.csv')
for index, row in keyword.iterrows():
    abox.add((URIRef(url + row['Keyword_ID']), url.isWord, row['word']))
    abox.add((URIRef(url + row['Keyword_ID']), url.partOfTopic, (URIRef(url + row['Topic_ID']))))
    abox.add((URIRef(url + row['Topic_ID']), url.isAbout, row['topic']))

haskeywords = pd.read_csv('IS_ABOUT.csv')
for index, row in haskeywords.iterrows():
    abox.add((URIRef(url + row['Paper_ID']), url.hasKeyword, URIRef(url + row['Keyword_ID'])))

publishedIn = pd.read_csv('PUBLISHED_IN.csv')
for index, row in publishedIn.iterrows():
    abox.add((URIRef(url + row['Paper_ID']), url.publishedIn, URIRef(url + row['Volume_ID'])))

volume = pd.read_csv('Volume.csv')
for index, row in volume.iterrows():
    abox.add((URIRef(url + row['Volume_ID']), url.volumeName, row['name']))
    abox.add((URIRef(url + row['Volume_ID']), url.publicationYear, row['year']))
    abox.add((URIRef(url + row['Volume_ID']), url.publishedByJournal, (URIRef(url + row['Journal_ID']))))

journal = pd.read_csv('Journal.csv')
for index, row in journal.iterrows():
    abox.add((URIRef(url + row['Journal_ID']), url.journalName, row['name']))

presentedAt = pd.read_csv('PRESENTED_AT.csv')
for index, row in presentedAt.iterrows():
    abox.add((URIRef(url + row['Paper_ID']), url.publishedInEdition, URIRef(url + row['Conference_ID'])))

proceeding = pd.read_csv('Edition.csv')
for index, row in proceeding.iterrows():
    abox.add((URIRef(url + row['Edition_ID']), url.publishedByConfWork, (URIRef(url + row['Conference_ID']))))
    abox.add((URIRef(url + row['Edition_ID']), url.heldIn, row['city']))
    abox.add((URIRef(url + row['Edition_ID']), url.publicationYear, row['year']))

confwork = pd.read_csv('Conference.csv')
for index, row in confwork.iterrows():
    abox.add((URIRef(url + row['Conference_ID']), url.conferenceName, row['name']))

# Serialize to ttl and save
turtle_data = abox.serialize(destination='abox.ttl', format='turtle')

