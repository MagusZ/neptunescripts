#!/usr/bin/env python
import re

def decimalat(DegreeString):	#def defines a function
	# Converts a string for latitude or longitude into a float
	SearchString = '(\d+) ([\d\.]+) (\w)'
	Result	= re.search( SearchString, DegreeString )

	Degree = float( Result.group( 1 ) )
	Minute = float( Result.group( 2 ) )
	Compass = Result.group( 3 )
	DecimalDegree = Degree + Minute / 60

	if Compass in 'SW':
		DecimalDegree = - DecimalDegree

	return DecimalDegree	#This is the output (The point is to convert the string into a float)

assert (decimalat( '36 30.0 N') == 36.5) #Si mientes, el programa no funcionara. Assert bueno para pruebas!!
assert (decimalat( '36 30.0 S') == -36.5)
assert (decimalat( '36 30.0 W') == -36.5)

InFileName = 'Marrus_claudanielis.txt'

InFile = open( InFileName, 'r' )

LineNumber = 0

for Line in InFile:
	Line = Line.strip()

	if LineNumber > 0:
		ElementList = Line.split( '\t' )
		print( 'Depth:{} Lat:{} Lon:{}'.format( ElementList[4], ElementList[2], ElementList[3] ) )

		latitude = decimalat( ElementList[ 2 ] )

		print ( latitude )

		longitude = decimalat (ElementList [3])

		print (longitude)

	LineNumber = LineNumber + 1

InFile.close()