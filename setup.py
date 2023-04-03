from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="hello_mdelgert",
    version="0.0.02",
    description="Example hello",
    long_description=readme(),
    url="https://github.com/mdelgert/PythonPackage",
    author="Matthew Elgert",
        entry_points={
        "console_scripts": [
            "demo=hello_mdelgert.demo2:main",
        ]
    }
)