"""
Setup.py for adext
"""
from os import path
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="adext",
    version="0.1",
    description="AlarmDecoder extended",
    url="https://github.com/ajschmidt8/adext",
    author="AJ Schmidt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=["adext"],
    install_requires=["alarmdecoder==1.13.2"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications",
        "Topic :: Home Automation",
        "Topic :: Security",
    ],
)
