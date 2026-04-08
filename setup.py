from pathlib import Path
from setuptools import setup

BASE_DIR = Path(__file__).resolve().parent

long_description = (BASE_DIR / "README.md").read_text(encoding="utf-8")

requirements = [
    line.strip()
    for line in (BASE_DIR / "requirements.txt").read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.startswith("#")
]

setup(
    name="bres-manuscript-classifier",
    version="0.2.0",
    author="Amy Laird",
    author_email="dataweaver22@gmail.com",
    description="A multi-label classification framework for detecting structural patterns in symbolic manuscripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amy2213/bres-manuscript-classifier",
    py_modules=["classifier_multi_label", "api"],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "bres-classifier=classifier_multi_label:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Text Processing :: Linguistic",
    ],
    keywords=[
        "manuscripts",
        "symbolic-analysis",
        "archaeoastronomy",
        "calendar-classification",
        "digital-humanities",
        "pattern-detection",
    ],
)
