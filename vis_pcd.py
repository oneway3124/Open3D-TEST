
import open3d as o3d

if __name__ == "__main__":
    pcd = o3d.io.read_point_cloud('pt1txt-pcd.pcd')
    o3d.visualization.draw(pcd)