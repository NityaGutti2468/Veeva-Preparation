# Veeva Graph Questions and Coding Practice

Polished revision sheet for graph MCQs, BFS/DFS patterns, graph coding tasks, and two extra HashMap/String parsing problems.

## Part 1: Graph MCQs With Options

### 1. Counting Graph Edges

In the given graph with nodes 0, 1, 2, 3, 4, and 5, count the total number of edges.

A. Total Edges = 6  
B. Total Edges = 7  
C. Total Edges = 8  
D. Total Edges = 9  

Answer: C  
Explanation: The edges are 2-3, 2-4, 2-0, 0-4, 0-5, 4-5, 4-1, and 5-1. Total edges = 8.

### 2. Maximum Edges In Connected Graph

In a graph with n vertices and m edges, what is the maximum number of edges that can be present in a connected simple undirected graph?

A. n  
B. n - 1  
C. n(n - 1) / 2  
D. 2 * n  

Answer: C  
Explanation: A simple undirected graph has maximum edges when it is complete. Formula = n(n - 1) / 2.

### 3. Connected Graph With No Cycles

A connected graph with no cycles is known as:

A. Complete Graph  
B. Bipartite Graph  
C. Tree  
D. Cyclic Graph  

Answer: C  
Explanation: A tree is a connected acyclic graph.

### 4. Disconnected Graph

In a disconnected graph, what can be present between two nodes from different components?

A. A unique path  
B. A cycle  
C. No connecting path  
D. Weighted edges  

Answer: C  
Explanation: In a disconnected graph, at least two nodes exist such that no path connects them.

### 5. Graph Nodes And Edges Count

In the shown graph with four red nodes and all possible connections between them, what are the total nodes and total edges?

A. Total Nodes = 3, Total Edges = 5  
B. Total Nodes = 4, Total Edges = 6  
C. Total Nodes = 4, Total Edges = 4  
D. Total Nodes = 5, Total Edges = 6  

Answer: B  
Explanation: There are 4 nodes. It is a complete graph K4, so edges = 4 * 3 / 2 = 6.

### 6. Adjacency Matrix Definition

In an adjacency matrix of an unweighted graph, what does matrix[i][j] represent?

A. The label of node i  
B. The presence or absence of an edge between nodes i and j  
C. The weight of the edge between nodes i and j  
D. The number of nodes in the graph  

Answer: B  
Explanation: For an unweighted graph, matrix[i][j] is usually 1 if edge i-j exists, otherwise 0.

### 7. Adjacency Matrix Characteristic

For an undirected graph, what is a characteristic of the adjacency matrix?

A. It is asymmetric  
B. It is a sparse matrix  
C. It is a symmetric matrix  
D. It contains only 0s  

Answer: C  
Explanation: If u is connected to v, then v is also connected to u. So matrix[u][v] = matrix[v][u].

### 8. Sparse Graph Representation

Which graph representation is more memory-efficient for sparse graphs?

A. Adjacency Matrix  
B. Adjacency List  
C. Both have the same memory efficiency  
D. Edge List  

Answer: B  
Explanation: Adjacency matrix uses O(V^2) memory. Adjacency list uses O(V + E), which is better for sparse graphs.

### 9. BFS Node Traversal Order

In Breadth-First Search (BFS), how are nodes visited in a graph?

A. In a depth-first manner  
B. In a random order  
C. In a level-by-level manner  
D. In a reverse order  

Answer: C  
Explanation: BFS visits all nodes at the current level before moving to the next level.

### 10. Connected Components Meaning

In a graph with four connected components, what does it mean?

A. There are four isolated vertices  
B. The graph is disconnected into four separate groups of vertices  
C. There are four cycles in the graph  
D. Each vertex is connected to exactly four other vertices  

Answer: B  
Explanation: A connected component is a group of vertices where every vertex is reachable from every other vertex in the same group.

### 11. Single Vertex Component

Can a single vertex be considered a connected component in a graph?

A. Yes  
B. No  
C. Only in directed graphs  
D. Only in weighted graphs  

Answer: A  
Explanation: An isolated vertex is also a connected component by itself.

## Part 2: Rearrangement Questions

### 12. Rearrange DFS Steps

Rearrange the following DFS steps:

A. Start from a source node  
B. If a node has no unvisited neighbors, backtrack to the previous node  
C. Recursively explore each unvisited neighbor  
D. Visit the current node and mark it visited using a boolean array/vector  

Answer: A, D, C, B  
Explanation: DFS starts at a source, visits and marks it, explores unvisited neighbors recursively, and backtracks when needed.

### 13. Rearrange BFS Steps

Rearrange the following BFS steps:

