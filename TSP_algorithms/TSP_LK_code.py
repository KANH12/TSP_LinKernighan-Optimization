
from data.TSP_LK_data import N, dist_matrix, tour_cost

def full_lin_kernighan():
    def get_initial_tour():
        unvisited = list(range(1, N))
        current = 0
        tour = [0]
        while unvisited:
            next_node = min(unvisited, key=lambda x: dist_matrix[current][x])
            tour.append(next_node)
            unvisited.remove(next_node)
            current = next_node
        tour.append(0)
        return tour

    current_tour = get_initial_tour()
    best_overall_cost = tour_cost(current_tour)

    candidate_set = []
    for i in range(N):
        line = sorted(range(N), key=lambda x: dist_matrix[i][x])
        candidate_set.append(line[1:11]) 

    def get_node_after(t, tour):
        idx = tour.index(t)
        return tour[idx + 1] if idx < N else tour[1]

    def get_node_before(t, tour):
        idx = tour.index(t)
        return tour[idx - 1] if idx > 0 else tour[N-1]

    def flip_tour(tour, t3, t4, t2, t1):
        new_tour = tour[:]
        i, j = new_tour.index(t2), new_tour.index(t3)
        if i > j: i, j = j, i
        new_tour[i:j+1] = reversed(new_tour[i:j+1])
        return new_tour

    improved = True
    while improved:
        improved = False
        for t1 in range(N):
            for t2 in [get_node_before(t1, current_tour), get_node_after(t1, current_tour)]:
                x1_weight = dist_matrix[t1][t2]
                
                for t3 in candidate_set[t2]:
                    if t3 == t1 or t3 == get_node_before(t2, current_tour) or t3 == get_node_after(t2, current_tour):
                        continue
                    
                    y1_weight = dist_matrix[t2][t3]
                    gain1 = x1_weight - y1_weight
                    
                    if gain1 > 0:
                        for t4 in [get_node_before(t3, current_tour), get_node_after(t3, current_tour)]:
                            if t4 == t1 or t4 == t2: continue
                            
                            gain_final = gain1 + dist_matrix[t3][t4] - dist_matrix[t4][t1]
                            if gain_final > 0:
                                new_tour = flip_tour(current_tour, t3, t4, t2, t1)
                                new_cost = tour_cost(new_tour)
                                if new_cost < best_overall_cost:
                                    best_overall_cost = new_cost
                                    current_tour = new_tour
                                    improved = True
                                    break
                    if improved: break
                if improved: break
            if improved: break

    return best_overall_cost, current_tour
