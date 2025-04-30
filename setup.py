from setuptools import setup, find_packages

# Read the README file for the long description (optional)
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sat_mnist_solver",  # Project name
    version="1.0.0",  # Version of the package
    author="Savannah Shannon",  # Name
    author_email="savannahshannon@example.com",  # Email address
    description="A SAT solver-based approach to classifying MNIST dataset using SAT encodings",  # Short description
    long_description=long_description,  # Long description from the README
    long_description_content_type="text/markdown",  # Markdown for README
    url="https://github.com/savannahshannon/sat_mnist_solver",  # URL for the project
    packages=find_packages(),  # Automatically find the packages in the project
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",  # OS compatibility
    ],
    install_requires=[  # Dependencies for the package
        "torch>=2.0.0",
        "torchvision>=0.10.0",
        "python-sat>=1.8.0",
        "pysat>=3.0.0",
    ],
    extras_require={  # Additional dependencies for testing
        "dev": [
            "pytest>=6.0",  # Testing framework
            "unittest",  # Optional for testing
        ],
    },
    python_requires=">=3.6",  # Minimum Python version
    entry_points={  # Optional: If you want to add command-line tools
        "console_scripts": [
            "sat-mnist-solver=satlib.core:main",  # Example CLI entry point
        ],
    },
)