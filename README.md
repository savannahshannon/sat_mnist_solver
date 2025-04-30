# SAT MNIST Solver

This project explores the use of SAT solvers for neural network training by leveraging the MNIST dataset. Specifically, we implement a SAT-based approach to solving binary classification problems (digits 0 and 1) by encoding neural network weights as SAT variables, then solving the resulting SAT problem to find an optimal solution.

Table of Contents
	•	Installation
	•	Usage
	•	Testing
	•	License
	•	Acknowledgements

Installation

To install the project dependencies, you’ll need Python 3.7+ and pip installed. Start by cloning the repository:

git clone https://github.com/savannahshannon/sat_mnist_solver.git
cd sat_mnist_solver

Then, install the required libraries using:

pip install -r requirements.txt

You will need to install the following dependencies:
	•	PyTorch: For handling MNIST data
	•	PySAT: For SAT solver functionalities

You can manually install PyTorch and PySAT with:

pip install torch torchvision
pip install python-sat

Usage

1. Load Data and Preprocess

The script uses the MNIST dataset and binarizes the pixel values (1 if the pixel is greater than 0.5, otherwise 0). This dataset is used for training the SAT solver to predict whether the given image corresponds to the digit ‘0’ or ‘1’.

from satlib.core import SATMNISTTrainer

# Initialize the trainer (for binary classification: 0 vs 1)
trainer = SATMNISTTrainer(num_samples=600, class_labels=(0, 1))

# Load data (600 samples of 0 and 1)
images, labels = trainer.load_data()

# Encode constraints for SAT solver
trainer.encode_constraints(images, labels)

2. Solve the SAT Problem

Once the data is preprocessed and constraints are encoded, you can solve the SAT problem to find the optimal neural network weights for the binary classification task.

# Solve SAT problem
model = trainer.solve()

# Print learned weights
if model is not None:
    weights = trainer.get_weight_assignments()
    print("Learned Weights:", weights)

3. Run Example Script

You can also run the example script to see the complete flow in action.

python examples/run_example.py

Example of Running the Trainer

from satlib.core import SATMNISTTrainer

# Initialize the SAT trainer
trainer = SATMNISTTrainer(num_samples=600, class_labels=(0, 1))

# Load and preprocess data
images, labels = trainer.load_data()

# Encode constraints for the SAT solver
trainer.encode_constraints(images, labels)

# Solve the SAT problem to find weights
model = trainer.solve()

# Print the learned weights
if model:
    weights = trainer.get_weight_assignments()
    print(weights)

Testing

We have included unit tests for verifying the functionality of the main components of the library.

To run the tests:

python -m unittest discover tests

Tests include:
	•	Data loading
	•	Constraint encoding
	•	Solver functionality
	•	Weight assignment retrieval

Project Structure

The project is organized as follows:

sat_mnist_solver/
├── satlib/
│   ├── __init__.py
│   ├── core.py         # Main solver logic
│   ├── utils.py        # Utility functions like data loading
├── examples/
│   └── run_example.py  # Example script demonstrating usage
├── tests/
│   └── test_core.py    # Unit tests for core functionalities
├── requirements.txt    # List of dependencies
├── README.md           # Project documentation
├── LICENSE             # Project license
├── setup.py            # Packaging and installation setup
└── .gitignore          # Git ignore file

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
	•	PySAT: A Python library used for SAT solving. (PySAT GitHub)
	•	PyTorch: A deep learning framework used for MNIST data handling.
