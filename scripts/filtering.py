import pcl

# Note: pcd file should be a string
def pcl_to_voxel(pcl_data):

  # Create a voxel filter
  #cloud = pcl.load_XYZRGB(pcl_data)

  vox_grid = pcl_data.make_voxel_grid_filter()

  # Set leaf size of model
  LEAF_SIZE = 0.01
  vox_grid.set_leaf_size(LEAF_SIZE, LEAF_SIZE, LEAF_SIZE)

  # Filter out excess data points acording to leaf_size
  cloud_filtered = vox_grid.filter()

  return cloud_filtered


def select_region_containing_objects(passthrough):

  filter_axis = 'z'
  passthrough.set_filter_field_name(filter_axis)
  axis_min = 0.6
  axis_max = 1.1
  passthrough.set_filter_limits(axis_min, axis_max)

  return passthrough


def voxel_to_passthrough(vox_filtered):

  # Make passthrough filter
  passthrough = vox_filtered.make_passthrough_filter()

  # Select region containing objects
  passthrough = select_region_containing_objects(passthrough)

  # Filter out other data points not containing the objects of interest
  cloud_filtered = passthrough.filter()

  return cloud_filtered


########################### Note: not tested below ############################

# pcl_data must be in pcl data format
def filter_point_cloud(pcl_data):

  voxel_grid = pcl_to_voxel(pcl_data)

  passthrough = voxel_to_passthrough(voxel_grid)

  return passthrough


def apply_statistical_outlier_filter(cloud_filtered):
  outlier_filter = cloud_filtered.make_statistical_outlier_filter()

  # Set the number of neighboring points to analyze for any given point
  outlier_filter.set_mean_k(50)

  # Set threshold scale factor
  x = 1.0

  # Any point with a mean distance larger than (mean distance+x*std_dev)
  # will be an outlier
  outlier_filter.set_std_dev_mul_thresh(x)

  # Finally call the filter function for magic
  cloud_filtered = outlier_filter.filter()

  return cloud_filtered

