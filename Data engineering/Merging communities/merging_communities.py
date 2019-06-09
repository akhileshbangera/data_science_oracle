global graph

 

def tree_traverse(s,n):

    #mark all the vertices not visited

    visited = [False]*n

    conn_ver = []

    global graph

    # Create a queue for BFS

    queue = []

    # Mark the source node as 

    # visited and enqueue it

    queue.append(s)

    visited[s] = True

    while(queue):

        # Dequeue a vertex from

        # add that vertex int the conn_ver list

        s= queue.pop(0)

        conn_ver.extend([s+1])

        

        #get the adjacent vertices of the the s

        for i in graph[s]:

            if visited[i]== False:

                queue.append(i)

                visited[i] = True

    return len(conn_ver)

 

 

def main():

    #take the input

    n,q = map(int,input().split())

    global graph

    result = []

    graph= {i: [] for i in range(0,n)}

    for i in range(q):

        strng = input()

        if strng[0] == 'Q':

            # code for traversal BSF/DFS

            x = int(strng[2])

            val = tree_traverse(x-1,n)

            result.extend([val])

        else:

            #code if strng[0] == 'M'

            u,v = int(strng[2]),int(strng[4])

            graph[v-1].extend([u-1])

            graph[u-1].extend([v-1])

    print(*result, sep= '\n')

main();