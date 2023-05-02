# -*- coding: utf-8 -*-

"""Utilities for `mapp_metadata_checker`."""

import pandas as pd


def table_loader(table_path):
    """Load a table from a path.

    Parameters
    ----------
    table_path : str
        Path to the table.

    Returns
    -------
    pandas.DataFrame
        The loaded table.
    """

    return pd.read_csv(table_path, sep="\t", comment="#", dtype=str)