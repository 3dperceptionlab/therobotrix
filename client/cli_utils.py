from PIL import Image
import png
import numpy as np

def read_8(res):
    img = np.asarray(Image.open(res))
    return img

def read_png(res):
    import StringIO
    img = Image.open(StringIO.StringIO(res))
    return np.asarray(img)

def read_npy(res):
    import StringIO
    return np.load(StringIO.StringIO(res))

def save_16bit_png(image, name, thresh_min, thresh_max):

    image[image > thresh_max] = 0.0
    image[image < thresh_min] = 0.0

    print("Depth image range is: " + str(image.min()) + ", " + str(image.max()) + " [" + str(image.ptp()) + "]")
    scaled_img = (65535*((image - image.min())/image.ptp())).astype(np.uint16)
    print("Depth image range in 16 bits: " + str(scaled_img.min()) + ", " + str(scaled_img.max()))

    with open(name, 'wb') as f:
        writer = png.Writer(width=scaled_img.shape[1], height=scaled_img.shape[0], bitdepth=16, greyscale=True)
        scaled_img_list = scaled_img.tolist()
        writer.write(f, scaled_img_list)
