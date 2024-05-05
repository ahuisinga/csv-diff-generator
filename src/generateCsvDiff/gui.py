import argparse
from pathlib import Path

from gooey import Gooey, GooeyParser

from .generateCsvDiff import generateDiff


@Gooey(
    program_name="Spreadsheet Comparator",
    program_description="Compare spreadsheets and generate new files that list the row differences.",
)
def main():
    parser = GooeyParser()
    fileAGroup = parser.add_argument_group(
        "File A Info", gooey_options={"show_border": True}
    )
    fileAGroup.add_argument(
        "FileA", action="store", widget="FileChooser", metavar="Filename A"
    )
    fileAGroup.add_argument(
        "ColA", action="store", help="Case Sensitive", metavar="Id Column A"
    )
    fileBGroup = parser.add_argument_group(
        "File B Info", gooey_options={"show_border": True}
    )
    fileBGroup.add_argument(
        "FileB", action="store", widget="FileChooser", metavar="Filename B"
    )
    fileBGroup.add_argument(
        "ColB", action="store", help="Case Sensitive", metavar="Id Column B"
    )
    outputGroup = parser.add_argument_group(
        "Output", gooey_options={"show_border": True}
    )
    outputGroup.add_argument(
        "saveLocation",
        action="store",
        widget="DirChooser",
        type=Path,
        metavar="Output Directory",
    )
    flagsGroup = parser.add_argument_group("Flags", gooey_options={"show_border": True})
    flagsGroup.add_argument(
        "--Remove-Duplicates",
        action="store_true",
        dest="removeDupes",
        metavar="Remove Duplicates",
    )

    args = parser.parse_args()
    fileA_path = Path(args.FileA)
    fileB_path = Path(args.FileB)
    colA = args.ColA
    colB = args.ColB
    removeDupes = args.removeDupes
    dest_dir = args.saveLocation
    generateDiff(fileA_path, fileB_path, colA, colB, dest_dir, removeDupes)


if __name__ == "__main__":
    main()
