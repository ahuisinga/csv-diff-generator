"""
The command-line interface for the diff
"""

import argparse
from pathlib import Path

from .generateCsvDiff import generateDiff


def main():
    # define arguments
    parser = argparse.ArgumentParser(
        prog="Spreadsheet Comparator",
        description="Compare spreadsheets and generate new files that list the row differences.",
    )
    fileAGroup = parser.add_argument_group(
        "File A Info",
    )
    fileAGroup.add_argument(
        "FileA", action="store", help="CSV file A to compare against file B."
    )
    fileAGroup.add_argument(
        "ColA",
        action="store",
        help="Unique ID column for file A. Case Sensitive.",
    )
    fileBGroup = parser.add_argument_group("File B Info")
    fileBGroup.add_argument(
        "FileB",
        action="store",
        help="CSV file B to compare against file A.",
    )
    fileBGroup.add_argument(
        "ColB",
        action="store",
        help="Unique ID column for file B. Case Sensitive.",
    )
    flagsGroup = parser.add_argument_group("Flags")
    flagsGroup.add_argument(
        "-d",
        "--Remove-Duplicates",
        action="store_true",
        dest="removeDupes",
        help="Removes duplicate rows from both files.",
    )

    args = parser.parse_args()
    fileA_path = Path(args.FileA)
    fileB_path = Path(args.FileB)
    colA = args.ColA
    colB = args.ColB
    removeDupes = args.removeDupes
    dest_dir = Path.cwd()
    # generate a csv diff
    generateDiff(fileA_path, fileB_path, colA, colB, dest_dir, removeDupes)


if __name__ == "__main__":
    main()
