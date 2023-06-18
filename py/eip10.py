
def define_G1(): 
    m = 6 
    G = [set() for _ in range(m)]
    G[0] |= {1, 2}
    G[1] |= {0, 2, 5}
    G[2] |= {0, 1, 3, 5}
    G[3] |= {2, 5}
    # G[4] ist leer
    G[5] |= {1, 2, 3}
    return G

graph = define_G1()
print(graph)

m = len(graph)
print('Anzahl der Knoten: ', m)

k = sum(len(graph[i]) for i in range(m)) // 2
print("Anzahle der Kanten: ", k)

#test ob eine nummer in der Graph ist 
print("2 in G[2]:  ", 2 in graph[2])
print("2 in G[3]:  ", 2 in graph[3])

d = len(graph[2])
print("Grad eines Knoten: ", d)


# Graph mit kantenkosten
def define_G3():
    G = [
        {1: 2}, 
        {0: 2, 2: 5, 3: 7},
        {1: 5, 3: 6},
        {1: 7, 2: 6}
    ]
    return G

G = define_G3()
print(G)

print("2-1: ",G[2][1])
print("2-3: ",G[2][3])

