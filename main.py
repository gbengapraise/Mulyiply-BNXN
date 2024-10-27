def multiply_single_iteration(N, M):
    
    return N * M


def multiply_n_iterations(N, M):
   
    result = 0
    for _ in range(N):
        result += M
    return result


def main():
    N = 5
    M = 6

    single_iteration_result = multiply_single_iteration(N, M)
    print(f"Single Iteration Result: {N} * {M} = {single_iteration_result}")

    n_iterations_result = multiply_n_iterations(N, M)
    print(f"N Iterations Result: {N} * {M} = {n_iterations_result}")


if __name__ == "__main__":
    main()