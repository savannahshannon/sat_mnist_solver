from setuptools import setup, find_packages

setup(
    name='sat_mnist_solver',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'torch',
        'torchvision',
        'python-sat'
    ],
    author='Savannah Shannon',
    license='MIT',
    description='SAT-based learning system for MNIST',
)
