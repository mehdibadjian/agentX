# setup.py
from setuptools import setup, find_packages

setup(
    name="agentx",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=0.19.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "flake8>=4.0.0",
            "black>=22.0.0",
            "isort>=5.10.0",
            "mypy>=0.950",
        ],
    },
    python_requires=">=3.8",
)