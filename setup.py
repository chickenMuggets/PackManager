import pathlib

import setuptools

setuptools.setup(
    name="packManager",
    version="1.0.7",
    description="A package manager for python",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://chicken-muggets.github.io/packManager/",
    author="Chicken Muggets",
    license="MIT",
    project_urls={
        "Documentation": "https://github.com/chicken-muggets/PackInst/wiki",
        "Source": "https://github.com/chicken-muggets/PackInst"
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.10,",
    packages=setuptools.find_packages(),
    include_package_data=True,
)