# thumb

> Create thumbnails for all images in a directory with one simple command.

## Getting Started

1. Download `thumb.py`.

2. Run `chmod a+x thumb.py`.

3. Create a soft link to the script using `sudo ln -s path/to/downloads/webp.py /usr/bin/webp`.

## Usage and Syntax

> **Note**: You can run `thumb -h` to see a list of all available options.

This script creates thumbnails for all valid images in a directory (and potentially all nested directories, if the recursive flag is enabled). The only required argument is the size of the thumbnails.

Syntax:

```
usage: thumb [-h] [--d D] [--r] [--t T] s

Create thumbnails for all images in a directory.

positional arguments:
  s           The desired size of the thumbnails (e.g., 32 for 32x32).       

optional arguments:
  -h, --help  show this help message and exit
  --d D       The directory to walk. If omitted, this is assumed to be the   
              directory from which thumb was called.
  --r         Walks all nested subdirectories if enabled.
  --t T       The string tail to append to all thumbnail images, before the  
              file extension (e.g., "32x32", "-thumbnail", etc.). By default,
              this will be nxn, where n is whatever size you specified.
```

Example:

```bash
thumb 32 --r
```

This will create 32x32 thumbnails for all images in the directory from which the command was run. All thumbnail file names will end in '32x32' before the extension. For example, if the script processes `my-image.JPG`, the thumbnail will be saved as `my-image32x32.JPG`.

> **Note 1**: Files that don't end in a valid image extension will not be processed.

> **Note 2**: Files that end in the specified tail will not be processed. This is to prevent re-processing any thumbnails you create (if this weren't prevented, you'd create thumbnails for your thumbnails).
