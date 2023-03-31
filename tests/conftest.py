import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

#https://realpython.com/pytest-python-testing/
#https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
#https://docs.python.org/3/library/unittest.html
#https://docs.pytest.org/en/stable/
#https://realpython.com/absolute-vs-relative-python-imports/
#https://www.tutorialspoint.com/pytest/pytest_conftest_py.htm
#https://www.pythonforthelab.com/blog/complete-guide-to-imports-in-python-absolute-relative-and-more/