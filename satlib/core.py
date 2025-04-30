# core.py

import torch
from torchvision import datasets, transforms
from pysat.formula import CNF
from pysat.solvers import Solver

class SATMNISTTrainer:
    def __init__(self, class_labels=(0, 1), threshold=0.5, images=None, labels=None):
        self.class_labels = class_labels
        self.threshold = threshold
        self.num_pixels = 28 * 28
        self.var_map = self._generate_variable_map()
        self.cnf = CNF()
        self.model = None
        self.images = images
        self.labels = labels

    def _generate_variable_map(self):
        return {
            (i, digit): digit * self.num_pixels + i + 1
            for digit in self.class_labels
            for i in range(self.num_pixels)
        }

    def load_data(self, num_samples=600):
        transform = transforms.Compose([transforms.ToTensor()])
        mnist = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
        subset = torch.utils.data.Subset(mnist, list(range(num_samples)))

        binarized_images = []
        labels = []

        for image, label in subset:
            if label not in self.class_labels:
                continue
            binary_image = (image.view(-1) > self.threshold).int()
            binarized_images.append(binary_image.tolist())
            labels.append(label)

        self.images = binarized_images
        self.labels = labels

        return self.images, self.labels

    def encode_constraints(self,images,labels):
        if self.images is None or self.labels is None:
            raise ValueError("Images and labels must be loaded before encoding constraints.")

        for img, label in zip(self.images, self.labels):
            for i, pixel in enumerate(img):
                if pixel == 1:
                    var0 = self.var_map[(i, self.class_labels[0])]
                    var1 = self.var_map[(i, self.class_labels[1])]
                    if label == self.class_labels[0]:
                        self.cnf.append([var0, -var1])
                    elif label == self.class_labels[1]:
                        self.cnf.append([var1, -var0])

    def solve(self):
        with Solver(name='g3') as solver:
            solver.append_formula(self.cnf)
            print("Solving SAT problem...")

            if solver.solve():
                print("SAT solution found.")
                self.model = solver.get_model()
                return self.model
            else:
                print("No solution found.")
                return None

    def get_weight_assignments(self):
        if self.model is None:
            raise ValueError("Model has not been solved yet.")
        weights = {var: (var in self.model) for var in self.var_map.values()}
        return weights