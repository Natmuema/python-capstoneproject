def solution(A, K):
    N = len(A)

    # Handle edge cases
    if N == 0 or K == 0:
        return A

    # Optimize K
    K = K % N

    # Rotate the array
    return A[-K:] + A[:-K]


# Example usage
print(solution([3, 8, 9, 7, 6], 3))  # Should print [9, 7, 6, 3, 8]
print(solution([0, 0, 0], 1))  # Should print [0, 0, 0]
print(solution([1, 2, 3, 4], 4))  # Should print [1, 2, 3, 4]
print(solution([1, 2, 3, 4], 2))  # Should print [3, 4, 1, 2]

