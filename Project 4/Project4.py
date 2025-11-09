import math

def count_arrangements(n, r, repetition_allowed, order_matters):
    if order_matters:
        # Permutations
        if repetition_allowed:
            result = n ** r  # P(n, r) with repetition
        else:
            result = math.perm(n, r)  # P(n, r) without repetition
    else:
        # Combinations
        if repetition_allowed:
            result = math.comb(n + r - 1, r)  # C(n + r - 1, r) with repetition
        else:
            result = math.comb(n, r)  # C(n, r) without repetition
    return result

# Example test:
n = int(input("Enter n: "))
r = int(input("Enter r: "))
repetition_allowed = input("Repetition allowed? (True/False): ").strip().lower() == "true"
order_matters = input("Order matters? (True/False): ").strip().lower() == "true"

result = count_arrangements(n, r, repetition_allowed, order_matters)
print("Result:", result)
