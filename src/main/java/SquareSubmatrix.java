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
//        System.out.println(SquareSubmatrix.findLargestSquareSubMatrix(matrix));
//
//
//        int[][] matrix2 = {
//            {1,1,1,0,0,0,0,0,0,0},
//            {1,1,1,1,1,1,1,0,0,0},
//            {1,1,0,1,1,1,1,1,0,0},
//            {1,1,0,1,1,1,1,1,0,0},
//            {1,1,0,1,1,1,1,1,0,0},
//            {1,1,0,1,1,1,1,0,0,0}
//        };
//        System.out.println(SquareSubmatrix.findLargestSquareSubMatrix(matrix2));
//        int[][] matrix3 = {
//            { 0, 1, 1},
//            { 0, 1, 1}
//        };
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
//        System.out.println(SquareSubmatrix.findLargestSquareSubMatrix(matrix4));
//        System.out.println(SquareSubmatrix.COUNTER);


        int[][] matrix5 = {
            {1,1,0,0,0,0,0,0,0,0},
            {1,1,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0,1},
        };
        System.out.println(SquareSubmatrix.findLargestSquareSubMatrix(matrix5));
        System.out.println(SquareSubmatrix.COUNTER);

    }
}
