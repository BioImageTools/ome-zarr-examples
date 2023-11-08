import zarr

# v0.4 reference:
# https://ngff.openmicroscopy.org/0.4/index.html

# v0.4 JSON Schema
# https://github.com/ome/ngff/blob/main/0.4/schemas/image.schema

image = zarr.open_group("data/image-01.zarr", "w")
image.attrs.put({})
# -> fail

image = zarr.open_group("data/valid-image-02.zarr", "w")
image.attrs.put({"version": "0.4", "multiscales": []})
labels = image.create_group("labels")
labels.attrs.put({"labels": []})
# -> fail, with no obvious error (hanging, with "loading" message)

image = zarr.open_group("data/valid-image-03.zarr", "w")
image.attrs.put(
    {
        "version": "0.4",
        "multiscales": [
            {
                "axes": [
                    {"name": "y", "type": "space", "unit": "micrometer"},
                    {"name": "x", "type": "space", "unit": "micrometer"},
                ],
                "datasets": [
                    {
                        "coordinateTransformations": [
                            {"scale": [1.0, 1.0], "type": "scale"}
                        ],
                        "path": "0",
                    },
                ],
                "version": "0.4",
            }
        ],
    }
)
labels = image.create_group("labels")
labels.attrs.put({"labels": []})
# -> fails correctly, because of missing .zarray

image = zarr.open_group("data/valid-image-04.zarr", "w")
image.attrs.put(
    {
        "version": "0.4",
        "multiscales": [
            {
                "axes": [
                    {"name": "y", "type": "space", "unit": "micrometer"},
                    {"name": "x", "type": "space", "unit": "micrometer"},
                ],
                "datasets": [
                    {
                        "coordinateTransformations": [
                            {"scale": [1.0, 1.0], "type": "scale"}
                        ],
                        "path": "0",
                    },
                ],
                "version": "0.4",
            }
        ],
    }
)
labels = image.create_group("labels")
labels.attrs.put({"labels": []})
zarr.open_array(
    "data/valid-image-04.zarr/0",
    dimension_separator="/",
    shape=(1000, 1000),
    chunks=(100, 100),
)
# succeeds