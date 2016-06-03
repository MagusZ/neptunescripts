#! /usr/bin/env python

# Ponemos env python para que lo encuentre en cualquier ordenador,
# sea donde sea que este instalado. 

DNASeq = "ATGAAC"

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
