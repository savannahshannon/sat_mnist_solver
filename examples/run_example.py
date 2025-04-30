# examples/run_example.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from satlib.core import SATMNISTTrainer
from satlib.utils import load_mnist_subset

def main():
    # Load MNIST data
    print("Loading MNIST subset...")
    images, labels = load_mnist_subset(num_samples=600, class_labels=(0, 1))  # Ensure images and labels are loaded
    
    # Initialize the SAT-based MNIST solver
    print("Initializing SAT-based MNIST solver...")
    solver = SATMNISTTrainer(images=images, labels=labels, class_labels=(0, 1))  # Adjusted constructor args
    
    # Encode constraints and solve
    print("Encoding constraints...")
    solver.encode_constraints(images, labels)
    print("🔑 Solving SAT problem...")
    solution = solver.solve()

    # If a solution is found, print weight assignments
    if solution:
        print("SAT solution found!")
        weights = solver.get_weight_assignments()
        print("Weight assignments:", weights)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
