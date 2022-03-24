from setuptools import setup, find_namespace_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="metaflow-sample-plugin",
    version="0.1.0",
    author="sappier",
    description="Metaflow sapmple plugin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sappier/metaflow-sample-plugin",
    install_requires=[
        "metaflow>=2.5.3",
    ],
    packages=find_namespace_packages(include=["metaflow_extensions.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Environment :: Console",
    ],
    python_requires=">=3.7",
)
