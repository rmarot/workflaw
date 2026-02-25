import os
from setuptools import setup

print("PoC running in", os.environ.get("GITHUB_REPOSITORY"))
setup(name="dummyext", version="0.1.0")
