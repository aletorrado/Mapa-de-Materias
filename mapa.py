#!/usr/bin/env python
# coding: utf-8
# Este archivo usa el encoding: utf-8

# Copyright 2009 Alejandro Torrado
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.

import sys, os, csv
import optparse
try:
	from pygraphviz import *
except ImportError:
	print "Requiere el módulo \"pygraphviz\""
	sys.exit(1)

def generar_grafo(materias,cursadas,salida):
	colores = {"en final":"green","lista":"blue","cursable":"orange",\
													"no cursable":"red"}
	grafo = AGraph(directed=True) # Creo el grafo dirigido
	
	# proceso el programa de materias
	for archivo in materias.split(","):
		file_materias = open(archivo)
		csv_materias = csv.reader(file_materias)
		
		for linea in csv_materias:
			grafo.add_node(linea[0],color=colores["cursable"])
			for correlativa in linea[1:]:
				grafo.add_edge(correlativa,linea[0])
	file_materias.close()
	
	# proceso las etiquetas de las materias
	file_labels = open("label_materias.csv")
	csv_labels = csv.reader(file_labels)
	
	for linea in csv_labels:
		if grafo.has_node(linea[0]):
			grafo.get_node(linea[0]).attr["label"] = linea[0].decode("utf8")+"\\n"+linea[1].decode("utf8")
	file_labels.close()
			
	# proceso las materias cursadas
	file_cursadas = open(cursadas)
	csv_cursadas = csv.reader(file_cursadas)
	
	for linea in csv_cursadas:
		if len(linea)==0 or linea[0][0] == "#":
			continue
		nodo = grafo.get_node(linea[0])
		nodo.attr["color"]=colores[linea[1]]
	file_cursadas.close()
	
	# calculo estado de las otras materias
	for nodo in grafo:
		iterador = grafo.iterinedges(nodo)
		for vertice in iterador:
			nodo_correlativa = grafo.get_node(vertice[0])
			if nodo_correlativa.attr["color"] != colores["lista"]:
				nodo.attr["color"] = colores["no cursable"]
				break
	grafo.draw(salida,prog="dot")

def modo_interactivo():
	# proximamente
	parser.print_help()
	sys.exit(0)
	#~ return "materias.info.csv","ale.csv","grafo.png"
	

parser = optparse.OptionParser()
parser.add_option("-m", "--materias", dest="materias")
parser.add_option("-c", "--cursadas", dest="cursadas")
parser.add_option("-s", "--salida", dest="salida")
options, args = parser.parse_args()

for opcion in options.__dict__:
	if options.__dict__[opcion] == None:
		generar_grafo(*modo_interactivo())
		break
else:
	generar_grafo(options.materias,options.cursadas,options.salida)

parser.destroy()
