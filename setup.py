import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
#this is used to publish this package on pypi

__version__ = "0.0.0"

REPO_NAME = "NLP_text_summerization"
AUTHOR_NAME = "lokesh75-kank"
SRC_REPO = "textSummerization"
AUTHOR_EMAIL = "kank.lokesh75@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

