# QBio Week 2 assignment
# Sept. 23, 2022
# Implement Needleman-Wunsch algorithm for DNA and AA alignment

from fasta import readFASTA
import numpy as np 
import sys

def count_gaps(seq):
	# Find length of longest gap
	gaps = [0]
	for i in seq:
		if i == '-':
			gaps[-1] += 1 
		else:
			# new gap
			if gaps[-1] != 0:
				gaps.append(0)
	gaps = [g for g in gaps if g != 0]
	return np.max(gaps), len(gaps)

# Print out number of gaps in first sequence, in 2nd, and score of final align

# Run 2x, once for DNA, once for protein
# Score HOX for DNA, BLOSUM for AA

if __name__ == '__main__':
	# get inputs
	fasta = sys.argv[1]
	scoring = sys.argv[2]
	gap_penalty = float(sys.argv[3])
	out = sys.argv[4]

	#######################
	### 1. PARSE INPUTS ###
	#######################

	# In future, could put more defensive programming; will not for this assignment
	if gap_penalty > 0:
		print('WARNING: Gap penalty is greater than 0')
	# Read in sequences
	input_sequences = readFASTA(open(fasta))

	seq1_id, seq1 = input_sequences[0]
	seq2_id, seq2 = input_sequences[1]

	# Parse in scoring matrix
	scoring_matrix = []
	letter2idx = dict() # Dict to convert letter (e.g ATCG) to index
	with open(scoring, 'r') as f:
		for i, line in enumerate(f.readlines()):
			# Need to ignore first line
			if i == 0:
				for idx, letter in enumerate(line.split()):
					letter2idx[letter] = idx # This will store row/column order
			else:
				scoring_matrix.append([float(v) for v in line.split()[1:]])
		# Save as array 
		scoring_matrix = np.array(scoring_matrix)
	f.close()
	##############################
	### 2. INITIALIZE MATRICES ###
	##############################

	F_matrix = np.zeros((len(seq1)+1, len(seq2)+1))
	traceback = np.zeros((len(seq1)+1, len(seq2)+1)) # Will contain L U or D

	# tracecode dictionary
	code2letter = dict({3:'L', 1:'U', 2:'D'}) # L is 3, U is 1, D is 2
	letter2code = dict({'L':3, 'U':1, 'D':2})

	# Fill in first col/row; code for F_matrix is from class. 
	for i in range(len(seq1)+1):
		F_matrix[i,0] = i*gap_penalty
		traceback[i,0] = letter2code['U']

	for j in range(len(seq2)+1):
		F_matrix[0,j] = j*gap_penalty
		traceback[0,j] = letter2code['L']

	traceback[0,0] = -1 # Signal that we reached the end

	###################
	### 3. POPULATE ###
	###################
	
	# code from class, supplemented/changed for traceback

	# Now that we've filled in the first row and column, we need
	# to go row-by-row, and within each row go column-by-column,
	# calculating the scores for the three possible alignments
	# and storing the maximum score
	for i in range(1, len(seq1)+1): # loop through rows
		for j in range(1, len(seq2)+1): # loop through columns
			align_score = scoring_matrix[letter2idx[seq1[i-1]], letter2idx[seq2[j-1]]] 
			
			d = F_matrix[i-1, j-1] + align_score
			h = F_matrix[i,j-1] + gap_penalty
			v = F_matrix[i-1,j] + gap_penalty

			score = max(d,h,v)
			if d == score:
				# Went with d
				traceback[i, j] = letter2code['D']
			elif h == score:
				# Went with h, have gap in seq 1
				traceback[i, j] = letter2code['L']
			else:
				traceback[i, j] = letter2code['U']

			F_matrix[i,j] = score
	# Assert all filled
	assert(np.sum(traceback==0)==0)
	############################
	### 4. OPTIMAL ALIGNMENT ###
	############################

	# Start at bottom right corner of F matrix
	align1 = ''
	align2 = ''

	# remember to reverse the sequences. 
	i = F_matrix.shape[0] - 1
	j = F_matrix.shape[1] - 1
	while i > 0 or j > 0:
		# Counting backwards
		if code2letter[traceback[i,j]] == 'D':
			# Diagonal
			align1 += seq1[i-1]
			align2 += seq2[j-1]
			i -= 1
			j -= 1
		elif code2letter[traceback[i,j]] == 'U':
			# Go up. That means gap in seq2
			align1 += seq1[i-1]
			align2 += '-'
			i -= 1
		elif code2letter[traceback[i,j]] == 'L':
			align1 += '-'
			align2 += seq2[j-1]
			j -= 1

	# Reverse
	align1 = align1[::-1]
	align2 = align2[::-1]

	print('Number of gaps in align 1: {}'.format(align1.count('-')))
	print('Number of gaps in align 2: {}'.format(align2.count('-')))

	print('Length of largest gap in align 1: {}'.format(count_gaps(align1)[0]))
	print('Length of largest gap in align 2: {}'.format(count_gaps(align2)[0]))

	print('Number of gaps (consecutive counted as 1 gap) in align 1: {}'.format(count_gaps(align1)[1]))
	print('Number of gaps (consecutive counted as 1 gap) in align 2: {}'.format(count_gaps(align2)[1]))

	print('Score of the alignment: {}'.format(F_matrix[-1,-1]))

	# Save 
	with open(out, 'w') as f:
		f.write('> {}\n'.format(seq1_id))
		f.write('{}\n'.format(align1))
		f.write('> {}\n'.format(seq2_id))
		f.write('{}\n'.format(align2))
	print('Alignments written out to {}'.format(out))

