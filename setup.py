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
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="AlarmDecoder extended",
    url="https://github.com/ajschmidt8/adext",
    author="AJ Schmidt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=["adext"],
    install_requires=[
        "alarmdecoder@https://github.com/nutechsoftware/alarmdecoder/tarball/d45be9f53884ed21a84fb848b18c17fdfcf86170#egg=alarmdecoder-1.13.9b"
    ],
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
