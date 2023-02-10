# CCRS-Python-MySQL
Reconstruction of WA's Cannabis Data
---

CCRS-Python-MySQL is a few python scripts which takes the raw [CCRS](https://lcb.wa.gov/ccrs) .zip download from a public records request and converts it from a rather dirty dataset to a somewhat usable set of csv with up to 1,000,000 lines each.

I'm using this learn python, mysql, and methods to handle 150M+ lines of raw, TSV data with challenging encoding and types. As I'm learning the code has been refactored to several times but here's my best shot so far.

## How to use

There are two scripts one which inflates the zip and removes the folder hierarchy `inflate.py` and the other standardizes the row width `columnStandardization.py`.

Both read files from one directory and then writes to a new directory without compression. The CCRS data in csv form is 23 gb at this time, so be careful with disk space.

## Known Issues with the scripts and output data

No Compression, slow, and could possibly be changed to write to compression. Data will have issues too, the size of the dataset means that I haven't been able to confirm that my column standardization method is perfect.

`InventoryAdjustment_0.csv` seems to have particular encoding issues.
