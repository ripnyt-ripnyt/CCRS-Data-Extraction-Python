# CCRS-Python-MySQL
Reconstruction of WA's Cannabis Data
---

This is a project which I'm using to learn python, mysql, and methods to handle 150M+ lines of raw, TSV data with challenging encoding and types.

The repo is currenly in rough shape, so here's what's going on:

Use the dataCleanup.py file to process the raw files from TSV, UTF-16-LE with many non-ASCII characters to a list of tuples for use with the most recent sql connection, 
StrainsSQLConnect.py.

Plan on adding these two files together when done debugging.
