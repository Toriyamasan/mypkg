#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Toriyamasan
# SPDX-License-Identifier: GPL-3.0-only

import rclpy
from rclpy.node import Node
from person_msgs.msg import Person
import math

class AngleConverter(Node):
    def __init__(self):
        super().__init__("listener")
        self.sub = self.create_subscription(Person, "angle", self.cb, 10)

    def cb(self, msg):
        rad = msg.age * (math.pi / 180)
        self.get_logger().info('受信: %d deg -> 変換後: %.4f rad' % (msg.age, rad))

def main():
    rclpy.init()
    node = AngleConverter()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
