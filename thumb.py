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
    parser.add_argument('size', type=int, help='The target resolution of the thumbnails (e.g., 32 for 32x32).')
    parser.add_argument('--dir', help='The directory to walk. If omitted, this is assumed to be the directory from which thumb was called.')
    parser.add_argument('--recursive', help='Walks all nested subdirectories if enabled.', action='store_true')
    parser.add_argument('--tail', help='The string tail to append to all thumbnail images, before the file extension (e.g., "32x32", "-thumbnail", etc.). By default, this will be nxn, where n is whatever size you specified.')
    args = parser.parse_args()

    size = args.size
    target_dir = args.dir if args.dir else '.'
    thumbnail_tail = args.tail if args.tail else '{}x{}'.format(size, size)

    for dir_name, subdir_list, file_list in os.walk(target_dir):

        # Would be better to glob for only image formats, but that's way too much work for little to no return
        image_files = [f for f in glob.glob('{}/*.*'.format(target_dir))]

        # If the user wants to walk all nested subdirectories
        if args.recursive:
            image_files = file_list

        for file in image_files:
            name, extension = os.path.splitext(file)
            file_path = '{}{}'.format(os.path.join(dir_name, name), extension)

            # Skip files processed by the script, or else each successive iteration will
            # generate a new file for previously created thumbnails.
            if name.endswith(thumbnail_tail):
                print(Fore.YELLOW + 'Skipping existing thumbnail: ' + Style.RESET_ALL + file_path)
                continue
            
            # Don't crash if it's not a real image file (good precation in case the dir has other file formats)          
            try:
                img = Image.open(os.path.join(dir_name, file))
                img.thumbnail((size, size), Image.ANTIALIAS)

                # In case we're working with JPG
                rgb_thumbnail = img.convert('RGB')
                rgb_thumbnail.save(os.path.join(dir_name, name) + thumbnail_tail + extension)

                print(Fore.GREEN + 'Created thumbnail for: ' + Style.RESET_ALL + file_path)

            except Exception:
                print(Fore.RED + 'Unable to process: ' + Style.RESET_ALL + file_path)
                


if __name__ == "__main__":
    main()
