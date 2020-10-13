"""Setup file for victron package."""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION", "r") as fh:
    version = fh.read().strip()

EXTRAS = {"mqtt-client": ["paho-mqtt"]}

REQUIRES = []

setuptools.setup(
    name="victron",
    version=version,
    author="Matt Knight",
    author_email="matt@adventurousway.com",
    description="Python API for talking to a local Victron gateway",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT License",
    install_requires=REQUIRES,
    extras_require=EXTRAS,
    url="https://github.com/abstractvector/python-victron",
    packages=setuptools.find_packages(),
    keywords=["Victron", "Venus", "IoT"],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Home Automation",
        "Natural Language :: English",
    ],
    python_requires=">=3.8",
)
