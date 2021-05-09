# resizeall

> Resize all images in a directory.

## Motivation

I created this custom script as an alternative to ImageMagick's `convert`. You may find that ImageMagick suits your needs and is simpler to use.

## Installation

1. Clone this repo.
2. Run `chmod u+x resizeall.py`.
3. Create a soft link to the script using `sudo ln -s /path/to/resizeall.py /usr/local/bin/resizeall`.

## Usage and Syntax

Run `resizeall -h` to view this help menu:

```
usage: resizeall.py [-h] [--width [WIDTH]] [--source [SOURCE]]
                    [--output [OUTPUT]] [--tail TAIL]

Resizes all images in a directory, preserving their aspect ratio.

optional arguments:
  -h, --help         show this help message and exit
  --width [WIDTH]    The target width of the resized images.
  --source [SOURCE]  The source directory containing images to be processed.
                     If omitted, defaults to the directory from which the
                     script was invoked.
  --output [OUTPUT]  The output directory for the resized images.
  --tail TAIL        A string to append to all resized images, after the
                     original name but before the file extension (e.g.,
                     "-thumbnail"). By default, this will be w, where w is
                     whatever width you specified.
```

Example usage:

```bash
resizeall --source /path/to/images --width 32
```

This will resize all images in `/path/to/images` to `32px` width, preserving their aspect ratio. The images will be saved to the same directory as the source (unless you specify an explicit output directory).

> **Note**: Files that don't end in a valid image extension will not be processed.

> **Note**: Files that end in the specified tail will not be processed. This is to prevent re-processing any thumbnails you create (if this weren't prevented, you'd create thumbnails for your thumbnails).
