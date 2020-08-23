# python-package-example

## Pre-requirement
- Miniconda
- Apply for an account on [testpypi](https://test.pypi.org/account/register/).
    - You could create an API [token](https://test.pypi.org/manage/account/token/)
    - Login with 
        - account: __token__
        - password: pypi-<token>

## Description
- This is a basic structure based on PyPA documentation [^1] to deploy package.
- For more detail about setuptools could visit its latest official documentation [^2].
- The package management uses the single-sourcing that use this article [^3] method 3.

```
# install the needed package
conda install setuptools
conda install wheel

# to upload the package to pypi
conda install twine

# package your module
python setup.py sdist bdist_wheel

# upload to testpypi, you need to enter your token
twine upload --repository testpypi dist/*

# after upload
pip install --index-url https://test.pypi.org/simple/ --no-deps <Your package>

# optional: you could install this package to encrypt your password
pip install travis-encrypt
travis-encrypt --deploy gusibi python-weixin .travis.yml
```

## References
[^1] Python Packaging Authority. (n.d.). Packaging Python Projects. Retrieved August 22, 2020, from https://packaging.python.org/tutorials/packaging-projects/

[^2] Setuptools. (n.d.). Building and Distributing Packages with Setuptools. Retrieved August 22, 2020, from https://setuptools.readthedocs.io/en/latest/setuptools.html

[^3] Python Packaging Authority. (n.d.). Single-sourcing the package version. Retrieved August 23, 2020, from https://packaging.python.org/guides/single-sourcing-package-version/
