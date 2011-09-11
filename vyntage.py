import Image, ImageChops, ImageEnhance, random, sys

def distort(image_file):
        try:
                x = Image.open(image_file)
                x.load()
                red, green, blue = x.split()
                green = ImageChops.offset(green, random.randint(0,3),
                    random.randint(0,3))
                blue = ImageChops.offset(ImageEnhance.Contrast(blue).enhance(.4),
                    random.randint(0,5),
                    random.randint(0,5))
                Image.merge("RGB", (red, green, blue)).save("vyntage_%s.jpg" %
                                                            image_file)
        except IOError:
                print "Incompatible file type"
        

if __name__ == "__main__":
        for x in sys.argv[1:]:
                distort(x)
