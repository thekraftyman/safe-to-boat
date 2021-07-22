# matrix_operations.py
# By: thekraftyman

# A collection of matrix operations used by the main program

def matrix_average( matrix ):
	''' returns the average value of a matrix '''
	row_avgs = [ sum(row)/len(row) for row in matrix ]
	return sum(row_avgs) / len(row_avgs)

def get_submatrix( parent_matrix, start_row, start_col, end_row, end_col ):
	''' returns a matrix from parent matrix where returned matrix is a subset based on the start/end of the vars

	for example, if parent matrix:
		[[0,0,1,1,0],
		 [0,1,1,0,0],
		 [1,1,0,0,0],
		 [1,0,0,0,1],
		 [0,0,0,1,1]]

	then get_submatrix( matrix, 2, 1, 4, 3 ) would return:
		[[1,0,0],
		 [0,0,0],
		 [0,0,1]]
	'''

	nrows = len( parent_matrix )
	ncols = len( parent_matrix[0] )
	submatrix = []

	# check that our index coords are in the parent
	if start_row < 0 or start_row > nrows:
		raise Exception( 'start_row out of index of parent matrix' )

	if start_col < 0 or start_col > ncols:
		raise Exception( 'start_col out of index of parent matrix' )

	# check that we dont end up outside of the matrix, setting to limit if exceeded
	if end_row < 0:
		end_row = 0
	elif end_row > nrows:
		end_row = nrows

	if end_col < 0:
		end_col = 0
	elif end_col > nrows:
		end_col = nrows

	# get the row ranges used in the walk through the matrix
	if start_row < end_row:
		row_walk = range( start_row, end_row + 1 )
	elif start_row > end_row:
		row_walk = range( end_row, start_row + 1 )
	else:
		row_walk = [ start_row ]

	# get the column ranges used in the walk through the matrix
	if start_col < end_col:
		col_walk = range( start_col, end_col + 1 )
	elif start_col > end_col:
		col_walk = range( end_col, start_col + 1 )
	else:
		col_walk = range( start_col )

	# populate submatrix
	for row in row_walk:
		cur_row = []
		for column in col_walk:
			cur_row.append( parent_matrix[row][column] )
		submatrix.append( cur_row )

	# return the submatrix
	return submatrix
