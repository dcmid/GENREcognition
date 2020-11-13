# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:13:57 2020

@author: dclay
"""

import pandas as pd

#read full metadata file
metadata = pd.read_csv("./fma_metadata/tracks.csv", skiprows=[0,2], low_memory=False)

# drop all tracks that are not in fma_small dataset
metadata = metadata[metadata["subset"].eq("small")]
# add name to track_id column (missing because of stupid CSV formatting)
metadata = metadata.rename(columns={"Unnamed: 0": "track_id"})
# drop all columns that don't relate to genre
# we will not have this metadata from the audio file
metadata.drop(metadata.columns.difference(["track_id","genre_top"]),1,inplace=True)
# reset indices accounting for dropped rows
metadata = metadata.reset_index(drop=True)

#write only relevant metadata to file for use in training
metadata.to_csv("fma_small_genres.csv")

metadata.head()