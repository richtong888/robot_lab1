#!/usr/bin/env python

from __future__ import print_function

from tutorial.srv import MulTwoInts, MulTwoIntsResponse
import rospy

def handle_mul_two_ints(req):
    print("Returning [%s * %s = %s]"%(req.a, req.b, (req.a*req.b)))
    return MulTwoIntsResponse(req.a*req.b)

def mul_two_ints_server():
    rospy.init_node('mul_two_ints_server')
    s = rospy.Service('mul_two_ints', MulTwoInts, handle_mul_two_ints)
    print("Ready to multiply two ints.")
    rospy.spin()

if __name__ == "__main__":
    mul_two_ints_server()
