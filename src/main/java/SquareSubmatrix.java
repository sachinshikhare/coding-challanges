package main.java;

import java.util.Arrays;

/**
 * Question:​ Given a 2D array of 1s and 0s, find the largest square subarray of all 1s.
 */
public class SquareSubmatrix {

    public static int COUNTER = 0;

    public static int findSquareSubMatrix(final int[][] matrix, final int row, final int col, final int rowStart, final int colStart) {

        if (row == matrix.length || col == matrix[0].length) {
            return 0;
        }
        boolean isValid = checkNewlyAddedRowAndColumn(matrix, row, col, rowStart, colStart);
        if (isValid) {
            COUNTER++;
            return 1 + findSquareSubMatrix(matrix, row + 1, col + 1, rowStart, colStart);
        }
        return 0;
    }

    private static boolean checkNewlyAddedRowAndColumn(final int[][] matrix, final int row, final int col, final int rowStart, final int colStart) {
        if (row == rowStart) {
            return matrix[row][col] == 1;
        }
        for (int i = rowStart; i <= row; i++) {
            if (matrix[i][col] != 1) {
                return false;
            }
        }
        for (int i = colStart; i < col; i++) {
            if (matrix[row][i] != 1) {
                return false;
            }
        }
        return true;
    }

    public static int findLargestSquareSubMatrix(final int[][] matrix) {
        int maxTillNow = 0;
        int newMax = 0;
        outer:
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (maxTillNow > matrix.length - i && maxTillNow > matrix[0].length - j) {
                    break outer;
                }
                maxTillNow = Integer.max(findSquareSubMatrix(matrix, i, j, i, j), maxTillNow);
            }
        }
        return maxTillNow;
    }
}

class SquareSubmatrixTester {
    public static void main(String[] args) {
//        int[][] matrix = {
//            {1,1,1,0},
//            {1,1,1,1},
//            {1,1,0,0}
//        };
//        SquareSubmatrix.COUNTER = 0;
//        System.out.println(SquareSubmatrix.findLargestSquareSubMatrix(matrix));
//
//
        int[][] matrix2 = {
            {1,1,1,0,0,0,0,0,0,0},
            {1,1,1,1,1,1,1,0,0,0},
            {1,1,0,1,1,1,1,1,0,0},
            {1,1,0,1,1,1,1,1,0,0},
            {1,1,0,1,1,1,1,1,0,0},
            {1,1,0,1,1,1,1,0,0,0}
        };
        SquareSubmatrix.COUNTER = 0;
        System.out.println(SquareSubmatrix.findLargestSquareSubMatrix(matrix2));
        System.out.println(new OtherApproach().findLargestSquareSubMatrix(matrix2));
        System.out.println(new OtherApproach().findLargestSquareSubMatrixWithCache(matrix2));

//        int[][] matrix3 = {
//            { 0, 1, 1},
//            { 0, 1, 1}
//        };
//        SquareSubmatrix.COUNTER = 0;
//        System.out.println(SquareSubmatrix.findLargestSquareSubMatrix(matrix3));
//        int[][] matrix4 = {
//            {1,1,1,1,1,1,1,1,1,1},
//            {1,1,1,1,1,1,1,1,1,1},
//            {1,1,1,1,1,1,1,1,1,1},
//            {1,1,1,1,1,1,1,1,1,1},
//            {1,1,1,1,1,1,1,1,1,1},
//            {1,1,1,1,1,1,1,1,1,1},
//            {1,1,1,1,1,1,1,1,1,1},
//            {1,1,1,1,1,1,1,1,1,1},
//            {1,1,1,1,1,1,1,1,1,1},
//            {1,1,1,1,1,1,1,1,1,1}
//        };
//        SquareSubmatrix.COUNTER = 0;
//        System.out.println(SquareSubmatrix.findLargestSquareSubMatrix(matrix4));
//        System.out.println("COUNTER: " + SquareSubmatrix.COUNTER);
//
//
//        int[][] matrix5 = {
//            {1,1,0,0,0,0,0,0,0,0},
//            {1,1,0,0,0,0,0,0,0,0},
//            {0,0,0,0,0,0,0,0,0,0},
//            {0,0,0,0,0,0,0,0,0,0},
//            {0,0,0,0,0,0,0,0,0,0},
//            {0,0,0,0,0,0,0,0,0,0},
//            {0,0,0,0,0,0,0,0,0,0},
//            {0,0,0,0,0,0,0,0,0,0},
//            {0,0,0,0,0,0,0,0,0,0},
//            {0,0,0,0,0,0,0,0,0,1},
//        };
//        SquareSubmatrix.COUNTER = 0;
//        System.out.println(SquareSubmatrix.findLargestSquareSubMatrix(matrix5));
//        System.out.println("COUNTER: " + SquareSubmatrix.COUNTER);

    }
}

class OtherApproach {

    public static int findLargestSquareSubMatrix(final int[][] matrix) {
        int maxTillNow = 0;
        outer:
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (maxTillNow > matrix.length - i && maxTillNow > matrix[0].length - j) {
                    break outer;
                }
                maxTillNow = Integer.max(findSquareSubMatrix(matrix, i, j), maxTillNow);
            }
        }
        return maxTillNow;
    }

    private static int findSquareSubMatrix(final int[][] matrix, final int row, final int col) {

        if (row == matrix.length || col == matrix[0].length || matrix[row][col] != 1) {
            return 0;
        }
        return 1 + Integer.min(
            Integer.min(
                findSquareSubMatrix(matrix, row, col+1),
                findSquareSubMatrix(matrix, row+1, col+1)
            ),
            findSquareSubMatrix(matrix, row+1, col)
        );
    }

    public int findLargestSquareSubMatrixWithCache(final int[][] matrix) {
        int[][] cache = new int[matrix.length][matrix[0].length];
        for (int i = 0; i < cache.length; i++) {
            System.out.println("cache used");
            Arrays.fill(cache[i], 0);
        }
        int maxTillNow = 0;
        outer:
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (maxTillNow > matrix.length - i && maxTillNow > matrix[0].length - j) {
                    break outer;
                }
                maxTillNow = Integer.max(findSquareSubMatrixWithCache(matrix, i, j, cache), maxTillNow);
            }
        }
        return maxTillNow;
    }

    private int findSquareSubMatrixWithCache(final int[][] matrix, final int row, final int col, final int[][] cache) {
        if (row == matrix.length || col == matrix[0].length || matrix[row][col] != 1) {
            return 0;
        }
        if (cache[row][col] > 0) return cache[row][col];
        cache[row][col] = 1 + Integer.min(
            Integer.min(
                findSquareSubMatrix(matrix, row, col+1),
                findSquareSubMatrix(matrix, row+1, col+1)
            ),
            findSquareSubMatrix(matrix, row+1, col)
        );
        return cache[row][col];
    }
}
