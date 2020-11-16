def sparsify(adj_dict):
    """The function 'sparsify' takes in an adjecency dictionary and returns the corresponding sparse matrix as a list of lists.An adjacency dictionary is a collection of key & value pairs where the keys refer to the nodes in a graph and the values are dictionaries containing the outgoing edges as keys and weight as values."""
    #This check if the input is not a dictionary and raise Assertion Error
    if not isinstance(adj_dict,dict):
        raise AssertionError
    A1 = [0,0,0,0]
    B1 = [0,0,0,0]
    C1 = [0,0,0,0]
    D1 = [0,0,0,0]
    #Checks for the elements of the input individually and inputs the desired weights in their corresponding indexes.
    for i in adj_dict:
        if i=='A':
            if not isinstance(adj_dict['A'],dict):
                raise AssertionError
            f = adj_dict['A']
            for j in f:
                if j=='A':
                    if not (isinstance(f['A'],int) and f['A']>=0):
                        raise AssertionError
                    A1[0] = f['A']
                elif j=='B':
                    if not (isinstance(f['B'],int) and f['B']>=0):
                        raise AssertionError
                    B1[0] = f['B']
                elif j=='C':
                    if not (isinstance(f['C'],int) and f['C']>=0):
                        raise AssertionError
                    C1[0] = f['C']
                elif j=='D':
                    if not (isinstance(f['D'],int) and f['D']>=0):
                        raise AssertionError
                    D1[0] = f['D']
                else:
                    raise AssertionError
        elif i=='B':
            if not isinstance(adj_dict['B'],dict):
                raise AssertionError
            g = adj_dict['B']
            for h in g:
                if h=='A':
                    if not (isinstance(g['A'],int) and g['A']>=0):
                        raise AssertionError
                    A1[1] = g['A']
                elif h=='B':
                    if not (isinstance(g['B'],int) and g['B']>=0):
                        raise AssertionError
                    B1[1] = g['B']
                elif h=='C':
                    if not (isinstance(g['C'],int) and g['C']>=0):
                        raise AssertionError
                    C1[1] = g['C']
                elif h=='D':
                    if not (isinstance(g['D'],int) and g['D']>=0):
                        raise AssertionError
                    D1[1] = g['D']
                else:
                    raise AssertionError
        elif i=='C':
            if not isinstance(adj_dict['C'],dict):
                raise AssertionError
            k = adj_dict['C']
            for l in k:
                if l=='A':
                    if not (isinstance(k['A'],int) and k['A']>=0):
                        raise AssertionError
                    A1[2] = k['A']
                elif l=='B':
                    if not (isinstance(k['B'],int) and k['B']>=0):
                        raise AssertionError
                    B1[2] = k['B']
                elif l=='C':
                    if not (isinstance(k['C'],int) and k['C']>=0):
                        raise AssertionError
                    C1[2] = k['C']
                elif l=='D':
                    if not (isinstance(k['D'],int) and k['D']>=0):
                        raise AssertionError
                    D1[2] = k['D']
                else:
                    raise AssertionError
        elif i=='D':
            if not isinstance(adj_dict['D'],dict):
                raise AssertionError
            m = adj_dict['D']
            for n in m:
                if n=='A':
                    if not (isinstance(m['A'],int) and m['A']>=0):
                        raise AssertionError
                    A1[3] = m['A']
                elif n=='B':
                    if not (isinstance(m['B'],int) and m['B']>=0):
                        raise AssertionError
                    B1[3] = m['B']
                elif n=='C':
                    if not (isinstance(m['C'],int) and m['C']>=0):
                        raise AssertionError
                    C1[3] = m['C']
                elif n=='D':
                    if not (isinstance(m['D'],int) and m['D']>=0):
                        raise AssertionError
                    D1[3] = m['D']
                else:
                    raise AssertionError
        else:
            raise AssertionError
    return [A1,B1,C1,D1] #Gives our output as list of lists.
print(sparsify({"A":{"B": 2,"D":4}, "B": {"C": 1}, "C": {"A": 3, "D": 1}, "D": {"B": 1}}))
print(sparsify({"A":{"B": 2,"D":4}, "B": {"C": 1}, "C": {"A": 3, "D": 1}, "D": {"B": 1}}))

def sparsify(adj_dict):
    """The function 'sparsify' takes in an adjecency dictionary and returns the corresponding sparse matrix as a list of lists.An adjacency dictionary is a collection of key & value pairs where the keys refer to the nodes in a graph and the values are dictionaries containing the outgoing edges as keys and weight as values."""
    #This check if the input is not a dictionary and raise Assertion Error
    if not isinstance(adj_dict,dict):
        raise AssertionError
    A1,B1,C1,D1,E1,F1,G1,H1,I1,J1,K1,L1,M1,N1,O1,P1,Q1,R1,S1,T1,U1,V1,W1,X1,Y1,Z1 = [[0 for i in range(len(adj_dict))] for i in range(26)]
    code = {'A':A1, 'B':B1, 'C':C1,'D':D1,'E':E1,'F':F1,'G':G1,'H':H1,'I':I1,'J':J1,'K':K1,'L':L1,'M':M1,'N':N1,'O':O1,'P':P1,'Q':Q1,'R':R1,'S':S1,'T':T1,'U':U1,'V':V1,'W':W1,'X':X1,'Y':Y1,'Z':Z1}
    letter = {'A':0, 'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
    '''a =  max(adj_dict)
    b = []
    for m in adj_dict.values():
        b.append(m.values())'''
    #Checks for the elements of the input individually and inputs the desired weights in their corresponding indexes.
    for i in adj_dict:
        f = adj_dict[i]
        for j in f:
            code[j][letter[j]] = f[j]
            break
        break
    for k in adj_dict:
        my_max = k
    new_list = []
    for i in range(letter[k]):
        new_list.append(code[list(letter.keys())[list(letter.values()).index(i)]])
    return new_list,b
print(sparsify({"A":{"B": 2,"D":4}, "B": {"C": 1}, "C": {"A": 3, "D": 1}, "D": {"B": 1}}))

        
    
    
