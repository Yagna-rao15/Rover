#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraSubscriber(Node):
    def __init__(self):
        super().__init__('camera_subscriber')
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.bridge = CvBridge()

    def listener_callback(self, msg):
        self.get_logger().info('Receiving image frame')
        try:
            # Convert ROS Image message to OpenCV image
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

            # Display image
            cv2.imshow("Camera Image", cv_image)
            cv2.waitKey(1)

        except Exception as e:
            self.get_logger().error(f"Error converting image: {e}")

def main(args=None):
    rclpy.init(args=args)
    camera_subscriber = CameraSubscriber()
    rclpy.spin(camera_subscriber)
    camera_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

