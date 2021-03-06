"""Setuptools packaging script"""
from setuptools import setup


__version__ = '0.0.9'


setup(
    name="testforeman",
    version=__version__,
    description="Orchestrate parallel test runs",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    keywords="test",
    author="Yan Kevych",
    license="BSD 2-clause",
    packages=["testforeman"],
    python_requires=">=3.1",
    url="https://github.com/ykvch/testforeman",
    extras_require={"pytest": ["pytest"], "nose": ["nose"]},
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Testing",
    ],
    entry_points={
        "pytest11": ["foreman = testforeman.pytest_plugin"],
        "console_scripts": ["testforeman = testforeman.server:main"],
    }
)
