# This script mines the run time from any .err files in any directory
# below the current file location.
import os                                                                                          


def get_time(dir): 
	#Open output file
	outfile = open('MyRuntimes.csv', 'w')
	outfile.write("Input Files" + ',' + "EndOfFileStatus" + ',' + "Hours" + ',' + "Minutes" + ',' + "Seconds" + ',' + "Tot Seconds" + '\n')                                                                                     
	#Gets list of all sub-directories in current directory
	subdirs = [x[0] for x in os.walk(dir)]
	#Loop through all sub-directories
	for subdir in subdirs:
		#Splits the sub-directory into tokens
		subDirTokens = subdir.split('\\')
		#Gets list of files in sub-directory
		files = os.walk(subdir).next()[2]
		#Loop through all files in sub-directory
		for file in files:
			#Splits into file path and file extension
			fileName, fileExt = os.path.splitext(subdir + "\\" + file)
			#Finds all .err files
			if fileExt == '.err':
				#Creates the full file name
				fullFileName = (fileName + fileExt)
				#Skip the composite files
				if 'composite' in fullFileName:
					next
				#Open the rest of the files
				else:
					#Open the file in read-only
					with open(fullFileName, 'r') as readfile:
						#Read line by line until the last line is found
						for line in readfile:
							#Run completed successfully
							if 'EnergyPlus Completed Successfully' in line:
								#Strip the new line character
								line = line.replace("\n","")
								#Split the last line at the "=+ and take the right side
								timeString = line.split('=')[1]
								#Split time string into tokens
								timeStringTokens = timeString.split(' ')
								#Get the our from the first element in the timeStringTokenList
								hours = float(timeStringTokens[0][0:2])
								#Take the minutes from the seconde element in the timeStringTokenList
								minutes = float(timeStringTokens[1][0:2])
								#Grab the last element in the timeStringTokenList
								secondsTerm = timeStringTokens[-1]
								#Find the 's' in 'sec'
								secondsIndex = secondsTerm.index('s')
								#Take everything on the left of the 's'
								seconds = float(secondsTerm[0:(secondsIndex-1)])
								#Calculate total run time in seconds
								totalRunTimeSeconds = (hours * 3600) + (minutes * 60) + seconds
								#Write to the output file
								outfile.write(str(subDirTokens[-1]) + ',' "Success" + ',' + str(hours) + ',' + str(minutes) + ',' + str(seconds) + ',' + str(totalRunTimeSeconds) + "\n")	
							#For fatal error handling
							elif 'EnergyPlus Terminated--Fatal Error Detected' in line:
								outfile.write(str(subDirTokens[-1]) + ',' "Failed" + "\n")	
							#Next line if not the last line
							else:
								next
	#Close the output file.
	outfile.close()	
							
get_time(os.getcwd())


