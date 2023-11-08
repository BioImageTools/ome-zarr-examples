import zarr
import numpy as np

# v0.4 reference:
# https://ngff.openmicroscopy.org/0.4/index.html

# v0.4 JSON Schema
# https://github.com/ome/ngff/blob/main/0.4/schemas/image.schema

image = zarr.open_group("data/invalid/image-01.zarr", "w")
image.attrs.put({})
# -> fail

image = zarr.open_group("data/invalid/image-02.zarr", "w")
image.attrs.put({"version": "0.4", "multiscales": []})
labels = image.create_group("labels")
labels.attrs.put({"labels": []})
# -> fail, with no obvious error (hanging, with "loading" message)

image = zarr.open_group("data/invalid/image-03.zarr", "w")
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


# WARNING for dtype mismatch
image = zarr.open_group("data/warning/image-01.zarr", "w")
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
                    {
                        "coordinateTransformations": [
                            {"scale": [2.0, 2.0], "type": "scale"}
                        ],
                        "path": "1",
                    },
                ],
                "version": "0.4",
            }
        ],
    }
)
labels = image.create_group("labels")
labels.attrs.put({"labels": []})
array = zarr.open_array(
    "data/warning/image-01.zarr/0",
    dimension_separator="/",
    shape=(64, 64),
    chunks=(32, 32),
    dtype=int,
)
array = zarr.open_array(
    "data/warning/image-01.zarr/1",
    dimension_separator="/",
    shape=(32, 32),
    chunks=(32, 32),
    dtype=float,
)
# succeeds


image = zarr.open_group("data/valid/image-01.zarr", "w")
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
    "data/valid/image-01.zarr/0",
    dimension_separator="/",
    shape=(1000, 1000),
    chunks=(100, 100),
)
# succeeds

image = zarr.open_group("data/valid/image-02.zarr", "w")
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
array = zarr.open_array(
    "data/valid/image-02.zarr/0",
    dimension_separator="/",
    shape=(200, 200),
    chunks=(100, 100),
)
array[:] = np.random.uniform(0, 1000, (200, 200))
# succeeds

image = zarr.open_group("data/valid/image-03.zarr", "w")
image.attrs.put(
    {
        "version": "0.4",
        "multiscales": [
            {
                "axes": [
                    {"name": "z", "type": "space", "unit": "micrometer"},
                    {"name": "y", "type": "space", "unit": "micrometer"},
                    {"name": "x", "type": "space", "unit": "micrometer"},
                ],
                "datasets": [
                    {
                        "coordinateTransformations": [
                            {"scale": [1.0, 1.0, 1.0], "type": "scale"}
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
array = zarr.open_array(
    "data/valid/image-03.zarr/0",
    dimension_separator="/",
    shape=(2, 100, 100),
    chunks=(1, 50, 100),
)
array[:] = np.random.uniform(0, 1000, (2, 100, 100))
# succeeds


# More than one resolution level
image = zarr.open_group("data/valid/image-04.zarr", "w")
image.attrs.put(
    {
        "version": "0.4",
        "multiscales": [
            {
                "axes": [
                    {"name": "z", "type": "space", "unit": "micrometer"},
                    {"name": "y", "type": "space", "unit": "micrometer"},
                    {"name": "x", "type": "space", "unit": "micrometer"},
                ],
                "datasets": [
                    {
                        "coordinateTransformations": [
                            {"scale": [1.0, 1.0, 1.0], "type": "scale"}
                        ],
                        "path": "0",
                    },
                    {
                        "coordinateTransformations": [
                            {"scale": [1.0, 2.0, 2.0], "type": "scale"}
                        ],
                        "path": "1",
                    },
                ],
                "version": "0.4",
            }
        ],
    }
)
labels = image.create_group("labels")
labels.attrs.put({"labels": []})
array = zarr.open_array(
    "data/valid/image-04.zarr/0",
    dimension_separator="/",
    shape=(2, 64, 64),
    chunks=(1, 32, 32),
)
array = zarr.open_array(
    "data/valid/image-04.zarr/1",
    dimension_separator="/",
    shape=(2, 32, 32),
    chunks=(1, 32, 32),
)
# succeeds