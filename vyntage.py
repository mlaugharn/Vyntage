import Image, ImageChops, ImageEnhance, random, sys

def distort(image_file, glitch = False):
        if glitch:
                glitch = 1
        else:
                glitch = 0
        x = Image.open(image_file, "r")
        x.load()
        red, green, blue = x.split()
        
        green = ImageChops.offset(green,
            glitch*random.randint(0,3),
            glitch*random.randint(0,3))
        
        blue = ImageChops.offset(ImageEnhance.Contrast(blue).enhance(.4),
            glitch*random.randint(0,5),
            glitch*random.randint(0,5))
        
        Image.merge("RGB", (red, green, blue)).save("vyntage_%s" %
                                                    image_file)

if __name__ == "__main__":
        if "-g" in sys.argv[1:]:
            arglist = sys.argv[2:]
            for x in arglist:
                distort(x, True)
        else:
            for x in sys.argv[1:]:
                distort(x)
