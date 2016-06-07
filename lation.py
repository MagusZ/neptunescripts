#! /usr/bin/env python

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

	

	else:
		print ("Skipping header")

	LineNumber = LineNumber + 1


InFile.close()