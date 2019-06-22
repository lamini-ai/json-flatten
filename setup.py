from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="json-flatten",
    description="Python functions for flattening a JSON object to a single dictionary of pairs, and unflattening that dictionary back to a JSON object",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/json-flatten",
    license="Apache License, Version 2.0",
    version=VERSION,
    py_modules=["json_flatten"],
)