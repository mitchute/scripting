
import os

def write_flow_schedule(InitVal,Rate,outfile):
	# Init values
	Time = 0
	Value = InitVal
	# Header information
	outfile.write("Schedule:Day:Interval," + "\n")
	outfile.write("\t" + "Flow Fraction DaySchedule," + "\t" + "!-Name" + "\n")
	outfile.write("\t" + "Any Number," + "\t\t\t" + "!-Schedule Type Limits Name" + "\n")
	outfile.write("\t" + "Yes," + "\t\t\t\t" + "!-Interpolate to Timestep" + "\n")
	# Loop over all hours and minutes
	for hour in range(0,25):
		for min in range(0,60,10):
			# Sets first value correctly
			if hour == 0 and min == 0:
				continue
			# Sets last value correctly
			if hour == 24 and min == 0:
				# Time counter
				Time += 1
				# Write timestep information
				outfile.write("\t%02d:%02d,\t\t\t\t!- Time %i(hh:mm)\n" %(hour, min, Time))
				outfile.write("\t%0.3f;\t\t\t\t!- Value Until Time %i" %(Value, Time))
				break
			else:
				# Time counter
				Time += 1
				# Write timestep information
				outfile.write("\t%02d:%02d,\t\t\t\t!- Time %i(hh:mm)\n" %(hour, min, Time))
				outfile.write("\t%0.3f,\t\t\t\t!- Value Until Time %i\n" %(Value, Time))
			Value += Rate

def write_load_schedule(InitVal,Rate,outfile):
	# Init values
	Time = 0
	Value = InitVal
	# Header information
	outfile.write("Schedule:Day:Interval," + "\n")
	outfile.write("\t" + "Load Profile Day Schedule," + "\t" + "!-Name" + "\n")
	outfile.write("\t" + "Any Number," + "\t\t\t" + "!-Schedule Type Limits Name" + "\n")
	outfile.write("\t" + "Yes," + "\t\t\t" + "!-Interpolate to Timestep" + "\n")
	# Loop over all hours and minutes
	for hour in range(0,25):
		for min in range(0,60,10):
			# Sets first value correctly
			if hour == 0 and min == 0:
				continue
			# Sets last value correctly
			if hour == 24 and min == 0:
				# Time counter
				Time += 1
				# Write timestep information
				outfile.write("\t%02d:%02d,\t\t\t\t!- Time %i(hh:mm)\n" %(hour, min, Time))
				outfile.write("\t%0.2f;\t\t\t!- Value Until Time %i" %(Value, Time))
				break
			# For the rest of the time
			else:
				# Time counter
				Time += 1
				# Write timestep information
				outfile.write("\t%02d:%02d,\t\t\t\t!- Time %i(hh:mm)\n" %(hour, min, Time))
				outfile.write("\t%0.2f,\t\t\t!- Value Until Time %i\n" %(Value, Time))
			# Set value for next iteration
			Value += Rate

def write_schedules():
	# Open output file
	outfile = open('Schedules.txt', 'w')
	# Write flow schedule
	write_flow_schedule(0.0, 0.006993,outfile)
	# Add some blank lines
	outfile.write("\n\n")
	# Write load schedule
	write_load_schedule(0.0,-6293.71,outfile)
	# Close output file
	outfile.close()

write_schedules()
	
