### This sequence tests filtering.py to ensure the functions work
from filtering import *
import pcl

##################################   Test 1   #################################
voxel_grid = pcl_to_voxel(\
'/home/danny/Documents/RoboND-Perception-Exercises/Exercise-1/tabletop.pcd')

filename = 'test.pcd'
pcl.save(voxel_grid, filename)

### To test run the following in command line:
# $ python test.py
# $ pcl_viewer test.pcd

# Window should display a point cloud of a table and objects on top, with
# the appropriate shadows from the sensor stick

##################################   Test 2   #################################
passthrough = voxel_to_passthrough(voxel_grid)

filename = 'test2.pcd'
pcl.save(passthrough, filename)

### To test run the following in command line:
# $ python test.py
# $ pcl_viewer test2.pcd

# Window should display a point cloud of a tabletop and objects only
