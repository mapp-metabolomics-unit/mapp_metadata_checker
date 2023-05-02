# -*- coding: utf-8 -*-

"""Utilities for `mapp_metadata_checker`."""

import pandas as pd


def table_loader(table_path):
    """Load a table from a path. Return the table.

    Parameters
    ----------
    table_path : str
        Path to the table.

    Returns
    -------
    pandas.DataFrame
        The loaded table.
    """

    df = pd.read_csv(table_path, sep=",", comment="#", dtype=str)
    return df


def headers_reader(table_path):
    """Load a table from a path. Read and return the headers.

    Parameters
    ----------
    table_path : str
        Path to the table.

    Returns
    -------
    pandas.DataFrame
        The loaded table.
    """

    df = pd.read_csv(table_path, sep=",", comment="#", dtype=str)
    headers = df.columns.tolist()
    print(headers)
    return headers
