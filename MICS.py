from pulp import *

# https://goo.gl/TzaJNN
L = 0.99
U = 0 # Problem specific definition
'''
Input File:
No. of nodes (c)
|				|
|	adj matrix	|
|				|
Eg.
3
1 0 1
0 1 1
1 1 1
'''
def solve(filename, c):
	C = [i for i in range(c)]
	f = open(filename,'r')
	n = int(f.readline())
	N = [i for i in range(n)]
	K = [2**i for i in range(n)]
	U = sum(K) * 2

	problem = LpProblem("IdentifyingCodes", LpMinimize)
	Q = []
	for i in N:
		for j in C:
			Q.append('{}{}'.format(i,j))
	q = LpVariable.dict("q_%s", Q, 0, 1, LpInteger)

	# each pair has a constraints
	Y = []
	for i in N:
		for j in N:
			if j < i:
				Y.append('{}{}'.format(i,j))
	y = LpVariable.dict("y_%s", Y, 0, 1, LpInteger)

	u = []
	for i in N:
		x = 0
		for j in range(c):
			x += q['{}{}'.format(i,j)]
		u.append(x)

	obj_func = sum(q[i] for i in Q)
	problem += obj_func

	for i in N:
		problem += u[i] <= 1, "Node_{}".format(i)

	for j in range(c):
		x = 0
		for i in N:
			x += q['{}{}'.format(i,j)]
		problem += x == 1, "Color_{}".format(j)

	# https://goo.gl/6MUaHN
	M = []
	for i in N:
		m_i = 0
		adj_i = map(int, f.readline().split(' '))
		for n_j in range(len(adj_i)):
			for j in range(c):
				m_i += adj_i[n_j] * q['{}{}'.format(n_j,j)] * K[n_j]
		M.append(m_i)

	for i in N:
		problem += M[i] >= 1, "has_color_{}".format(i)

	for i in range(len(M)):
		for j in range(len(M)):
			if j < i:
				problem += M[i] - M[j] <= U * y['{}{}'.format(i,j)] - L, 'Unique_min_{}_{}'.format(i,j)
				problem += M[i] - M[j] >= L - U * (1 - y['{}{}'.format(i,j)]), 'Unique_max_{}_{}'.format(i,j)

	problem.solve(pulp.GLPK_CMD());
	print("Status:", LpStatus[problem.status]);
	for v in problem.variables():
		print(v.name, "=", v.varValue);

	#Optimal cost
	print(value(problem.objective));

if __name__ == '__main__':
	solve(sys.argv[1], int(sys.argv[2]))