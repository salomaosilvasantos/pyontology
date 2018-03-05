#!/usr/bin/env python

from owlready import *

ontologyInput =  get_ontology("https://github.com/salomaosilvasantos/pyontology/blob/master/teste3.owl")

ontologyInput.load()

print(ontologyInput.classes)

