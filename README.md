# ome-zarr-examples

Collection of OME-Zarr structures, for testing different NGFF validators.

Within `data`, there exist subfolders `valid`, `invalid` and `warning` (defined based on the outcome of https://ome.github.io/ome-ngff-validator).

## Re-create the data

This requires running the `create_example_data.py` Python script, which only requires
the zarr-python library to be installed.

## Other data collections

Note that other lists of publicly available OME-Zarrs do exist:

* https://idr.github.io/ome-ngff-samples/
* https://ome.github.io/ome-ngff-tools/

This repository is meant to only contain syntethic data, only created to explore existing or future OME-Zarr validators test.

## Validators

The main existing validator is https://ome.github.io/ome-ngff-validator. A
simple way to test it is through the
[`ome-zarr-py`](https://github.com/ome/ome-zarr-py) CLI command `ome_zarr
view`:
```
ome_zarr view data/valid/01-image.zarr
```
