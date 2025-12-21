from data.TSP_LK_data import N, cities, tour_cost
from TSP_algorithms.TSP_LK_code import full_lin_kernighan

if __name__ == "__main__":
    print(f"=== DATASET {N} CITIES ===")
    for i, (x, y) in enumerate(cities):
        print(f"City {i}: ({x:.4f}, {y:.4f})")

    # Baseline tour (sequential)
    sequential_tour = list(range(N)) + [0]
    sequential_cost = tour_cost(sequential_tour)

    # Lin–Kernighan
    lk_cost, lk_tour = full_lin_kernighan()

    print("\n=== BASELINE: SEQUENTIAL TOUR ===")
    print("Cost:", sequential_cost)
    print("Tour:", sequential_tour)

    print("\n=== LIN–KERNIGHAN RESULT ===")
    print("Cost:", lk_cost)
    print("Tour:", lk_tour)

    improvement = (sequential_cost - lk_cost) / sequential_cost * 100
    cost_savings = (sequential_cost - lk_cost)
    print(f"\nCost savings compared to sequential tour: {cost_savings:.2f}")
    print(f"Improvement over sequential tour (per percent): {improvement:.2f}%")

