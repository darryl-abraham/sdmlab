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
tbox.add((url.hasName, RDF.type, RDF.Property))
tbox.add((url.hasName, RDFS.domain, url.Author))
tbox.add((url.hasName, RDFS.range, XSD.string))
# Author works for
tbox.add((url.worksFor, RDF.type, RDF.Property))
tbox.add((url.worksFor, RDFS.domain, url.Author))
tbox.add((url.worksFor, RDFS.range, url.Organization))
tbox.add((url.worksForCompany, RDF.type, RDF.Property))
tbox.add((url.worksForCompany, RDFS.subPropertyOf, url.worksFor))
tbox.add((url.worksForCompany, RDFS.domain, url.Author))
tbox.add((url.worksForCompany, RDFS.range, url.Company))
tbox.add((url.worksForUniversity, RDF.type, RDF.Property))
tbox.add((url.worksForUniversity, RDFS.subPropertyOf, url.worksFor))
tbox.add((url.worksForUniversity, RDFS.domain, url.Author))
tbox.add((url.worksForUniversity, RDFS.range, url.University))
# Author authored
tbox.add((url.Authored, RDF.type, RDF.Property))
tbox.add((url.Authored, RDFS.domain, url.Author))
tbox.add((url.Authored, RDFS.range, url.Paper))
tbox.add((url.Authored, RDFS.range, url.Review))
tbox.add((url.wrotePaper, RDF.type, RDF.Property))
tbox.add((url.wrotePaper, RDFS.subPropertyOf, url.Authored))
tbox.add((url.wrotePaper, RDFS.domain, url.Author))
tbox.add((url.wrotePaper, RDFS.range, url.Paper))
tbox.add((url.wroteReview, RDF.type, RDF.Property))
tbox.add((url.wroteReview, RDFS.subPropertyOf, url.Authored))
tbox.add((url.wroteReview, RDFS.domain, url.Author))
tbox.add((url.wroteReview, RDFS.range, url.Review))
tbox.add((url.correspondingAuthor, RDF.type, RDF.Property))
tbox.add((url.correspondingAuthor, RDFS.subPropertyOf, url.Authored))
tbox.add((url.correspondingAuthor, RDFS.domain, url.Author))
tbox.add((url.correspondingAuthor, RDFS.range, url.Paper))
# Author relevant in
tbox.add((url.relevantAuthorOf, RDF.type, RDF.Property))
tbox.add((url.relevantAuthorOf, RDFS.domain, url.Author))
tbox.add((url.relevantAuthorOfConfWork, RDF.type, RDF.Property))
tbox.add((url.relevantAuthorOfConfWork, RDFS.range, url.ConfWork))
tbox.add((url.relevantAuthorOfJournal, RDF.type, RDF.Property))
tbox.add((url.relevantAuthorOfJournal, RDFS.range, url.Journal))

# Organization
# Company
tbox.add((url.Company, RDFS.subClassOf, url.Organization))
tbox.add((url.companyName, RDF.type, RDF.Property))
tbox.add((url.companyName, RDFS.subPropertyOf, url.orgName))
tbox.add((url.companyName, RDFS.domain, url.Company))
tbox.add((url.companyName, RDFS.range, XSD.string))
# University
tbox.add((url.University, RDFS.subClassOf, url.Organization))
tbox.add((url.universityName, RDF.type, RDF.Property))
tbox.add((url.universityName, RDFS.subPropertyOf, url.orgName))
tbox.add((url.universityName, RDFS.domain, url.University))
tbox.add((url.universityName, RDFS.range, XSD.string))

# Review
# Review of
tbox.add((url.reviewOf, RDF.type, RDF.Property))
tbox.add((url.reviewOf, RDFS.domain, url.Review))
tbox.add((url.reviewOf, RDFS.range, url.Paper))
# Review text
tbox.add((url.hasText, RDF.type, RDF.Property))
tbox.add((url.hasText, RDFS.domain, url.Review))
tbox.add((url.hasText, RDFS.range, XSD.string))

# Paper
# Paper title
tbox.add((url.hasTitle, RDF.type, RDF.Property))
tbox.add((url.hasTitle, RDFS.domain, url.Paper))
tbox.add((url.hasTitle, RDFS.range, XSD.string))
# Paper abstract
tbox.add((url.hasAbstract, RDF.type, RDF.Property))
tbox.add((url.hasAbstract, RDFS.domain, url.Paper))
tbox.add((url.hasAbstract, RDFS.range, XSD.string))
# Paper keywords + TOPICS
tbox.add((url.hasKeyword, RDF.type, RDF.Property))
tbox.add((url.hasKeyword, RDFS.domain, url.Paper))
tbox.add((url.hasKeyword, RDFS.range, url.Keyword))
tbox.add((url.isWord, RDF.type, RDF.Property))
tbox.add((url.isWord, RDFS.domain, url.Keyword))
tbox.add((url.isWord, RDFS.range, XSD.string))
tbox.add((url.partOfTopic, RDF.type, RDF.Property))
tbox.add((url.partOfTopic, RDFS.domain, url.Keyword))
tbox.add((url.partOfTopic, RDFS.range, url.Topic))
tbox.add((url.isAbout, RDF.type, RDF.Property))
tbox.add((url.isAbout, RDFS.domain, url.Topic))
tbox.add((url.isAbout, RDFS.range, XSD.string))
# Paper citation
tbox.add((url.citedBy, RDF.type, RDF.Property))
tbox.add((url.citedBy, RDFS.domain, url.Paper))
tbox.add((url.citedBy, RDFS.range, url.Paper))
# Paper published in
tbox.add((url.publishedIn, RDF.type, RDF.Property))
tbox.add((url.publishedIn, RDFS.domain, url.Paper))
tbox.add((url.publishedIn, RDFS.range, url.Collection))

