# TSP – Lin-Kernighan Optimization

## 📌 Overview
This project focuses on solving the **Traveling Salesman Problem (TSP)** using the **Lin–Kernighan (LK) heuristic**, one of the most effective local search algorithms for combinatorial optimization problems.

The implementation compares the performance of the Lin–Kernighan heuristic with a **sequential (naive) tour**, highlighting the improvement in total tour length.

---

## 🧠 Problem Description
The **Traveling Salesman Problem (TSP)** is a classical combinatorial optimization problem in Computer Science and Operations Research.

Given a set of *n* cities and the distance between each pair of cities, the goal is to find a closed tour such that:
- Each city is visited exactly once  
- The tour returns to the starting city  
- The total travel distance is minimized  

Since TSP is an **NP-hard problem**, exact algorithms become impractical for large datasets. Therefore, heuristic and approximation methods are widely used in practice.

---

## 📥 Input and Output

### Input
- Number of cities: n ≥ 2  
- Set of cities: V = {v1, v2, ..., vn}  
- Distance matrix: D = [d_ij], where d_ij is the distance between city vi and vj  

### Output
- A Hamiltonian cycle:  
  T = (v_i1, v_i2, ..., v_in, v_i1)

- Total tour cost:  
  C(T) = d(v_i1, v_i2) + d(v_i2, v_i3) + ... + d(v_in, v_i1)
  
---

## ⚙️ Methodology
- Generate random TSP instances with a fixed number of cities
- Construct an initial (sequential) tour
- Optimize the tour using the **Lin–Kernighan heuristic**
- Compare results with the baseline sequential tour
- Visualize and analyze the improvement

---

## 🧩 Lin–Kernighan Algorithm
The **Lin–Kernighan (LK)** algorithm is a local search heuristic and an extension of **2-opt** and **3-opt** methods, generalized into a **dynamic k-opt** strategy.

### Main Idea
- Start from an initial tour  
- Perform a sequence of edge exchanges  
- The number of exchanged edges (*k*) is determined dynamically  
- Only exchanges that reduce the total tour length are accepted  

### Gain Concept
For each exchange step, a gain value is computed:

`
**Gain = Σ(removed edges) − Σ(added edges)**
`


If **Gain > 0**, the exchange improves the tour. The algorithm continues extending the exchange chain until no further improvement is possible.

---

## 📊 Comparison and Results
The project provides:
- Total distance comparison between algorithms  
- Visualization of optimized and baseline tours  
- Performance analysis using charts  

Example output:

- *Comparison Algorithms Chart*
![Comparing_Algorithms](https://github.com/KANH12/TSP_LinKernighan-Optimization/blob/main/comparison_chart.png?raw=true)

---

## 📂 Project Structure

```
TSP_LinKernighan-Optimization/
                      │
                      ├── main.py
                      ├── comparing_algorithms.ipynb
                      ├── comparison_chart.png
                      │
                      ├── TSP_algorithms/
                      │      └── TSP_LK_code.py
                      │
                      ├── data/
                      │      └── TSP_LK_data.py
                      │
                      └── README.md

```

## 📌 Conclusion
This project demonstrates the effectiveness of the **Lin–Kernighan heuristic** in solving the Traveling Salesman Problem. By comparing the optimized tour with a baseline sequential tour, the results show a significant reduction in total travel distance, confirming the practical value of heuristic optimization methods for NP-hard problems.

---

## 👤 Author
- Tran Duy Thanh 
- Nguyen Dinh Quoc 
- Le Nguyen Bao Khang 
