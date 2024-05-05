<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ahuisinga/csv-diff-generator">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">CSV Diff Generator</h3>

  <p align="center">
    A handly little tool to compare two csv files and generate new files that display the differences in rows between the two.
    <br />
    <a href="https://github.com/ahuisinga/csv-diff-generator"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ahuisinga/csv-diff-generator">View Demo</a>
    ·
    <a href="https://github.com/ahuisinga/csv-diff-generator/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/ahuisinga/csv-diff-generator/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

![CLI Screen Shot][cli-screenshot]
![GUI Screen Shot][gui-screenshot]

As part of my job, I often found myself needing to pull reports and compare data between different sources. I consider myself pretty decent with excel but when dealing with thousands of rows of data, it is a slow going process that often just gives up. So I wrote a little python script that takes advantage of the pandas package to do the comparison for me.

I got tired of always typing in the full path name of the csv files, so I turned the script into a small gui with the help of [Gooey](https://github.com/chriskiehl/Gooey). Then I got tired of always selecting my files one by one, so I turned my script into its own command line tool to be run from anywhere.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

-   [![Python][Python.org]][Python-url]
-   [![Pandas][Pandas.org]][Pandas-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these steps.

### Prerequisites

-   Python
    -   Follow the steps on the [official Python site](https://www.python.org/downloads) to setup python on your computer. Make sure to install a version >= 3.6.
    -   Verify python is installed.
    ```sh
    python3 --version
    ```
-   Pip
    -   With most installations of python, pip should be included. Verify pip is installed.
    ```sh
    python3 -m pip --version
    ```

### Installation

1. Clone the repo
    ```sh
    git clone https://github.com/ahuisinga/csv-diff-generator.git
    ```
2. Navigate to the repo

    ```sh
    cd csv-diff-generator
    ```

3. Install the commands
    ```sh
    pip install .
    ```
4. You should now be able to use the diff-csv and diff-csv-gui commands on your local computer. To see where they were installed run:
    ```sh
    which diff-csv
    ```
    ```sh
    which diff-csv-gui
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

There are two ways to use the CSV Diff Generator, as a true CLI and as a GUI. Both options will compare the csv input files and produce 2 output files. The output file names will be the same as in the input file names with '\_diff_someuniqueid.csv' appended. In this file will be all the rows that appeared in the original file that were not present in the compared file. You specify the column to use as the unique identifier of a row for each file.

For example, say we have the following files:

FileA.csv
| ID | Name |
|-----|--------|
| 123 | test 1 |
| 456 | test 2 |
| 789 | test 3 |
| 012 | test 4 |
| 345 | test 5 |
| 678 | test 6 |

FileB.csv
| ID | Name |
|-----|--------|
| 123 | test 1 |
| 789 | test 3 |
| 012 | test 4 |
| 678 | test 6 |
| 999 | test 7 |

And we run the following

```sh
diff-csv FileA.csv ID FileB.csv ID
```

We would generate the following output files.

FileA_diff_0023495.csv
| ID | Name |
|-----|--------|
| 456 | test 2 |
| 345 | test 5 |

FileB_diff_0023495.csv
| ID | Name |
|-----|--------|
| 999 | test 7 |

The rows with IDs '456' and '345' do not appear in FileB, so they appear in FileA's diff. The row with ID '999' does not appear in FileA, so it appears in FileB's diff. All other rows appear in both files and therefore are left out of both output files.

To use the diff generator fully from the command line, use the `diff-csv` command and provide the appropriate arguments. To see a full list of arguments and their descriptions, use the _-h_ when running the command.

To use the diff generator in gui form, use the `diff-csv-gui` command, without any command line arguments. This will open a simple interface that allows you to pick your files to compare from a finder window. It has all the same inputs as the _diff-csv_ command, plus an additional choice to select the output destination argument.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

-   [ ] Select mulitple columns as the row identifiers
-   [ ] Make the output destination argument optional in the gui
-   [ ] Package the gui as an executeable

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Anna Huisinga

Project Link: [https://github.com/ahuisinga/csv-diff-generator](https://github.com/ahuisinga/csv-diff-generator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

-   Shoutout to the creator of this [article](https://betterprogramming.pub/build-your-python-script-into-a-command-line-tool-f0817e7cebda) that I found on how to turn my python scripts into command line tools
-   [https://github.com/chriskiehl/Gooey](https://github.com/chriskiehl/Gooey) - great tool for creating simple guis for python scripts
-   [https://github.com/othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template) is what this README is based on

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/ahuisinga/csv-diff-generator.svg?style=for-the-badge
[contributors-url]: https://github.com/ahuisinga/csv-diff-generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ahuisinga/csv-diff-generator.svg?style=for-the-badge
[forks-url]: https://github.com/ahuisinga/csv-diff-generator/network/members
[stars-shield]: https://img.shields.io/github/stars/ahuisinga/csv-diff-generator.svg?style=for-the-badge
[stars-url]: https://github.com/ahuisinga/csv-diff-generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/ahuisinga/csv-diff-generator.svg?style=for-the-badge
[issues-url]: https://github.com/ahuisinga/csv-diff-generator/issues
[license-shield]: https://img.shields.io/github/license/ahuisinga/csv-diff-generator.svg?style=for-the-badge
[license-url]: https://github.com/ahuisinga/csv-diff-generator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/annahuisinga
[cli-screenshot]: images/csv-diff-help-screenshot.png
[gui-screenshot]: images/csv-diff-gui-screenshot.png
[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org
[Pandas.org]: https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/docs/index.html
