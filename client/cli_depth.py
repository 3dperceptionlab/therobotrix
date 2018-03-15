import cli_utils as utils

def get_depth(client):

    res_ = client.request('vget /camera/0/depth npy')

    if res_ is None:
        return None

    depth_ = utils.read_npy(res_)
    return depth_
