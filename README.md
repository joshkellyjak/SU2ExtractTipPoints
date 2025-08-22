# ExtractTipPoints

This program extracts blade tip surface points from turbomachinery blade geometries. It takes as input MoveSurface files (generated in SU2) and the corresponding SU2 mesh file, then outputs unstructured point clouds of the blade tip surfaces. Each extracted value corresponds to an index in the original SU2 mesh.

## Features

- Reads SU2 MoveSurface files and the SU2 mesh file.
- Extracts blade tip surface points as unstructured point clouds.

## Requirements

Python 3.x

NumPy

## Installation

Clone or download this repository.

Add the bin/ folder to your PYTHONPATH in ~/.bashrc

```sh
export PYTHONPATH=$PYTHONPATH:/path/to/repo/bin  
```

## Usage

Run the program by executing ExtractTipPoints.py with a configuration file:

```sh
python ExtractTipPoints.py <config_file>
```

## Examples

The repository includes example files in the example/ folder:

## License

MIT