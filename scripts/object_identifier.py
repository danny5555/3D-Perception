#!/usr/bin/env python

### Higher aim for project:
# To write a ROS node that reads in an image as a point cloud, filters and
# segments (using Euclidean clustering) that image into individual items

### Aims for segmentation.py file:
# 1) Write a function that will publish the point cloud data to the
# sensor_stick/point_cloud topic
#

# Import modules
from pcl_helper import *
from filtering import *
from segmentation import *
from clustering import *

# TODO: Define functions as required

# Callback function for your Point Cloud Subscriber
def pcl_callback(pcl_msg):

    # Convert ROS msg to PCL data
    pcl_data = ros_to_pcl(pcl_msg)

    # Apply all voxel_grid and pasthrough filters to data
    filtered_point_cloud = filter_point_cloud(pcl_data)

    # Extract inliers (table) and outliers (objects)
    # from point cloud using RANSAC
    table, objects =\
    segment_inliers_and_outliers_completely(filtered_point_cloud)

    # TODO: Euclidean Clustering

    cluster_cloud = extract_clusters(objects)

    # TODO: Convert PCL data to ROS messages
    ros_cloud_objects = pcl_to_ros(objects)
    ros_cloud_table = pcl_to_ros(table)
    ros_cloud_cluster = pcl_to_ros(cluster_cloud)

    # TODO: Publish ROS messages
    pcl_objects_pub.publish(ros_cloud_objects)
    pcl_table_pub.publish(ros_cloud_table)
    pcl_cluster_pub.publish(ros_cloud_cluster)


if __name__ == '__main__':

    # TODO: ROS node initialization
    rospy.init_node('clustering', anonymous=True)

    # TODO: Create Subscribers
    pcl_sub = rospy.Subscriber("sensor_stick/point_cloud", pc2.PointCloud2,\
              pcl_callback, queue_size = 1)
    # TODO: Create Publishers
    pcl_objects_pub = rospy.Publisher("/pcl_objects", PointCloud2, queue_size=1)
    pcl_table_pub = rospy.Publisher("/pcl_table", PointCloud2, queue_size=1)
    pcl_cluster_pub = rospy.Publisher("/pcl_cluster", PointCloud2, queue_size=1)

    # Initialize color_list
    get_color_list.color_list = []

    # TODO: Spin while node is not shutdown

    while not rospy.is_shutdown():
     rospy.spin()
