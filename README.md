# PythonPackage

[Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

Make sure you have the latest version pip installed:
```
python -m pip install --upgrade pip
```

Make sure you have the latest version of PyPA’s [build](https://packaging.python.org/en/latest/key_projects/#build) installed:
```
python -m pip install --upgrade build
```

Now run this command from the same directory where pyproject.toml is located:
```
python -m build
```

[Create a token to upload here](https://test.pypi.org/account/register/)

Now that you are registered, you can use [twine](https://packaging.python.org/en/latest/key_projects/#twine) to upload the distribution packages.

```
python -m pip install --upgrade twine
```

To see pip.ini location example file included in solution:
```
pip config debug
```

Once installed, run Twine to upload all of the archives under dist:
```
python -m twine upload --repository testpypi dist/* --config-file $('C:\ProgramData\pip\pip.ini')
```

Package location [example-package-mdelgert](https://test.pypi.org/project/example-package-mdelgert/)

Installing your newly uploaded package:
```
pip install -i https://test.pypi.org/simple/ example-package-mdelgert
```

Test new package:
```
python
from example_package_mdelgert import example
example.add_one(2)
exit()
```

Uninstalling your newly uploaded package:
```
pip uninstall example-package-mdelgert
```

Running the unit tests:
```
pytest
```

[Notes Samples](https://github.com/topics/notes-app?l=python)

[Using the Python starter workflow](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)

https://github.com/nikhilkumarsingh/weather-reporter

