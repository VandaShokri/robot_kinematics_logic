import rclpy
import math
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray 

class KinematicsNode(Node):
    def __init__(self):
        super().__init__('kinematics_node')
        # Structure: Set up the communication channel
        self.publisher_ = self.create_publisher(Float64MultiArray, 'joint_angles', 10)
        
        # Structure: Set up the timer (1.0 = runs once per second)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Kinematics Node is live. Publishing dynamic placeholders.')

    def timer_callback(self):
        msg = Float64MultiArray()
        
        # --- DYNAMIC DUMMY LOGIC ---
        # Get current time to create a moving value (proves node is active)
        time_sec = self.get_clock().now().to_msg().sec
        dynamic_value = math.sin(float(time_sec)) 
        
        # Replace these with 0.0, 0.0, 0.0 if you want a flat line
        msg.data = [dynamic_value, dynamic_value, dynamic_value] 
        
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = KinematicsNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()