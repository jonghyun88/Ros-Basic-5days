#! /usr/bin/env python

import rospkg
import rospy
# from std_srvs.srv import Empty, EmptyRequest # you import the service message python classes generated from Empty.srv.
from services_quiz.srv import BB8CustomServiceMessage

rospy.init_node('service_move_bb8_in_square_custom_client') # Initialise a ROS node with the name service_client
rospy.wait_for_service('/move_bb8_in_square_custom') # Wait for the service client /move_bb8_in_circle to be running
my_service = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage) # Create the connection to the service
my_service_object = BB8CustomServiceMessage() # Create an object of type EmptyRequest

my_service_object.side = 4.0
my_service_object.repetitions = 4

result = my_service(my_service_object) # Send through the connection the path to the trajectory file to be executed
print result # Print the result given by the service called