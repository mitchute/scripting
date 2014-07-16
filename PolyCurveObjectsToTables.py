
def single_var_poly_curve_to_table(X_min, X_max, Interval, C_args = [], Input_Array = [], Output_Array = []):
	# This function takes a 1-D polynomial function of the form:
	#
	#       Y = C0 + C1*X + C2*X^2 + ... CN*X^N
	#
	# and returns tabular data over the range and interval specified.
	#
	# INPUT SYNTAX EXAMPLE
	# single_var_curve_to_table(X_min, X_max, Interval, C0, C1, C2, ... , CN)
	#       where: 
	#       X_min is the independent variable lower bound
	#       X_max is the independent variable upper bound
	#       C0-CN are a constants
			
	# Initial X Val
	X = X_min
	#Calculate Outputs
	while X <= X_max:
		power = 0
		Y = 0
		for CN in C_args:
			Y += (CN * pow(X,power))
			power += 1
		# Append to input/output arrays
		Input_Array.append(X)
		Output_Array.append(Y)
		
		# Increment poly function input value
		if X == X_max:
			break
		elif X + Interval > X_max:
			X = X_max
		else:
			X += Interval
	
def write_curve_table(Name, X_min, X_max, *Coeffs):
	outfile = open('Table.txt', 'w')
	# Definitions
	CN = []
	Input_Array = []
	Output_Array = []
	count = 0
	Prev_In_Val = ""
	# Get coefficients
	for i in Coeffs:
		CN.append(i)
	# Set interval
	Interval = float((X_max - X_min))/15.0
	# Calculate the curve outputs
	single_var_poly_curve_to_table(X_min, X_max, Interval, CN, Input_Array, Output_Array)
	
	# Write table
	outfile.write('Table:OneIndependentVariable,\n')
	outfile.write('%s\t\t\t\t!- Name\n' %(Name))
	if len(CN) == 2:
		outfile.write('Linear,\t\t\t\t!- Curve Type\n')
	elif len(CN) == 3:
		outfile.write('Quadratic,\t\t\t\t!- Curve Type\n')
	elif len(CN) == 4:
		outfile.write('Cubic,\t\t\t\t!- Curve Type\n')
	elif len(CN) == 5:
		outfile.write('Quartic,\t\t\t\t!- Curve Type\n')
	outfile.write('%0.2f,\t\t\t\t!- Minimum Value of X\n' % (X_min))
	outfile.write('%0.2f,\t\t\t\t!- Maximum Value of X\n' % (X_max))
	outfile.write('%0.2f,\t\t\t\t!- Minimum Table Output\n' % (Output_Array[0]))
	outfile.write('%0.2f,\t\t\t\t!- Maximum Table Output\n' % (Output_Array[-1]))
	outfile.write('Dimensionless,\t\t!- Input Unit Type for X\n')
	outfile.write('Dimensionless,\t\t!- Output Unit Type\n')
	outfile.write(',\t\t\t\t\t!- Normalization Reference\n')
	
	Array_Length = len(Input_Array)
	# Corrects for last and second to last outputs which are within tolerance
	if (Input_Array[-1] - Input_Array[-2]) < 0.01:
		Array_Length -= 2
	
	while count <= Array_Length:	
		In_Val = ('%0.2f' %(Input_Array[count]))
		Out_Val = ('%0.2f' %(Output_Array[count]))
		
		if count == Array_Length:
			outfile.write('%s,\t\t\t\t!- X Value #%i\n' % (In_Val, (count + 1)))
			outfile.write('%s;\t\t\t\t!- Output Value #%i\n' % (Out_Val, (count + 1)))
		else:
			outfile.write('%s,\t\t\t\t!- X Value #%i\n' % (In_Val, (count + 1)))
			outfile.write('%s,\t\t\t\t!- Output Value #%i\n' % (Out_Val, (count + 1)))
	
		count += 1 
	
	
	outfile.close()
	
	
	
	
	
write_curve_table("MyName", 1, 5, 0, 1, 1)


