#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from tutorial.srv import *

def mul_two_ints_client(x, y):
    rospy.wait_for_service('mul_two_ints')
    try:
        mul_two_ints = #Todo
        resp1 = #Todo
        return resp1.#Todo
	#Complete your client request function here
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s*%s"%(x, y))
    print("%s * %s = %s"%(x, y, mul_two_ints_client(x, y)))
