class Solution:
    """
    @param A: an array
    @return: total of reverse pairs
    """

    def reversePairs(self, A):
        # write your code here
        self.tmp = [0] * len(A)
        return self.mergesort(A, 0, len(A) - 1)

    def mergesort(self, A, l, r):
        if l >= r:
            return 0

        m = (l + r) // 2

        left_result = self.mergesort(A, l, m)
        right_result = self.mergesort(A, m + 1, r)
        result = left_result + right_result
        i, j, k = l, m + 1, l

        while (i <= m and j <= r):
            if A[i] <= A[j]:
                self.tmp[k] = A[i]
                i += 1
            else:
                self.tmp[k] = A[j]
                j += 1
                result += m + 1 - i
            k += 1

        while (i <= m):
            self.tmp[k] = A[i]
            k += 1
            i += 1
        while (j <= r):
            self.tmp[k] = A[j]
            k += 1
            j += 1

        for x in range(l, r + 1):
            A[x] = self.tmp[x]

        return result
