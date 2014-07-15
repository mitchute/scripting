
def single_var_curve_to_table(*args):
	# This function takes a 1-D polynomial function of the form:
	#
	#       Y = A + X1*X + X2*X^2 + ... XN*X^N
	#
	# and returns tabular data over the range and interval specified.
	#
	# INPUT SYNTAX EXAMPLE
	# single_var_curve_to_table(X_min, X_max, Interval, A, X1, X2, ... , XN)
	#       where: 
	#       X_min is the independent variable lower bound
	#       X_max is the independent variable upper bound
	#       A and X1-XN are a constants
        
	outfile = open('Schedules.txt', 'w')
	X_args = []
	B = 0
	# Number of arguments
	numArgs = len(args)
        
	# Input error handling
	if numArgs < 4:
		outfile.write("Insufficient input arguments. Function requires at least three [X_min, X_max, Interval]")
		print "Insufficient input arguments. Function requires at least three [X_min, X_max, Interval]"
		outfile.close()
		return
        
	# Initial inputs
	X_min = args[0]
	X_max = args[1]
	Interval = args[2]
        
	# Get Coefficients
	if numArgs > 3:
		# Get 'A' coefficient
		A = args[3]
		# Get 'X' coefficients
		if numArgs > 4:
			NumXArgs = numArgs - 4
			for i in range(NumXArgs):
				X_args.append(args[4 + i])
				
        # CALC OUTPUT VAL
        # Initial X Val
        x = X_min
        while i < X_max:
			Y = A
			print X_args
			for j in X_args:
				print j
                
			i += Interval
	outfile.close()
        
                
        
        
        
        
        
single_var_curve_to_table(1, 2, 3, 4, 5, 6, 7)
