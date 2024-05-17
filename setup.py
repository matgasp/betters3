from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
  long_description = fh.read()

setup(
  name="betters3",
  author="matgasp",
  version='{{VERSION_PLACEHOLDER}}',
  url = "https://github.com/matgasp/betters3",
  description="A wrapper of AWS S3 (boto3) that facilitate some operations. ",
  install_requires=['boto3', 'botocore'],
  
  long_description_content_type="text/markdown",
  long_description=long_description,
  packages=find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
  ]
)