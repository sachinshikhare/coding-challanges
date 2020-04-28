package donotcheckin;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Optional;
import java.util.Set;

class UndirectedGraph {

    Set<Integer> vertices = new HashSet<>();
    static HashMap<Integer, List<Integer>> edges = new HashMap<>();

    public void addEdge(int v1, int v2) {
        vertices.add(v1);
        vertices.add(v2);
        if (edges.containsKey(v1)) {
            edges.get(v1).add(v2);
        } else{
            List<Integer> edges = new LinkedList<>();
            edges.add(v2);
            UndirectedGraph.edges.put(v1, edges);
        }
    }

    public boolean isCyclic() {

        boolean[] visited = new boolean[vertices.size()];
        Arrays.fill(visited, false);
        for (int vertex: edges.keySet()) {
            if (!visited[vertex]) {
                if (checkForCycle(vertex, visited, -1)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean checkForCycle(final Integer vertex, final boolean[] visited, final int parent) {

        visited[vertex] = true;
        List<Integer> adjcentNodes = Optional.ofNullable(edges.get(vertex)).orElse(Collections.emptyList());
        for (Integer adjcentNode: adjcentNodes) {
            if (!visited[adjcentNode]) {
                return checkForCycle(adjcentNode, visited, vertex);
            }
            if (adjcentNode != parent) {
                return true;
            }

        }

        return false;
    }
}


public class GraphWithAdjList {

    public static void main(String[] args) {

        UndirectedGraph undirectedGraph = new UndirectedGraph();
        undirectedGraph.addEdge(0, 4);
        undirectedGraph.addEdge(1, 2);
        undirectedGraph.addEdge(1, 3);
        undirectedGraph.addEdge(1, 4);
        undirectedGraph.addEdge(2, 3);
        undirectedGraph.addEdge(3, 4);
        System.out.println(undirectedGraph.isCyclic());
    }

}
