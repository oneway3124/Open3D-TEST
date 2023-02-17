import numpy as np
import open3d as o3d

# pcd = np.genfromtxt("pt1.txt",dtype=[float,float,float,float])
#
# o3d.io.write_point_cloud("copy_of_fragment.pcd", pcd)

pcd = o3d.io.read_point_cloud("pt1.txt",format='xyz')

o3d.io.write_point_cloud("pt1txt-pcd2.pcd",pcd)