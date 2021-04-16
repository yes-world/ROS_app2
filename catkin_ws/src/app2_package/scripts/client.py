#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy

from app2_package.srv import AddTwoInts

def add_two_ints_client(x, y):

    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp = add_two_ints(x, y)
        return resp.sum

    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    a = 1
    b = 1
    print("%s + %s = %s"%(a, b, add_two_ints_client(a, b)))