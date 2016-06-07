#!/usr/bin/env python
import re

InFileName = 'Marrus_claudanielis.txt'

InFile = open( InFileName, 'r' )

LineNumber = 0

for Line in InFile:
	Line = Line.strip()

	if LineNumber > 0:
		ElementList = Line.split( '\t' )
		print( 'Depth:{} Lat:{} Lon:{}'.format( ElementList[4], ElementList[2], ElementList[3] ) )

		SearchString = '(\d+) ([\d\.]+) (\w)'
		Result	= re.search( SearchString, ElementList[2] )

		DegreeString = Result.group( 1 )
		MinuteString = Result.group( 2 )
		Compass = Result.group( 3 )

		print( DegreeString ) 
		print( MinuteString ) 
		print( Compass ) 

	LineNumber = LineNumber + 1

InFile.close()