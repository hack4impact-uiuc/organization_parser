import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="organization_parser",
    version="0.0.2",
    author="GlobalGiving",
    author_email="",
    description="A python library for importing parsed organization data, into GlobalGiving.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hack4impact-uiuc/organization_parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
