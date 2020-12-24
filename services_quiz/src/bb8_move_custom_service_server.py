#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage
from geometry_msgs.msg import Twist

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_square_custom has been called")
    i = 0
    
    while i <= request.repetitions: 

        while i <= request.side: 
            move_square.linear.x = 0.2
            move_square.angular.z = 0
            my_pub.publish(move_square)
            rate.sleep()
            i += 1
        
        
        while i <= 5: 
            move_square.linear.x = 0
            move_square.angular.z = 0.1
            my_pub.publish(move_square)
            rate.sleep()
            i += 1
    i += 1
    
    rospy.loginfo("Finished service move_bb8_in_square_custom")

    response = BB8CustomServiceMessage()
    response.success = True
    
    return response # the service Response class, in this case EmptyResponse


rospy.init_node('service_move_bb8_in_square_custom_server') 
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage, my_callback)
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move_square = Twist()
rate = rospy.Rate(1)
rospy.loginfo("Service /move_bb8_in_square_custom Ready")
rospy.spin() # mantain the service open.


from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest
