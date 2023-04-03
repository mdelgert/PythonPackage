pytest
Remove-Item dist -Recurse -Force
python -m build
python -m twine upload --repository testpypi dist/* --config-file $('C:\ProgramData\pip\pip.ini')
pip uninstall example-package-mdelgert -y
pip install -i https://test.pypi.org/simple/ example-package-mdelgert