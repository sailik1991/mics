from pulp import *

# https://goo.gl/TzaJNN
L = 0.99 #Lower Bound
U = 0 # Problem specific definition, Upper Bound
MAX_COLORS = 31
'''
Input File:
No. of nodes (c)
|               |
|   adj matrix  |
|               |
Eg.
3
1 0 1
0 1 1
1 1 1
'''

def solve(filename, c):
    '''
    TODO: Use normal solver while moving from max value towards lesser value for colors. 
    When infeasible, switch to Gurobi/GLPK.
    '''
    C = [i for i in range(c)]
    f = open(filename,'r')
    n = int(f.readline())
    N = [i for i in range(n)]
    K = [2**i for i in range(n)]
    U = sum(K) + 1
    print(K)
    print(U)
    #exit(0)
    problem = LpProblem("IdentifyingCodes", LpMinimize)
    Q = []
    for i in N:
        for j in C:
            Q.append('_{}_{}'.format(i,j))
    q = LpVariable.dict("q_%s", Q, 0, 1, LpInteger)
    #print(q)
    #exit(0)

    # each pair has a constraints
    Y = []
    for i in N:
        for j in N:
            if j < i:
                Y.append('_{}_{}'.format(i,j))
    y = LpVariable.dict("y_%s", Y, 0, 1, LpInteger)

    u = []
    for i in N:
        x = 0
        for j in range(c):
            x += q['_{}_{}'.format(i,j)]
        u.append(x)

    obj_func = sum(q[i] for i in Q)
    problem += obj_func

    for i in N:
        problem += u[i] <= 1, "Node_{}".format(i)

    for j in range(c):
        x = 0
        for i in N:
            x += q['_{}_{}'.format(i,j)]
        problem += x == 1, "Color_{}".format(j)

    # https://goo.gl/6MUaHN
    M = []
    for i in N:
        m_i = 0
        #adj_i = map(int, f.readline().split(' '))
        adj_i = [int(i.strip()) for i in f.readline().split(' ')]
        for n_j in range(len(adj_i)):
            for j in range(c):
                m_i += adj_i[n_j] * q['_{}_{}'.format(n_j,j)] * K[n_j]
        M.append(m_i)

    for i in N:
        problem += M[i] >= 1, "has_color_{}".format(i)

    for i in range(len(M)):
        for j in range(len(M)):
            if j < i:
                problem += M[i] - M[j] <= U * y['_{}_{}'.format(i,j)] - L, 'Unique_min_{}_{}'.format(i,j)
                problem += M[i] - M[j] >= L - U * (1 - y['_{}_{}'.format(i,j)]), 'Unique_max_{}_{}'.format(i,j)

    #problem.solve(pulp.GLPK_CMD());
    #problem.solve();
    problem.solve(pulp.GUROBI_CMD())
    #print("Status:", LpStatus[problem.status]);
    if LpStatus[problem.status] == 'Infeasible':
        print("----------------------------------")
        print("Status:", LpStatus[problem.status], "Not Possible With {} colors".format(c))
        print("----------------------------------")
        return 0
    elif LpStatus[problem.status] == 'Optimal':
        for v in problem.variables():
            print(v.name, "=", v.varValue)


        #Optimal cost
        print("Minimum Colors Required: {}".format(value(problem.objective)));
        print("----------------------------------")
        print("----------------------------------")   
        '''for c in problem.constraints.keys():
            print(c, " = ", problem.constraints[c])
            print("----------------------------------")
        #print(problem.constraints)'''
        exit(0)

def main(filename):
    for i in range(8, 12):
        print("Solving with {} colors..".format(i))
        print("----------------------------------")
        solve(filename, i)



if __name__ == '__main__':
    main(sys.argv[1])