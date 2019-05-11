#!/usr/bin/env python

import sys
import math
import random
import datetime
import numpy as np
import rospy
import moveit_commander
import matplotlib.pyplot as plt
from robot_env import RobotEnv
from dqn import Agent

EPISODES = 10000
TIME_STEPS = 500
MEMORY_SIZE = 20000
LR = 0.001
DISCOUNT = 0.95
EPSILON = 1.0
EPSILON_DECAY = 0.995
EPSILON_MIN = 0.001
BATCH_SIZE = 32
LOG_FILE = '/home/aykut/catkin_ws/src/dqn_log/dqn_log_' + str(datetime.datetime.now()) + '.txt'

def log(str):
    with open(LOG_FILE, 'a+') as f:
        f.write(str + '\n')

if __name__ == '__main__':
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('robot_env', anonymous = True)
    rospy.sleep(1)

    env = RobotEnv()
    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.n
    dqn_agent = Agent(state_dim = state_dim, action_dim = action_dim, memory_size = MEMORY_SIZE, lr = LR, discount = DISCOUNT, epsilon = EPSILON, epsilon_decay = EPSILON_DECAY, epsilon_min = EPSILON_MIN, batch_size = BATCH_SIZE)
    done = False
    
    reward_list = []
    
    for e in range(1, EPISODES+1):
        dist_list = []
        log('###################################################')
        log('#################### EPISODE ' + str(e) + ' ' + '#'*(20-int(math.log(e, 10))))
        log('###################################################')
        state = env.reset()
        state = np.reshape(state, [1, state_dim])
        total_reward = 0
        for t in range(1, TIME_STEPS+1):
            action = dqn_agent.policy(state)
            log('############### ITERATION ' + str(t) + ' ' + '#'*(15-int(math.log(t, 10))))
            next_state, reward, done, info, next_distance = env.step(int(action))
            dist_list.append(next_distance)
            reward = reward if not done else -10
            total_reward += reward
            next_state = np.reshape(next_state, [1, state_dim])
            log('State: ' + str(state))
            log('Action: ' + str(action))
            log('Reward: ' + str(reward))
            log('Next State: ' + str(next_state))
            log('Done: ' + str(done))
            log('Total Reward: ' + str(total_reward))
            dqn_agent.save2memory(state, action, reward, next_state, done)
            state = next_state
            if done:
                log('##### End of episode: ', e, '/', EPISODES, 'score: ', t)
                log('##### DQN Agent:\n' + dqn_agent.self_print())
                break
            if len(dqn_agent.memory) > BATCH_SIZE:
                dqn_agent.experience_replay()
        
        plt.figure()
        plt.plot(dist_list)
        plt.savefig('/home/aykut/catkin_ws/src/dqn_log/distance_figs/distance_' + str(e) + '.jpg')
        plt.close()
        reward_list.append(total_reward)

    plt.figure()
    plt.plot(reward_list)
    plt.savefig('/home/aykut/catkin_ws/src/dqn_log/reward.jpg')
    plt.close()
    
#    roscpp_shutdown()
    





