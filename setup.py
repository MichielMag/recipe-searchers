import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="recipe-searchers", # Replace with your own username
    version="0.0.7",
    author="Michiel K",
    author_email="michieL_m@live.nl",
    description="A webscraping package to search for recipes URL's",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MichielMag/recipe-searchers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'bs4',
        'tldextract'
    ],
    python_requires='>=3.6',
)