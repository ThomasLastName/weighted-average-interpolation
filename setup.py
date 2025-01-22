
### ~~~
## ~~~ From https://github.com/maet3608/minimal-setup-py/blob/master/setup.py
### ~~~ 

from setuptools import setup, find_packages

#
# ~~ Load the a .txt file, into a list of strings (each line is a string in the list)
def txt_to_list(filepath):
    with open(filepath, "r") as f:
        return [line.strip() for line in f]

setup(
    name = find_packages()[0], # ~~~ assumes there's only package in the directory where `setup.py` is located; otherwise, enter it manually: e.g., `name = "package_name"`
    version = "1.4.0",
    url = "https://github.com/ThomasLastName/slug",
    author = "Thomas Winckelman",
    author_email = "winckelman@tamu.edu",
    description = "Description of my package",
    packages = find_packages(),    
    install_requires = txt_to_list("requirements.txt") # ~~~ when you pip install `package_name`, pip will also install `pyreadr`
)
