#! /usr/bin/env python

# Ponemos env python para que lo encuentre en cualquier ordenador,
# sea donde sea que este instalado. 

#DNASeq = raw_input ("Enter a DNA sequence: ") #Prompts you to write stuff

DNASeq = "ATCACGAGCTTTATTATCGGGC"
DNASeq = DNASeq.upper()	#Takes DNASeq and creates a new string with an uppercase version of it

print ( "Sequence " + DNASeq)

SeqLength = float (len( DNASeq ))	#len cuenta las letras de una variable, es un integer

print ( "Length is " + str( SeqLength ) )	#str() dice que es un string lo que hay etre parentesis

# Si no ponemos str() el programa no funcionara pk no se pueden sumar strings e integers

Bases = "CGTA"


	
TotalStrong = 0
TotalWeak = 0

#Other option:

for Base in Bases:
	Count = DNASeq.count ( Base )
	Frequency = Count / SeqLength
	print( '{}: {:.2f}'.format( Base, Frequency ) )
	if Base in 'GC':
		TotalStrong = TotalStrong + Count
	elif Base in 'AT':
		TotalWeak = TotalWeak + Count
	else:
		print ("Unexpected nucleotide encountered")

print ('TotalWeak = ' +str (TotalWeak), 'TotalStrong = ' +str (TotalStrong))

