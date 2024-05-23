from rdflib import Graph, Namespace, URIRef, Literal, XSD
from rdflib.namespace import RDF, RDFS

# Create a Graph
tbox = Graph()

# Define Namespaces
url = Namespace("http://sdmlab2.org/")
tbox.bind("url", url)

# Add Ontology Data

# Author
# Author name
tbox.add((url.hasName, RDFS.domain, url.Author))
tbox.add((url.hasName, RDFS.range, XSD.string))
# Author works for
tbox.add((url.worksForCompany, RDFS.domain, url.Author))
tbox.add((url.worksForCompany, RDFS.range, url.Company))
tbox.add((url.worksForUniversity, RDFS.domain, url.Author))
tbox.add((url.worksForUniversity, RDFS.range, url.University))
# Author authored
tbox.add((url.Authored, RDFS.domain, url.Author))
tbox.add((url.wrotePaper, RDFS.subPropertyOf, url.Authored))
tbox.add((url.wrotePaper, RDFS.range, url.Paper))
tbox.add((url.wroteReview, RDFS.subPropertyOf, url.Authored))
tbox.add((url.wroteReview, RDFS.range, url.Review))
tbox.add((url.correspondingAuthor, RDFS.subPropertyOf, url.Authored))
tbox.add((url.correspondingAuthor, RDFS.range, url.Paper))
# Author relevant in
tbox.add((url.relevantAuthorOf, RDFS.domain, url.Author))
tbox.add((url.relevantAuthorOf, RDFS.range, url.ConfWork))
tbox.add((url.relevantAuthorOf, RDFS.range, url.Journal))

# Organization
# Company
tbox.add((url.worksForCompany, RDFS.subPropertyOf, url.worksFor))
tbox.add((url.Company, RDFS.subClassOf, url.Organization))
tbox.add((url.companyName, RDFS.subPropertyOf, url.orgName))
tbox.add((url.companyName, RDFS.domain, url.Company))
tbox.add((url.companyName, RDFS.range, XSD.string))
# University
tbox.add((url.worksForUniversity, RDFS.subPropertyOf, url.worksFor))
tbox.add((url.University, RDFS.subClassOf, url.Organization))
tbox.add((url.universityName, RDFS.subPropertyOf, url.orgName))
tbox.add((url.universityName, RDFS.domain, url.University))
tbox.add((url.universityName, RDFS.range, XSD.string))

# Review
# Review of
tbox.add((url.reviewOf, RDFS.domain, url.Review))
tbox.add((url.reviewOf, RDFS.range, url.Paper))
# Review text
tbox.add((url.hasText, RDFS.domain, url.Review))
tbox.add((url.hasText, RDFS.range, XSD.string))

# Paper
# Paper title
tbox.add((url.hasTitle, RDFS.domain, url.Paper))
tbox.add((url.hasTitle, RDFS.range, XSD.string))
# Paper abstract
tbox.add((url.hasAbstract, RDFS.domain, url.Paper))
tbox.add((url.hasAbstract, RDFS.range, XSD.string))
# Paper keywords + TOPICS
tbox.add((url.hasKeyword, RDFS.domain, url.Paper))
tbox.add((url.hasKeyword, RDFS.range, url.Keyword))
tbox.add((url.isWord, RDFS.domain, url.Keyword))
tbox.add((url.isWord, RDFS.range, XSD.string))
tbox.add((url.partOfTopic, RDFS.domain, url.Keyword))
tbox.add((url.partOfTopic, RDFS.range, url.Topic))
tbox.add((url.isAbout, RDFS.domain, url.Topic))
tbox.add((url.isAbout, RDFS.range, XSD.string))
# Paper citation
tbox.add((url.citedBy, RDFS.domain, url.Paper))
tbox.add((url.citedBy, RDFS.range, url.Paper))
# Paper published in
tbox.add((url.publishedIn, RDFS.domain, url.Paper))
tbox.add((url.publishedIn, RDFS.range, url.Collection))
tbox.add((url.publishedInProceeding, RDFS.subPropertyOf, url.publishedIn))
tbox.add((url.publishedInProceeding, RDFS.range, url.Proceeding))
tbox.add((url.publishedInVolume, RDFS.subPropertyOf, url.publishedIn))
tbox.add((url.publishedInVolume, RDFS.range, url.Volume))
# ??
tbox.add((url.Proceeding, RDFS.subClassOf, url.Collection))
tbox.add((url.Volume, RDFS.subClassOf, url.Collection))

# Published by
tbox.add((url.publishedBy, RDFS.domain, url.Collection))
tbox.add((url.publishedBy, RDFS.range, url.Publication))
tbox.add((url.publishedByConfWork, RDFS.subPropertyOf, url.publishedBy))
tbox.add((url.PublishedByConfWork, RDFS.domain, url.Proceeding))
tbox.add((url.publishedByConfWork, RDFS.range, url.ConfWork))
tbox.add((url.publishedByJournal, RDFS.subPropertyOf, url.publishedBy))
tbox.add((url.publishedByJournal, RDFS.domain, url.Volume))
tbox.add((url.publishedByJournal, RDFS.range, url.Journal))
# ??
tbox.add((url.ConfWork, RDFS.subClassOf, url.Publication))
tbox.add((url.Journal, RDFS.subClassOf, url.Publication))

# Volume
# Volume name
tbox.add((url.volumeName, RDFS.domain, url.Volume))
tbox.add((url.volumeName, RDFS.range, XSD.string))
# Volume date
tbox.add((url.publicationYear, RDFS.domain, url.Volume))
tbox.add((url.publicationYear, RDFS.range, XSD.int))

# Proceeding
# Proceeding date
tbox.add((url.publicationYear, RDFS.domain, url.Proceeding))
tbox.add((url.publicationYear, RDFS.range, XSD.int))
# Proceeding city
tbox.add((url.heldIn, RDFS.domain, url.Proceeding))
tbox.add((url.heldIn, RDFS.range, XSD.string))

# Conference
# Conference name
tbox.add((url.conferenceName, RDFS.domain, url.ConfWork))
tbox.add((url.conferenceName, RDFS.range, XSD.string))

# Journal
# Journal name
tbox.add((url.journalName, RDFS.domain, url.Journal))
tbox.add((url.journalName, RDFS.range, XSD.string))

# Serialize to .ttl and save
turtle_data = tbox.serialize(destination='tbox.ttl', format='turtle')

