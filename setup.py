from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup (
    name = "PyGameKit",
    version = '0.2',
    packages = find_packages(),
    install_requires = [
        'pygame-ce'
    ],
    description = "A PyGame wrapper for pygame-ce",
    long_description = long_description,
    long_description_content_type = "text/markdown",
)