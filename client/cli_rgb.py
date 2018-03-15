import cli_utils as utils

def get_rgb(client):

    res = client.request('vget /camera/0/lit png')

    if res is None:
        return None

    img = utils.read_png(res)
    print 'Read RGB image with shape ' + str(img.shape)
    return img
