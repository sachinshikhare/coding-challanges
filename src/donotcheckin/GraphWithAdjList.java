package donotcheckin;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

class Graph {

    static HashMap<Integer, List<Integer>> graph = new HashMap<>();

    public void addEdge(int from, int to) {
        if (graph.containsKey(from)) {
            graph.get(from).add(to);
        } else{
            List<Integer> edges = new LinkedList<>();
            edges.add(to);
            graph.put(from, edges);
        }
    }
}


public class GraphWithAdjList {

    public static void main(String[] args) {

        Graph graph = new Graph();
        graph.addEdge(0, 4);
        graph.addEdge(1, 2);
        graph.addEdge(1, 3);
        graph.addEdge(1, 4);
        graph.addEdge(2, 3);
        graph.addEdge(3, 4);

        boolean[] visible = new boolean[Graph.graph.keySet().size()];
        bfsTraverse(4);



    }

    private static void bfsTraverse(final int vertex) {



    }
}
