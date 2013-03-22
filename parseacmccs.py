import skos
import rdflib
import os

# filename  = "ACMComputingClassificationSystemSKOSTaxonomy.xml"
# getbroaderconcept("ACMComputingClassificationSystemSKOSTaxonomy.xml",10011182 )
def getbroaderconcept(filename,conceptid):
	graph = rdflib.Graph()
	graph.load(filename)
	loader = skos.RDFLoader(graph)
	concept = loader["file://" + os.path.abspath(filename) + "#" + str(conceptid)]
	a = concept.broader.items()[0][1]
	print a.prefLabel.decode().title()
	return a