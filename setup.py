import setuptools
import re

with open("README.md", "r") as fh:
    long_description = fh.read()

"""
name
----------------------------------
發布套件名稱，可使用字母、數字、底線和分隔線，不能與pypi.org任何套件重複
建議使用包含自己使用者名稱

version
----------------------------------
依照 PEP-440 規範可使用 X.YaM.devN.postO
a = alpha release
b = beta release
rc = release candidate
post = post-release
dev = developmental release

classifiers
----------------------------------
根據此 https://pypi.org/classifiers/ 建議進行分類此套件包
"""

metadata = {}
with open("hello_pkg/__init__.py") as fp:
    exec(fp.read(), metadata)

setuptools.setup(
    version=metadata['__version__'],
    author=metadata['__author__'],
    author_email=metadata['__email__'],
    license=metadata['__license__'],
    packages=setuptools.find_packages(),
)