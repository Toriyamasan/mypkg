#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Toriyamasan
# SPDX-License-Identifier: GPL-3.0-only

import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

class DegreeTalker(Node):
    def __init__(self):
        super().__init__("talker") # ノード名はtalkerのままでOK
        self.pub = self.create_publisher(Person, "angle", 10)
        self.create_timer(1.0, self.cb)
        self.deg = 0

    def cb(self):
        msg = Person()
        msg.name = "degree"
        msg.age = self.deg
        self.pub.publish(msg)
        self.get_logger().info('送信角度: %d deg' % msg.age)
        self.deg = (self.deg + 15) % 360

def main():
    rclpy.init()
    node = DegreeTalker()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
