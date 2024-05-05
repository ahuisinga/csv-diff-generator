import math
import time
from pathlib import PurePath

import pandas as pd


def generateDiff(fileA_path, fileB_path, col_A, col_B, dest_dir, removeDupes):
    try:
        # file A data
        fileA_df = pd.read_csv(fileA_path)
        # file B data
        fileB_df = pd.read_csv(fileB_path)
        if col_A not in fileA_df:
            raise ValueError(f"The column '{col_A}' was not found in '{fileA_path}'")
        if col_B not in fileB_df:
            raise ValueError(f"The column '{col_B}' was not found in '{fileB_path}'")
        if removeDupes:
            fileA_df.drop_duplicates(subset=[col_A], inplace=True)
            fileB_df.drop_duplicates(subset=[col_B], inplace=True)
        # left join on the identified fields
        left_merge_df = fileA_df.merge(
            fileB_df, left_on=[col_A], right_on=[col_B], how="left", indicator="Match"
        )
        # left join on the identified fields
        right_merge_df = fileB_df.merge(
            fileA_df, left_on=[col_B], right_on=[col_A], how="left", indicator="Match"
        )
        # create a column of booleans representing a match found for left merge
        left_merge_df["Match"] = left_merge_df["Match"] == "both"
        fileA_df["Match"] = left_merge_df["Match"]
        # create a column of booleans representing a match found for left merge
        right_merge_df["Match"] = right_merge_df["Match"] == "both"
        fileB_df["Match"] = right_merge_df["Match"]

        currTime = math.floor(time.time())
        fileA_stem = fileA_path.stem
        destA_path = PurePath(str(dest_dir), f"{fileA_stem}_diff_{currTime}.csv")
        fileB_stem = fileB_path.stem
        destB_path = PurePath(str(dest_dir), f"{fileB_stem}_diff_{currTime}.csv")

        # subset of A data that did not find a match in B data
        fileADiff = fileA_df.loc[fileA_df["Match"] == False]
        fileADiff = fileADiff.drop(columns=["Match"])
        fileADiff.to_csv(destA_path, index=False)

        # subset of B data that did not find a match in A data
        fileBDiff = fileB_df.loc[fileB_df["Match"] == False]
        fileBDiff = fileBDiff.drop(columns=["Match"])
        fileBDiff.to_csv(destB_path, index=False)
        print(
            f"\nSUCCESS. Find the results in {destA_path.name} and {destB_path.name}."
        )
    except Exception as e:
        print("\nUH-OH. There was an error.")
        print(e)
