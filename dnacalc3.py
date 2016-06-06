#! /usr/bin/env python

# Ponemos env python para que lo encuentre en cualquier ordenador,
# sea donde sea que este instalado. 

#DNASeq = raw_input ("Enter a DNA sequence: ") #Prompts you to write stuff

DNASeq = "ATCACGAGCTTTATTCGGGC"
DNASeq = DNASeq.upper()	#Takes DNASeq and creates a new string with an uppercase version of it

print ( "Sequence " + DNASeq)

SeqLength = float (len( DNASeq ))	#len cuenta las letras de una variable, es un integer

print ( "Length is " + str( SeqLength ) )	#str() dice que es un string lo que hay etre parentesis

# Si no ponemos str() el programa no funcionara pk no se pueden sumar strings e integers

NumberA = DNASeq.count('A')
NumberT = DNASeq.count("T")
NumberG = DNASeq.count("G")
NumberC = DNASeq.count("C")

print ("A: " + str( (NumberA / SeqLength) *100 ) +"%" )
print ("T: " + str( (NumberT / SeqLength) *100 ) +"%" )
print ("G: " + str( (NumberG / SeqLength) *100 ) +"%" )
print ("C: " + str( (NumberC / SeqLength) *100 ) +"%" )


print ("A: {:.5f}".format (NumberA / SeqLength))
print ("T: {}".format (NumberT / SeqLength))
print ("G: {}".format (NumberG / SeqLength))
print ("C: {}".format (NumberC / SeqLength))

TotalStrong = NumberG + NumberC
TotalWeak = NumberA + NumberT

if SeqLength <= 13:
	MeltTemp = (4 *TotalStrong) + (2*TotalWeak)
	#print ( "Melting Temp: {}".format(MeltTemp) )
	print ("Using short formula")

else:
	MeltTemp = 64.91 + 40 *(TotalStrong - 16.4) / SeqLength
	#print ( "Long Melting Temp: {}".format(MeltTemp) )
	print ("Using long formula")

print ( 'Melting temp: {}'.format(MeltTemp) )

print ("Done.")