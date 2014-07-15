##This file mines the EnergyPlus input files 
## 	in the test directory for files with pumps.
##Pump outputs are appended and the file is
##  copied to another directory for later use.

import shutil, os

# Base path where Tests directory is located
basePath = 'D:\EnergyPlus\Projects\Plant_Pumps\Testing\Baseline\Tests'
newFolderName = 'NewInputFiles'

#Loops over all files in the current directory
for root, dirs, files in os.walk(basePath):
	for f in files:
		# Find all IDF files
		if os.path.splitext(f)[1] == '.idf':
			# Get the file path, strip, and split
			pathList = root.strip().split("\\")
			fullPath = root + "\\" + f
			# Get the new file name
			newFileName = pathList[-1] + ".idf"
			# New file path length
			newFilePathLen = len(pathList) - 2
			# Write new file path
			newFilePath = ''
			for i in range(0, newFilePathLen):
				newFilePath += pathList[i] + "\\"
			newFilePath += newFolderName + "\\" + newFileName
			#Open each input file
			inFile = open(fullPath, 'r')
			for line in inFile:
				if 'Pump:ConstantSpeed,' in line:
					shutil.copyfile(fullPath, newFilePath)
					outFile = open(newFilePath, 'a')
					print("Pump:ConstantSpeed found in: " + newFileName)
					outFile.write('Output:Variable,*,Pump Mass Flow Rate, hourly;')
					inFile.close()
					outFile.close()
					break
				elif 'Pump:VariableSpeed,' in line:
					shutil.copyfile(fullPath, newFilePath)
					outFile = open(newFilePath, 'a')
					print("Pump:VariableSpeed found in: " + newFileName)
					outFile.write('Output:Variable,*,Pump Mass Flow Rate, hourly;')
					inFile.close()
					outFile.close()
					break
			# Copy each file to another directory for later use
			