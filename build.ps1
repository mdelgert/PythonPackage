pytest
Remove-Item dist -Recurse -Force
python -m build
python -m twine upload --repository testpypi dist/* --config-file $('C:\ProgramData\pip\pip.ini')
