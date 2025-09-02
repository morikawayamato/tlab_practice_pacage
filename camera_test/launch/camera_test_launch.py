from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    ld.add_action(Node(
        package = 'v4l2_camera',
        executable = 'v4l2_camera_node',
        output = 'screen'
    ))

    # ld.add_action(Node(
    #     package = 'rqt_image_view',
    #     name ='rqt_image_view',
    #     executable = 'image_view'
    # ))

    return ld