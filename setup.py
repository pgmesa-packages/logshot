
import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='logshot',  
    version='0.0.3',
    author="Pablo García Mesa",
    author_email="pgmesa.sm@gmail.com",
    description="Simplified log tool that allows an easy manageable global logger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pgmesa-packages/logshot",
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
 )