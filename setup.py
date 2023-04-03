from setuptools import setup

setup(
    name="hello_mdelgert",
    version="0.0.01",
    description="Example hello",
    url="https://github.com/mdelgert/PythonPackage",
    author="Matthew Elgert",
        entry_points={
        "console_scripts": [
            "demo=hello_mdelgert.demo2:main",
        ]
    }
)