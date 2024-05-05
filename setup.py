import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="spreadsheet-diff-comparator",
    version="0.0.8",
    author="Anna Huisinga",
    author_email="anna@example.com",
    description=(
        "A simple tool to compare spreadsheets and generate a file showing the rows in file A that are missing in file B."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pandas", "gooey"],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "diff-csv = generateCsvDiff.cli:main",
            "diff-csv-gui = generateCsvDiff.gui:main",
        ]
    },
)
