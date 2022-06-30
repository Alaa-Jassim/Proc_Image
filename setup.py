

import setuptools
from setuptools import find_packages

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "ProcImage",
    version = "0.0.1",
    author = "Alaa Jassim Mohammed",
    author_email = "alobede2001alobede@gmail.com",
    description = "Small and simple image processing library",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Alaa-Jassim/ProcImage",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.10"
)