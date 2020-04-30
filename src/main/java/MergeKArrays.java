package main.java;

import java.util.Arrays;
import java.util.PriorityQueue;

public class MergeKArrays {

    public int[] merge(int[][] matrix) {

        PriorityQueue<QueueNode> priorityQueue = new PriorityQueue<>();
        for (int i = 0; i < matrix.length; i++) {
            priorityQueue.add(new QueueNode(i, 0, matrix[i][0]));
        }

        int[] result = new int[matrix.length * matrix[0].length];
        for (int i = 0; !priorityQueue.isEmpty(); i++) {
            QueueNode queueNode = priorityQueue.poll();
            result[i] = queueNode.value;
            int newIndex = queueNode.elementIndex + 1;
            if (newIndex < matrix[queueNode.arrayIndex].length) {
                priorityQueue.add(new QueueNode(queueNode.arrayIndex, newIndex, matrix[queueNode.arrayIndex][newIndex]));
            }
        }
        return result;
    }
}

class MergeKArraysTester{
    public static void main(String[] args) {

        int[][] matrix = {
            { 7, 12, 13, 15, 18 },
            { 2, 9, 12, 14, 17 },
            { 2, 4, 7, 8, 12 },
            { 2, 3, 12, 14, 18 },
            { 2, 3, 7, 11, 19 },
            { 3, 7, 10, 12, 15 },
            { 1, 7, 8, 17, 19 },
            { 9, 14, 17, 18, 19 },
            { 2, 4, 7, 11, 13 },
            { 3, 5, 12, 14, 17 }
        };
        int[] result = new MergeKArrays().merge(matrix);
        Arrays.stream(result).forEach(System.out::println);
    }
}

class QueueNode implements Comparable{

    int arrayIndex;
    int elementIndex;
    int value;

    QueueNode(int arrayIndex, int elementIndex, int value) {
        this.arrayIndex = arrayIndex;
        this.elementIndex = elementIndex;
        this.value = value;
    }

    @Override
    public int compareTo(final Object o) {
        return this.value - ((QueueNode)o).value;
    }
}