A. Enqueue all unvisited neighbors of the dequeued node into the queue and mark them as visited  
B. While the queue is not empty  
C. Start from a source node  
D. Enqueue the source node into a queue and mark it as visited  
E. Dequeue a node from the queue and process it  
F. Repeat until the queue is empty  

Answer: C, D, B, E, A, F  
Explanation: BFS uses a queue. It starts from a source, enqueues it, then repeatedly dequeues and visits unvisited neighbors.

## Part 3: Graph Implementation And Coding Patterns

### 14. Build Adjacency Matrix

Task: Read n nodes and m undirected edges, then print the adjacency matrix.

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int[][] adjMatrix = new int[n + 1][n + 1];

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();

            adjMatrix[u][v] = 1;
            adjMatrix[v][u] = 1;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                System.out.print(adjMatrix[i][j] + " ");
            }
            System.out.println();
        }

        sc.close();
    }
}
```

Time: O(n^2 + m)  
Space: O(n^2)

### 15. Build Adjacency List

Task: Read n nodes and m undirected edges, then print the adjacency list.

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        ArrayList<Integer>[] graph = new ArrayList[n + 1];

        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();

            graph[u].add(v);
            graph[v].add(u);
        }

        for (int i = 1; i <= n; i++) {
            for (int node : graph[i]) {
                System.out.print(node + " ");
            }
            System.out.println();
        }

        sc.close();
    }
}
```

Time: O(n + m)  
Space: O(n + m)

### 16. DFS Traversal

Task: Traverse graph using Depth-First Search.

```java
import java.util.*;

class Main {
    static void dfs(int node, boolean[] visited, List<List<Integer>> graph) {
        visited[node] = true;
        System.out.print(node + " ");

        for (int nei : graph.get(node)) {
            if (!visited[nei]) {
                dfs(nei, visited, graph);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        boolean[] visited = new boolean[n + 1];

        for (int i = 1; i <= n; i++) {
            if (!visited[i]) {
                dfs(i, visited, graph);
            }
        }

        sc.close();
    }
}
```

Time: O(n + m)  
Space: O(n + m)

### 17. BFS Traversal

Task: Traverse graph using Breadth-First Search from node 1.

```java
import java.util.*;

class Main {
    static void bfs(int start, boolean[] visited, List<List<Integer>> graph) {
        Queue<Integer> q = new LinkedList<>();

        q.add(start);
        visited[start] = true;

        while (!q.isEmpty()) {
            int node = q.poll();
            System.out.print(node + " ");

            for (int nei : graph.get(node)) {
                if (!visited[nei]) {
                    visited[nei] = true;
                    q.add(nei);
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        boolean[] visited = new boolean[n + 1];
        bfs(1, visited, graph);

        sc.close();
    }
}
```

Time: O(n + m)  
Space: O(n + m)

### 18. Check Reachability From Node 1 In Directed Graph

Task: Print all vertices reachable from node 1 in increasing order.

```java
import java.util.*;

class Main {
    static void dfs(int node, boolean[] visited, List<List<Integer>> graph) {
        visited[node] = true;

        for (int nei : graph.get(node)) {
            if (!visited[nei]) {
                dfs(nei, visited, graph);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph.get(a).add(b);
        }

        boolean[] visited = new boolean[n + 1];
        dfs(1, visited, graph);

        for (int i = 1; i <= n; i++) {
            if (visited[i]) {
                System.out.print(i + " ");
            }
        }

        sc.close();
    }
}
```

Time: O(n + m)  
Space: O(n + m)

### 19. Chef Shortest Route

Task: Find minimum number of servers in a route from node 1 to node n in an undirected unweighted graph. Return -1 if unreachable.

```java
import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        int[] dist = new int[n + 1];
        Arrays.fill(dist, -1);

        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        dist[1] = 0;

        while (!q.isEmpty()) {
            int node = q.poll();

            for (int nei : graph.get(node)) {
                if (dist[nei] == -1) {
                    dist[nei] = dist[node] + 1;
                    q.add(nei);
                }
            }
        }

        if (dist[n] == -1) {
            System.out.println(-1);
        } else {
            System.out.println(dist[n] + 1);
        }

        sc.close();
    }
}
```

Why +1? dist stores number of edges, but the question asks for number of servers including start and destination.

### 20. Minimum Distance Between Two Nodes

Task: Find minimum number of edges between nodes x and y in an undirected unweighted graph.

```java
import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        int x = sc.nextInt();
        int y = sc.nextInt();

        int[] dist = new int[n + 1];
        Arrays.fill(dist, -1);

        Queue<Integer> q = new LinkedList<>();
        q.add(x);
        dist[x] = 0;

        while (!q.isEmpty()) {
            int node = q.poll();

            for (int nei : graph.get(node)) {
                if (dist[nei] == -1) {
                    dist[nei] = dist[node] + 1;
                    q.add(nei);
                }
            }
        }

        System.out.println(dist[y]);

        sc.close();
    }
}
```

