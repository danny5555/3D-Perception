import pcl
from pcl_helper import *


def extract_clusters(objects_point_cloud):

  white_cloud = XYZRGB_to_XYZ(objects_point_cloud)
  tree = white_cloud.make_kdtree()

  # Create a cluster extraction object
  ec = white_cloud.make_EuclideanClusterExtraction()
  # Set tolerances for distance threshold 
  # as well as minimum and maximum cluster size (in points)
  # NOTE: These are poor choices of clustering parameters
  # Your task is to experiment and find values that work for segmenting objects.
  ec.set_ClusterTolerance(0.07)
  ec.set_MinClusterSize(50)
  ec.set_MaxClusterSize(15000)
  # Search the k-d tree for clusters
  ec.set_SearchMethod(tree)
  # Extract indices for each of the discovered clusters
  cluster_indices = ec.Extract()

  #Assign a color corresponding to each segmented object in scene
  cluster_color = get_color_list(len(cluster_indices))

  color_cluster_point_list = []

  for j, indices in enumerate(cluster_indices):
      for i, indice in enumerate(indices):
          color_cluster_point_list.append([white_cloud[indice][0],
                                        white_cloud[indice][1],
                                        white_cloud[indice][2],
                                         rgb_to_float(cluster_color[j])])

  #Create new cloud containing all clusters, each with unique color
  cluster_cloud = pcl.PointCloud_PointXYZRGB()
  cluster_cloud.from_list(color_cluster_point_list)

  return cluster_cloud
