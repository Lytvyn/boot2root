#!/usr/bin/env python3
import turtle
import sys

LARGEUR, HAUTEUR = 640, 480
POS_X = POS_Y = 50
NOM_IMAGE = "Turtle resolver"

if __name__ == '__main__':
	# open input file for reading the data
	with open(sys.argv[1], 'r') as file:
		contents = file.readlines()

	turtle.setup(LARGEUR, HAUTEUR, POS_X, POS_Y)
	print("largeur : {} px".format(turtle.window_width()))
	print("hauteur : {} px".format(turtle.window_height()))

	for line in contents:
		matchAvance = line.find('Avance') != -1
		matchTourneGaucheDe = line.find('Tourne gauche de') != -1
		matchTourneDroiteDe = line.find('Tourne droite de') != -1
		matchRecule = line.find('Recule') != -1
		if matchAvance:
			advance = line.split(' ')
			print ("avance", advance[1])
			turtle.fd(float(advance[1]))
		elif matchRecule:
			recule = line.split(' ')
			print ("recule", recule[1])
			turtle.bk(float(recule[1]))
		elif matchTourneDroiteDe:
			Tourne_droite = line.split(' ')
			print ("Tourne_droite", Tourne_droite[3])
			turtle.right(float(Tourne_droite[3]))
		elif matchTourneGaucheDe:
			Tourne_gauche = line.split(' ')
			print ("Tourne_gauche", Tourne_gauche[3])
			turtle.left(float(Tourne_gauche[3]))

	turtle.exitonclick()
