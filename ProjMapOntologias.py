#!/usr/bin/env python

from owlready import *

ontologyInput =  get_ontology("http://github.com/salomaosilvasantos/pyontology/blob/master/conf.owl")

ontologyInput.load()

print(ontologyInput.classes)

