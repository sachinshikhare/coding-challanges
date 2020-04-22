package main.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class QueensThatCanAttackTheKing {

    public List<List<Integer>> queensAttacktheKing(int[][] queens, int[] king) {

        int xKing = king[0];
        int yKing = king[1];

        boolean[][] queenPresent = new boolean[8][8];
        for (boolean[] arr: queenPresent){
            Arrays.fill(arr, false);
        }
        for (int[] pos : queens) {
            queenPresent[pos[0]][pos[1]] = true;
        }

        List<List<Integer>> result = new ArrayList<>();

        int xIndex = xKing;
        int yIndex = yKing;

        check(queenPresent, xIndex+1, yIndex, result, true, false, false, false);
        check(queenPresent, xIndex-1, yIndex, result, false, false, true, false);

        check(queenPresent, xIndex, yIndex+1, result, false, true, false, false);
        check(queenPresent, xIndex, yIndex-1, result, false, false, false, true);

        check(queenPresent, xIndex+1, yIndex+1, result, true, true, false, false);
        check(queenPresent, xIndex-1, yIndex-1, result, false, false, true, true);

        check(queenPresent, xIndex+1, yIndex-1, result, true, false, false, true);
        check(queenPresent, xIndex-1, yIndex+1, result, false, true, true, false);

        return result;
    }

    private void check(
        final boolean[][] queenPresent,
        int xIndex,
        int yIndex,
        List<List<Integer>> result,
        final boolean incrX,
        final boolean incrY,
        final boolean decrX,
        final boolean decrY) {

        if (xIndex < 0 || xIndex > 7 || yIndex < 0 || yIndex > 7) {
            return;
        }
        if (queenPresent[xIndex][yIndex]) {
            List<Integer> temp = new ArrayList<>();
            temp.add(xIndex);
            temp.add(yIndex);
            result.add(temp);
            return;
        }
        xIndex = incrX ? xIndex + 1 : decrX ? xIndex - 1 : xIndex;
        yIndex = incrY ? yIndex + 1 : decrY ? yIndex - 1 : yIndex;

        check(queenPresent, xIndex, yIndex, result, incrX, incrY, decrX, decrY);
    }

    public static void main(String[] args) {
        int[][] queens = {
            {5,6},{7,7},{2,1},{0,7},{1,6},{5,1},{3,7},{0,3},{4,0},{1,2},{6,3},{5,0},{0,4},{2,2},{1,1},
            {6,4},{5,4},{0,0},{2,6},{4,5},{5,2},{1,4},{7,5},{2,3},{0,5},{4,2},{1,0},{2,7},{0,1},{4,6},
            {6,1},{0,6},{4,3},{1,7}
        };

        int[] king = {3,4} ;

        new QueensThatCanAttackTheKing().queensAttacktheKing(queens, king);
    }
}
