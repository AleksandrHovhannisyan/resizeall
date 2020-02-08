import sys
import os
from PIL import Image
from colorama import Fore, Style

def main():
    
    for dir_name, subdir_list, file_list in os.walk('./posts'):

    for file in file_list:
        name, extension = os.path.splitext(file)

        # Skip files processed by the script, or else each successive iteration will
        # generate a new file for previously created -blurry versions. This assumes that
        # the user is not providing input files that already end with '-blurry'.
        # TODO: remove blurry
        if name.endswith('-placeholder') or extension == '.webp':
            continue

        img = Image.open(os.path.join(dir_name, file))

        # Hacky but effective. Basically, lose quality by reducing size and then scale
        # back up to its original dimensions.
        # TODO: Allow user to specify dimensions?
        img.thumbnail((32, 32), Image.ANTIALIAS)
        blurred = img

        # In case we're working with JPG
        rgb_img = blurred.convert('RGB')
        rgb_img.save(os.path.join(dir_name, name) + '-placeholder' + extension.upper())

        print(Fore.GREEN + 'Successfully blurred: ' + Style.RESET_ALL + '{}{}'.format(os.path.join(dir_name, name), extension))


if __name__ == "__main__":
    main()