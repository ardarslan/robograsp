roscore

roslaunch panda_sim_gazebo panda_sim_gazebo_world.launch

roslaunch panda_sim_moveit_config panda_moveit_planning_execution.launch

python ~/catkin_ws/src/panda_sim_gazebo/scripts/grasp.py
