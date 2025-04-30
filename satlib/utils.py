# utils.py

import torch
from torchvision import datasets, transforms

def load_mnist_subset(num_samples=600, class_labels=(0, 1), threshold=0.5):
    """
    Loads and binarizes a small MNIST subset filtered by class_labels.
    Returns: (binarized_images, labels)
    """
    transform = transforms.Compose([transforms.ToTensor()])
    mnist = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    subset = torch.utils.data.Subset(mnist, list(range(num_samples)))

    binarized_images = []
    labels = []

    for image, label in subset:
        if label not in class_labels:
            continue
        binary_image = (image.view(-1) > threshold).int()
        binarized_images.append(binary_image.tolist())
        labels.append(label)

    return binarized_images, labels

def generate_variable_map(num_pixels=784, class_labels=(0, 1)):
    """
    Creates a mapping from (pixel index, class) → SAT variable ID.
    """
    return {
        (i, digit): digit * num_pixels + i + 1
        for digit in class_labels
        for i in range(num_pixels)
    }

def parse_model_output(model, var_map):
    """
    Converts SAT model output (list of assigned literals) into a boolean weight dict.
    Only includes positive literals corresponding to valid weights.
    """
    weights = {}
    for key, var in var_map.items():
        weights[key] = (var in model)
    return weights