# Python code to for n Queen placement
class GfG:
    def __init__(self):
        self.MAX = 10
        self.arr = [0] * self.MAX
        self.no = 0

    def breakLine(self):
        print("\n------------------------------------------------")

    def canPlace(self, k, i):

        # Helper Function to check
        # if queen can be placed
        for j in range(1, k):
            if (self.arr[j] == i or
                    (abs(self.arr[j] - i) == abs(j - k))):
                return False
        return True

    def display(self, n):

        # Function to display placed queen
        self.breakLine()
        self.no += 1
        print("Arrangement No.", self.no, end = " ")
        self.breakLine()

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if self.arr[i] != j:
                    print("\t_", end = " ")
                else:
                    print("\tQ", end = " ")
            print()

        self.breakLine()

    def nQueens(self, k, n):

        # Function to check queens placement
        for i in range(1, n + 1):
            if self.canPlace(k, i):
                self.arr[k] = i
                if k == n:
                    self.display(n)
                else:
                    self.nQueens(k + 1, n)

                # Driver Code
if __name__ == '__main__':
    n = 8
    obj = GfG()
    obj.nQueens(1, n)

    # This code is contributed by vibhu4agarwal