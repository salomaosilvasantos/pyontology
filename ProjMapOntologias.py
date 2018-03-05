#!/usr/bin/env python

from owlready import *


#onto_path.append("teste3.owl")
#onto = get_ontology("https://github.com/salomaosilvasantos/pyontology/blob/master/teste3.owl")
#onto.load()
#owlready_ontology = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/owlready_ontology.owl").load()


#owlready_ontology = get_ontology("http://www.lesfleursdunormal.fr/static/_downloads/owlready_ontology.owl").load()
#ontologyInput =  get_ontology("pizza_onto.owl")

#ontologyInput.load()

#print(ontologyInput.classes)



onto = get_ontology("https://raw.githubusercontent.com/salomaosilvasantos/pyontology/master/pizza_onto.owl")
onto.load()
print(onto.classes)

