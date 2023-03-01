import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="capsphere",
    version="0.0.1",
    author="Andy Lee",
    author_email="andy.mt.lee@gmail.com",
    description="Capsphere proprietary libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ourandy/packaging",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)