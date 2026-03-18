Assignment 3: Understanding Algorithm Efficiency and Scalability

This project implements and analyzes two key algorithms: Randomized and Deterministic Quicksort and a Hash Table with Chaining. The goal is to evaluate their efficiency and scalability using both theoretical concepts and empirical testing.

The Quicksort program compares randomized pivot selection with a deterministic approach (first element as pivot). The algorithms are tested on different input types, including random, sorted, reverse-sorted, and repeated-element arrays. Results show that Randomized Quicksort consistently achieves O(n log n) performance, while Deterministic Quicksort performs poorly on sorted and reverse arrays, demonstrating its O(n²) worst-case behavior.

The hash table implementation uses chaining to resolve collisions and supports insert, search, and delete operations. The results confirm that operations perform efficiently with expected complexity of O(1 + α), where α is the load factor.

How to Run

Run Quicksort: python quicksort_analysis.py

Run Hash Table: python hash_table_chaining.py
