# Minimal Python Package (setup.py) Demo

Repo demonstrating how to build/host a python package in GitHub. You can clone and pull the repo both with

`pip install --upgrade git+https://github.com/ThomasLastName/slug.git`

Verify installation by running python code `from package_name import test`.

Here is some further reading:
 - How import statements work: [https://youtu.be/GxCXiSkm6no?si=BdIeM2QpuFVcnVxm](https://youtu.be/GxCXiSkm6no?si=BdIeM2QpuFVcnVxm)
 - How to put in on PyPI: [https://ewencp.org/blog/a-brief-introduction-to-packaging-python/index.html](https://ewencp.org/blog/a-brief-introduction-to-packaging-python/index.html)

# Building Your Own Package

Starting with this repo as it is (e.g., by [using it as a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)), basically just change the names of the folders and whatnot. Specifically, change the following:
1. The name of the folder `package_name`, which is the name you'll have to type during import statements (e.g., from `from package_name import test`).
2. The dependencies listed in `requirements.txt`.
3. The argument `version` in `setup.py`.
2. The argument `url` in `setup.py`.
4. The argument `author` in `setup.py`.
5. The argument `author_email ` in `setup.py`.
6. The argument `author_email ` in `setup.py`.
7. The argument `description` in `setup.py.
8. The name of the repository, itself, which is the name that you "pip install:" e.g., if you rename the repo to `my_fork`, then the repo would be installed using `pip install --upgrade git+https://github.com/ThomasLastName/my_fork.git` or, if you uploaded it to PyPI, then simply `pip install my_fork`.