Time: O(n + m)  
Space: O(n + m)

### 21. Count Connected Components

Task: Count the number of connected components in an undirected graph.

```java
import java.util.*;

class Main {
    static void dfs(int node, boolean[] visited, List<List<Integer>> graph) {
        visited[node] = true;

        for (int nei : graph.get(node)) {
            if (!visited[nei]) {
                dfs(nei, visited, graph);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        boolean[] visited = new boolean[n + 1];
        int components = 0;

        for (int i = 1; i <= n; i++) {
            if (!visited[i]) {
                components++;
                dfs(i, visited, graph);
            }
        }

        System.out.println(components);

        sc.close();
    }
}
```

Time: O(n + m)  
Space: O(n + m)

### 22. Roads Construction In Chef's Country

Task: Find the minimum number of roads needed to connect all cities.

A. connected components  
B. connected components - 1  
C. number of nodes - 1  
D. number of edges + 1  

Answer: B  
Explanation: If there are k connected components, we need k - 1 new roads to connect all components.

Code idea: Count connected components using DFS/BFS, then print components - 1.

### 23. Galactic Network

Task: Find the number of disconnected groups in an undirected graph.

A. Number of edges  
B. Number of connected components  
C. Number of cycles  
D. Number of isolated edges  

Answer: B  
Explanation: Each disconnected group is one connected component.

Code idea: Same as connected components count using DFS/BFS.

## Part 4: Extra Coding Problems

### 24. LeetCode 3160 - Find The Number Of Distinct Colors Among The Balls

Pattern: HashMap + frequency count

We need to track:

- each ball's current color
- how many balls currently have each color
- number of distinct colors after every query

```java
import java.util.*;

class Solution {
    public int[] queryResults(int limit, int[][] queries) {
        HashMap<Integer, Integer> ballColor = new HashMap<>();
        HashMap<Integer, Integer> colorCount = new HashMap<>();

        int n = queries.length;
        int[] result = new int[n];

        for (int i = 0; i < n; i++) {
            int ball = queries[i][0];
            int newColor = queries[i][1];

            if (ballColor.containsKey(ball)) {
                int oldColor = ballColor.get(ball);

                colorCount.put(oldColor, colorCount.get(oldColor) - 1);

                if (colorCount.get(oldColor) == 0) {
                    colorCount.remove(oldColor);
                }
            }

            ballColor.put(ball, newColor);
            colorCount.put(newColor, colorCount.getOrDefault(newColor, 0) + 1);

            result[i] = colorCount.size();
        }

        return result;
    }
}
```

Logic:

```text
ballColor: ball -> current color
colorCount: color -> number of balls with that color
```

Example:

```text
queries = [[1,4],[2,5],[1,3],[3,4]]
After [1,4]: colors {4} -> 1
After [2,5]: colors {4,5} -> 2
After [1,3]: ball 1 changes from 4 to 3, colors {3,5} -> 2
After [3,4]: colors {3,5,4} -> 3
Output: [1, 2, 2, 3]
```

Time: O(n)  
Space: O(n)

### 25. Sum Numbers In Alphanumeric String

This is not sum of digits. It is the sum of full numbers inside the string.

Examples:

```text
abc123xyz -> 123
10a20b30 -> 10 + 20 + 30 = 60
00abc12ghj -> 0 + 12 = 12
5 5 5 -> 5 + 5 + 5 = 15
abcDEFghj -> 0
```

```java
class Main {
    public static void main(String[] args) {
        String s = "10a20b30";

        long sum = 0;
        long num = 0;
        boolean buildingNumber = false;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (Character.isDigit(ch)) {
                num = num * 10 + (ch - '0');
                buildingNumber = true;
            } else {
                if (buildingNumber) {
                    sum += num;
                    num = 0;
                    buildingNumber = false;
                }
            }
        }

        if (buildingNumber) {
            sum += num;
        }

        System.out.println(sum);
    }
}
```

Pattern:

```text
If digit -> build number
If non-digit -> add completed number to sum
At end -> add last number if present
```

Time: O(n)  
Space: O(1)

## Final Graph Revision Notes

- Adjacency matrix memory: O(V^2)
- Adjacency list memory: O(V + E)
- DFS uses recursion or stack
- BFS uses queue
- BFS gives shortest path in unweighted graphs
- Connected components are counted using DFS/BFS from every unvisited node
- Minimum roads to connect all components = components - 1
- Tree = connected graph with no cycles
- Tree with n nodes has n - 1 edges
- Complete graph with n nodes has n(n - 1) / 2 edges
