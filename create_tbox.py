from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, RDFS

# Create a Graph
g = Graph()

# Define Namespaces
ex = Namespace("http://example.org/")
g.bind("ex", ex)

# Add Ontology Data
g.add((ex.Author, RDF.type, RDFS.Class))
g.add((ex.hasName, RDF.type, RDF.Property))
g.add((ex.Author, ex.hasName, RDFS.Literal))

# Serialize to Turtle
turtle_data = g.serialize(format='turtle')

# Write to TBox file
with open('example.ttl', 'wb') as f:
    f.write(turtle_data.encode())