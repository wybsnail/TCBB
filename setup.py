from setuptools import setup, find_packages

setup(
    name="antibodyflow",
    version="1.0.0",
    description="Fixed-Backbone Antibody CDR Design via Discrete Bayesian Flow Networks",
    author="Anonymous",
    python_requires=">=3.8",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "torch>=2.0.0",
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "pandas>=1.3.0",
        "tqdm>=4.62.0",
        "biopython>=1.79",
        "pyyaml>=6.0",
        "easydict>=1.9",
        "tensorboard>=2.10.0",
        "lmdb>=1.3.0",
        "joblib>=1.1.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
)
