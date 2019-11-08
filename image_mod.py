from PIL import Image, ImageFilter, ImageEnhance
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--image",required=True, help="path to image")

parser.add_argument("-b", "--blur", help="specify if you want image to be blured",
                    action="store_true")

parser.add_argument("-r", "--rotate", help="specify if you want image to be rotated",
                    action="store_true")

parser.add_argument("-s", "--scale", help="specify if you want image to be scaled",
                    action="store_true")

parser.add_argument("-c", "--contrast", help="specify if you want to change image contrast",
                    action="store_true")

parser.add_argument("--ratio", required=True, type=float, help="specify the modify ratio")

parser.add_argument("--step", required=True, type=float, help="specify the modify step")

args = parser.parse_args()


try:
    original = Image.open(args.image)
except:
    print("Unable to load the image")
    exit()

ratio = 0
counter = 0
quantity = int(args.ratio/args.step)
for counter in range(quantity):
    ratio+=args.step
    filename = '{:.2f}'.format(ratio).replace('.', '_')
    print('[INFO] Converting image {}\\{}...'.format(counter+1, quantity))

    if args.scale:

        try:
            os.mkdir('scaled')
            print('[INFO] Creating a directory...')
        except:
            pass

        print('[INFO] Resizing...')
        image = original.resize((int(original.width*ratio), int(original.height*ratio)))
        image.save('scaled/{}.png'.format(filename))
        image.close()

    if args.blur:

        try:
            os.mkdir('blured')
            print('[INFO] Creating a directory...')
        except:
            pass

        print('[INFO] Bluring...')
        image = original.filter(ImageFilter.GaussianBlur(ratio*10))
        image.save('blured/{}.png'.format(filename))
        image.close()

    if args.rotate:

        try:
            os.mkdir('rotated')
            print('[INFO] Creating a directory...')
        except:
            pass

        print('[INFO] Rotating...')
        image = original.rotate(360*ratio)
        image.save('rotated/{}.png'.format(filename))
        image.close()

    if args.contrast:

        try:
            os.mkdir('contrast')
            print('[INFO] Creating a directory...')
        except:
            pass

        print('[INFO] Reducing contrast of the image...')
        image = ImageEnhance.Contrast(original).enhance(ratio)
        image.save('contrast/{}.png'.format(filename))

        filename = '{:.2f}'.format(ratio+1).replace('.', '_')
        print('[INFO] Increasing contrast of the image...')
        image = ImageEnhance.Contrast(original).enhance(ratio+1)
        image.save('contrast/{}.png'.format(filename))
        image.close()

original.close()
