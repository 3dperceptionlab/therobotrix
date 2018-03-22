import numpy as np
from plyfile import (PlyData, PlyElement, make2d, PlyParseError, PlyProperty)

def camera_depth_to_plane_depth(depth, f):

    h_ = depth.shape[0]
    w_ = depth.shape[1]

    i_c_ = np.float(h_) / 2 - 1
    j_c_ = np.float(w_) / 2 - 1

    cols_, rows_ = np.meshgrid(np.linspace(0, w_ - 1, num = w_), np.linspace(0, h_ - 1, num = h_))
    dist_from_center_ = ((rows_ - i_c_)**2 + (cols_ - j_c_)**2)**(0.5)
    plane_depth_ = depth / ((1 + dist_from_center_ / f)**2)**(0.5)

    return plane_depth_

def rgbd_to_rgb_cloud(depth, color, cx, cy, fx, fy):

    points_ = []
    colors_ = []

    for i in range(0, depth.shape[1]-1):
        for j in range(0, depth.shape[0]-1):

            z_ = depth[j][i] / 1000.0
            x_ = (i - cx) * (z_ / fx)
            y_ = (j - cy) * (z_ / fy)
            
            r_ = color[j][i][0]
            g_ = color[j][i][1]
            b_ = color[j][i][2]

            points_.append([x_, y_, z_])
            colors_.append([r_, g_, b_])

    return np.array(points_), np.array(colors_)

def save_ply_cloud(points, colors, filename):

    vertex = np.zeros(points.shape[0], dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4'), ('red', 'u1'), ('green', 'u1'), ('blue', 'u1')])

    for i in range(points.shape[0]):
        vertex[i] = (points[i][0], points[i][1], points[i][2], colors[i][0], colors[i][1], colors[i][2])
        
    ply_out = PlyData([PlyElement.describe(vertex, 'vertex', comments=['vertices'])])
    ply_out.write(filename)

def generate_cloud(depth, color, camera, outFilename):
    plane_depth_ = camera_depth_to_plane_depth(depth, camera.fx)
    points_, colors_ = rgbd_to_rgb_cloud(plane_depth_, color, camera.cx, camera.cy, camera.fx, camera.fy)
    save_ply_cloud(points_, colors_, outFilename)
