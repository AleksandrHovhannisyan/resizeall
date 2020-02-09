#! /usr/bin/python3
import sys
import os
import glob
import argparse
try:
    from PIL import Image
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'Pillow'])
    from PIL import Image
try:
    from colorama import Fore, Style
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'colorama'])
    from colorama import Fore, Style


def main():
    parser = argparse.ArgumentParser(description='Create thumbnails for all images in a directory.')
    parser.add_argument('s', type=int, help='The desired size of the thumbnails (e.g., 32 for 32x32).')
    parser.add_argument('--d', help='The directory to walk. If omitted, this is assumed to be the directory from which thumb was called.')
    parser.add_argument('--r', help='Walks all nested subdirectories if enabled.', action='store_true')
    parser.add_argument('--t', help='The string tail to append to all thumbnail images, before the file extension (e.g., "32x32", "-thumbnail", etc.). By default, this will be whatever dimension you specified.')
    args = parser.parse_args()

    size = args.s
    target_dir = args.d if args.d else '.'
    thumbnail_tail = args.t if args.t else '{}x{}'.format(size, size)

    for dir_name, subdir_list, file_list in os.walk(target_dir):

        # Would be better to glob for only image formats, but that's way too much work for little to no return
        image_files = [f for f in glob.glob('{}/*.*'.format(target_dir))]

        # If the user wants to walk all nested subdirectories
        if args.r:
            image_files = file_list

        for file in image_files:
            name, extension = os.path.splitext(file)

            # Skip files processed by the script, or else each successive iteration will
            # generate a new file for previously created thumbnails.
            if name.endswith(thumbnail_tail):
                continue

            # Don't crash if it's not a real image file (good precation in case the dir has other file formats)          
            try:
                img = Image.open(os.path.join(dir_name, file))
                img.thumbnail((size, size), Image.ANTIALIAS)

                # In case we're working with JPG
                rgb_thumbnail = img.convert('RGB')
                rgb_thumbnail.save(os.path.join(dir_name, name) + thumbnail_tail + extension.upper())

                print(Fore.GREEN + 'Created thumbnail for: ' + Style.RESET_ALL + '{}{}'.format(os.path.join(dir_name, name), extension))

            except Exception:
                print(Fore.RED + 'Unable to process: ' + Style.RESET_ALL + '{}{}'.format(os.path.join(dir_name, name), extension))


if __name__ == "__main__":
    main()