tbox.add((url.publishedInProceeding, RDF.type, RDF.Property))
tbox.add((url.publishedInProceeding, RDFS.subPropertyOf, url.publishedIn))
tbox.add((url.publishedInProceeding, RDFS.domain, url.Paper))
tbox.add((url.publishedInProceeding, RDFS.range, url.Proceeding))
tbox.add((url.Proceeding, RDFS.subClassOf, url.Collection))

tbox.add((url.publishedInVolume, RDF.type, RDF.Property))
tbox.add((url.publishedInVolume, RDFS.subPropertyOf, url.publishedIn))
tbox.add((url.publishedInVolume, RDFS.domain, url.Paper))
tbox.add((url.publishedInVolume, RDFS.range, url.Volume))
tbox.add((url.Volume, RDFS.subClassOf, url.Collection))

# Published by
tbox.add((url.publishedBy, RDF.type, RDF.Property))
tbox.add((url.publishedBy, RDFS.domain, url.Collection))
tbox.add((url.publishedBy, RDFS.range, url.Publication))

tbox.add((url.publishedByConfWork, RDF.type, RDF.Property))
tbox.add((url.publishedByConfWork, RDFS.subPropertyOf, url.publishedBy))
tbox.add((url.publishedByConfWork, RDFS.domain, url.Proceeding))
tbox.add((url.publishedByConfWork, RDFS.range, url.ConfWork))
tbox.add((url.ConfWork, RDFS.subClassOf, url.Publication))

tbox.add((url.publishedByJournal, RDF.type, RDF.Property))
tbox.add((url.publishedByJournal, RDFS.subPropertyOf, url.publishedBy))
tbox.add((url.publishedByJournal, RDFS.domain, url.Volume))
tbox.add((url.publishedByJournal, RDFS.range, url.Journal))
tbox.add((url.Journal, RDFS.subClassOf, url.Publication))

# Volume
# Volume name
tbox.add((url.volumeName, RDF.type, RDF.Property))
tbox.add((url.volumeName, RDFS.domain, url.Volume))
tbox.add((url.volumeName, RDFS.range, XSD.string))
# Volume date
tbox.add((url.volumePublicationYear, RDF.type, RDF.Property))
tbox.add((url.volumePublicationYear, RDFS.domain, url.Volume))
tbox.add((url.volumePublicationYear, RDFS.range, XSD.int))

# Proceeding
# Proceeding date
tbox.add((url.proceedingPublicationYear, RDF.type, RDF.Property))
tbox.add((url.proceedingPublicationYear, RDFS.domain, url.Proceeding))
tbox.add((url.proceedingPublicationYear, RDFS.range, XSD.int))
# Proceeding city
tbox.add((url.heldIn, RDF.type, RDF.Property))
tbox.add((url.heldIn, RDFS.domain, url.Proceeding))
tbox.add((url.heldIn, RDFS.range, XSD.string))

# ConfWork
# ConfWork name
tbox.add((url.confworkName, RDF.type, RDF.Property))
tbox.add((url.confworkName, RDFS.domain, url.ConfWork))
tbox.add((url.confworkName, RDFS.range, XSD.string))
# ConfWork topic
tbox.add((url.confworkRelatedTo, RDF.type, RDF.Property))
tbox.add((url.confworkRelatedTo, RDFS.domain, url.ConfWork))
tbox.add((url.confworkRelatedTo, RDFS.range, url.Topic))

# Journal
# Journal name
tbox.add((url.journalName, RDF.type, RDF.Property))
tbox.add((url.journalName, RDFS.domain, url.Journal))
tbox.add((url.journalName, RDFS.range, XSD.string))
# Journal topic
tbox.add((url.journalRelatedTo, RDF.type, RDF.Property))
tbox.add((url.journalRelatedTo, RDFS.domain, url.Journal))
tbox.add((url.journalRelatedTo, RDFS.range, url.Topic))

# Serialize to .ttl and save
turtle_data = tbox.serialize(destination='MDS12-g6-B.1-TBOX-ABRAHAMWINTERS.ttl', format='turtle')

