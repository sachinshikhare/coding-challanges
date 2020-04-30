package main.java;

public class MatrixProduct {

    static int calculate(final int[][] arr, final int row, final int col, final int maxRow, final int maxCol, int product) {

        if (col == maxCol-1 && row == maxRow-1) {
            return product * arr[row][col];
        }

        if (col != maxCol-1 && row != maxRow -1) {
            return Integer.max(
                calculate(arr, row+1, col, maxRow, maxCol, product*arr[row][col]),
                calculate(arr, row, col+1, maxRow, maxCol, product*arr[row][col])
            );
        }
        if(col != maxCol - 1) {
            return calculate(arr, row, col+1, maxRow, maxCol, product*arr[row][col]);
        } else {
            return calculate(arr, row+1, col, maxRow, maxCol, product*arr[row][col]);
        }
    }
}

class MatrixProductTester {
    public static void main(String[] args) {
        int[][] arr = {
            {1,2,3},
            {4,5,6},
            {7,8,9}
        };
        int[][] arr2 = {
            {-1,2,3},
            {4,5,-6},
            {7,8,9}
        };
        System.out.println(MatrixProduct.calculate(arr, 0, 0, 3, 3, 1));
        System.out.println(MatrixProduct.calculate(arr2, 0, 0, 3, 3, 1));
    }
}
