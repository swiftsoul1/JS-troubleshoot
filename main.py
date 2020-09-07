from PIL import Image,ImageDraw

from SearchFunctions import binarySearchSub
from SortFunctions import selection_sort

def comparePixels(pix1, pix2):
    return pix1[0][0] > pix2[0][0]

def storePixels(im):
    width = int(im.size[0])
    height = int(im.size[1])

    pixel_array = []

    for i in range(width):
        for j in range(height):
            r,g,b = im.getpixel((i,j))
            pixel_array.append([(r,g,b),(i,j)])

    return pixel_array

def pixelsToImage(im, pixels):
    outimg = Image.new("RGB", im.size())
    outimg.putdata([p[0] for p in pixels])
    outimg.show()
    return outimg

def pixelsToPoints(im, pixels):
    #outimg = Image.new("RGB", size)
    for p in pixels:
        im.putpixel(p[1], p[0])
    im.show()
    #return outimg

def grayScale(im, pixels):
    draw = ImageDraw.Draw(im)
    for px in pixels:
        gray_av = int((px[0][0] + pv[0][1] + px[0][2])/3)
        draw.point(px[1], (gray_av, gray_av, gray_av))

def main():
    IMG_NAME = 'monkey'
    px = (128, 255, 255)
    #open image
    #read each pixel into memory as the image object im
    with Image.open(IMG_NAME + '.jpg') as im:
        pixels = storePixels(im)
        print("stored")

        sorted_pixels = pixels.copy()
        selection_sort(sorted_pixels)
        print("sorted")
        sorted_im = pixelsToImage(im, sorted_pixels)
        sorted_pixels.save('sorted_' + IMG_NAME + '.jpg', 'JPEG')

        while(True):
            command = input("Type a value for red threshhold or Q to quit:")
            if(command == "Q"):
                break

            threshhold = int(command)

            subi = binarySearchSub([r[0][0] for r in sorted_pixels], \
                                   0,len(sorted_pixels)-1, threshhold)

            pixelsToPoints(im, sorted_pixels[subi:])
            im.show()
        #print("Sublist of reds starts at: ", subi)

    im.save('gray_'+ IMG_NAME + '.jpg', 'JPEG')
    #im.show()


if __name__ == '__main__':
    main()