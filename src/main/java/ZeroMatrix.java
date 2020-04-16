public class ZeroMatrix {

    static void convert(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) {
            return;
        }
        boolean rowZero = false;
        boolean colZero = false;

        for (int i = 0; i < matrix.length; i++) {
            if (matrix[i][0] == 1) {
                colZero = true;
            }
        }
        for (int i = 0; i < matrix[0].length; i++) {
            if (matrix[0][i] == 1) {
                rowZero = true;
            }
        }
        for (int i = 1; i < matrix.length; i++) {
            for (int j = 1; j < matrix[0].length; j++) {
                if (matrix[i][j] == 1) {
                    matrix[i][0] = matrix[0][j] = 1;
                }
            }
        }
        for (int i = 0; i < matrix.length; i++) {
            if(matrix[i][0] == 1) {
                for (int j = 0; j < matrix[0].length; j++) {
                    matrix[i][j] = 1;
                }
            }
        }
        for (int i = 0; i < matrix[0].length; i++) {
            if(matrix[0][i] == 1) {
                for (int j = 0; j < matrix.length; j++) {
                    matrix[j][i] = 1;
                }
            }
        }
        if (rowZero) {
            for (int i = 0; i < matrix[0].length; i++) {
                matrix[0][i] = 1;
            }
        }
        if(colZero) {
            for (int i = 0; i < matrix.length; i++) {
                matrix[i][0] = 1;
            }
        }
    }
}

class ZeroMatrixTester {
    public static void main(String[] args) {
        int[][] arr = {
            { 0,1,0,0,0,0,0 },
            { 0,0,0,0,1,0,0 },
            { 0,0,0,0,0,0,0 },
            { 0,0,0,0,0,0,0 },
            { 0,0,1,0,0,0,0 },
            { 0,0,0,0,0,0,0 },
            { 0,0,0,0,0,1,0 },
            { 0,0,0,0,0,0,0 },
            { 0,0,0,0,0,0,1 },
        };
        ZeroMatrix.convert(arr);
        for (final int[] ints : arr) {
            for (int val: ints) {
                System.out.print(val + ", ");
            }
            System.out.println();
        }
    }
}
