from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    ld.add_action(Node(
        pakage = 'v4l2_camera'
        name = 'v4l2_camera_node'
        executable = 'camera_node'
    ))

    ld.add_action(Node(
        pakage = 'rqt_image_view'
        name ='rqt_image_view'
        executable = 'image_view'
    ))

    return ld