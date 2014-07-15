##This file mines the EnergyPlus input file for
##	files with plant and condenser loops

import glob

#Open output file
outfile = open('PlantFiles.csv', 'w')
outfile.write("Input Files" + ',' + "Plant Loops" + ',' + "Condenser Loops" + ',' + "Total Plant Loops" + '\n')


#Loops over all files in the current directory.
# Selects the idf files.
for datafile in glob.glob("*.idf"):
	plantCtr = 0
	condCtr = 0
	#Open each input file
	with open(datafile, 'r') as inF:
		#Loops over each line looking for 'PlantLoop' and
		#	'CondenserLoop'
		for line in inF:
			if 'PlantLoop,' in line:
				plantCtr += 1
			elif 'CondenserLoop,' in line:
				condCtr += 1
	totCtr = plantCtr + condCtr
	#Writes the data file, sans extension, to the output file
	if totCtr > 1:
		outfile.write(datafile[:-4] + ',' + str(plantCtr) + ',' + str(condCtr) + ',' + str(totCtr) + '\n')

#Close the output file.
outfile.close()