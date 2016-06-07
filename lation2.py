#! /usr/bin/env python
import re	#It creates an object where the package of Regular expressions are in Python

InFileName = 'Marrus_claudanielis.txt'

InFile = open (InFileName, 'r')	#opening the file to read it!

LineNumber = 0

for Line in InFile:
	Line = Line.strip()
	
	
	if LineNumber > 0:
		#print (LineNumber)
		#print (Line)
		ElementList = Line.split( '\t' )
		#print (ElementList)
		print ( 'Depth:{} Lat: {} Long: {}'.format (ElementList [4], ElementList [2], ElementList [3]))

		SearchString = '(\d+) ([\d\.]+) (\w)'
		Result = re.search( SearchString, ElementList[2] )	#in the regular epxpression library, search this re.
		print (Result.group ( 0 ))
		print (Result.group ( 1 ))
		print (Result.group ( 2 ))
		print (Result.group ( 3 ))
	
	LineNumber = LineNumber + 1


InFile.close()