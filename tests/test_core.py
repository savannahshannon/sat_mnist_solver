# # tests/test_core.py

# import unittest
# from satlib.core import SATMNISTTrainer
# from satlib.utils import load_mnist_subset

# class TestSATMNISTSolver(unittest.TestCase):

#     def test_load_data(self):
#         # Test if the data loading and binarization process works
#         print("🔍 Testing data loading...")
#         images, labels = load_mnist_subset(num_samples=600, class_labels=(0, 1), threshold=0.5)
        
#         self.assertEqual(len(images), 600)  # Should load exactly 600 samples
#         self.assertEqual(len(labels), 600)  # Should have 600 corresponding labels
        
#         # Ensure that the images are binarized (i.e., only 0s and 1s)
#         for image in images:
#             for pixel in image:
#                 self.assertIn(pixel, [0, 1])  # Pixels should be 0 or 1

#     def test_encode_constraints(self):
#         # Test encoding the constraints into CNF
#         print("📦 Testing SAT constraint encoding...")
#         solver = SATMNISTTrainer(num_samples=600, class_labels=(0, 1))
#         images, labels = load_mnist_subset(num_samples=600, class_labels=(0, 1), threshold=0.5)
#         solver.encode_constraints(images, labels)
        
#         # Check if constraints were added
#         self.assertGreater(len(solver.cnf.clauses), 0)  # There should be at least some constraints encoded

#     def test_solve(self):
#         # Test if SAT solver can find a solution
#         print("🧮 Testing SAT solver...")
#         solver = SATMNISTTrainer(num_samples=600, class_labels=(0, 1))
#         images, labels = load_mnist_subset(num_samples=600, class_labels=(0, 1), threshold=0.5)
#         solver.encode_constraints(images, labels)
        
#         model = solver.solve()
        
#         # The model should not be None if a solution is found
#         self.assertIsNotNone(model)

#     def test_get_weight_assignments(self):
#         # Test if the weight assignments can be retrieved correctly
#         print("📊 Testing weight assignments retrieval...")
#         solver = SATMNISTTrainer(num_samples=600, class_labels=(0, 1))
#         images, labels = load_mnist_subset(num_samples=600, class_labels=(0, 1), threshold=0.5)
#         solver.encode_constraints(images, labels)
#         solver.solve()
        
#         weights = solver.get_weight_assignments()
        
#         # There should be weight assignments available
#         self.assertGreater(len(weights), 0)

# if __name__ == "__main__":
#     unittest.main()

# tests/test_core.py

import unittest
from satlib.core import SATMNISTTrainer
from satlib.utils import load_mnist_subset

class TestSATMNISTTrainer(unittest.TestCase):
    def setUp(self):
        self.images, self.labels = load_mnist_subset(num_samples=100, class_labels=(0, 1))
        self.class_labels = (0, 1)
        self.trainer = SATMNISTTrainer(images=self.images, labels=self.labels, class_labels=self.class_labels)

    def test_load_data(self):
        trainer = SATMNISTTrainer(class_labels=self.class_labels)
        images, labels = trainer.load_data(num_samples=100)
        self.assertEqual(len(images), len(labels))
        self.assertTrue(all(label in self.class_labels for label in labels))
        print("test_load_data passed.")

    def test_encode_constraints(self):
        self.trainer.encode_constraints()
        self.assertTrue(len(self.trainer.cnf.clauses) > 0)
        print("📦 test_encode_constraints passed.")

    def test_solve(self):
        self.trainer.encode_constraints()
        model = self.trainer.solve()
        self.assertIsNotNone(model)
        self.assertIsInstance(model, list)
        print("test_solve passed.")

    def test_get_weight_assignments(self):
        self.trainer.encode_constraints()
        self.trainer.solve()
        weights = self.trainer.get_weight_assignments()
        self.assertIsInstance(weights, dict)
        self.assertTrue(all(isinstance(val, bool) for val in weights.values()))
        print("test_get_weight_assignments passed.")

if __name__ == "__main__":
    unittest.main()