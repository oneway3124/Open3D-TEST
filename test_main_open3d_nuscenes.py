import open3d as o3d
import numpy as np


def main():
    #sample_pcd = o3d.data.PCDPointCloud()
    #pcd = o3d.io.read_point_cloud(sample_pcd.path)
    #o3d.visualization.draw([pcd])
    #sample_pcd = o3d.data.PCDPointCloud()
    pcd = o3d.io.read_point_cloud("n008-2018-08-01-15-34-25-0400__RADAR_BACK_RIGHT__1533152711219287.pcd")
    o3d.visualization.draw([pcd])

if __name__ == "__main__":
    main()
