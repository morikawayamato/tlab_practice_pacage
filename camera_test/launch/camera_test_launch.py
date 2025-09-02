from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    ld.add_action(Node(
        package = 'v4l2_camera',
        executable = 'v4l2_camera_node',
        parameters=[{
                'video_device': '/dev/video0' # 使用するカメラデバイス
                # 'image_width': 640,
                # 'image_height': 480,
                # 'frame_rate': 30.0,
            }]
    )),

    ld.add_action(Node(
        package = 'rqt_image_view',
        name ='rqt_image_view',
        executable = 'rqt_image_view',
        output = 'screen',
        # arguments=['/image'] 
    ))

    return ld