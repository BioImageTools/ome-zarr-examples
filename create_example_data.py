import zarr

# v0.4 reference:
# https://ngff.openmicroscopy.org/0.4/index.html

# v0.4 JSON Schema
# https://github.com/ome/ngff/blob/main/0.4/schemas/image.schema

# Invalid containers

# 01: just no attributes
image = zarr.open_group("data/invalid-image-01.zarr", "w")
image.attrs.put({})

image = zarr.open_group("data/valid-image-01.zarr", "w")
image.attrs.put({"version": "0.4", "multiscales": []})

image = zarr.open_group("data/valid-image-02.zarr", "w")
image.attrs.put({"version": "0.4"})
labels = image.create_group("labels")
labels.attrs.put({"labels": []})

"""
subgroup = root.create_group("my_subgroup")
subgroup.attrs.put({"key2": "value2"})

zarr.open_array(
    "my_root.zarr/my_subgroup/my_array",
    shape=(1000, 1000),
    chunks=(100, 100),
)
"""
