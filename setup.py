from setuptools import setup

with open("README.md", "r") as fh:
    long_description=fh.read()

setup(
    name='subuxapp',
    version='0.0.1',
    description="Say hello",
    py_modules=["sub"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.10",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = [
        "blessings ~=1.7",
    ],
    extras_require = {
        "dev": [
            "pytest>=3.10",
        ],
    },
    url='https://github.com/python019/sub-module-pypi',
    author='Jumayev Ubaydullo',
    author_email='tommyjumayev@gmail.com'
)