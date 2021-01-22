# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def write_csv(csvpath,list_qual_loans):
    #write the code to save list of lists to the CSV file
    # YOUR CODE HERE
    # A path is where you want to save the file
    # you read the list and write to CSV
    with open(csvpath, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(list_qual_loans)