#!/usr/bin/env python

from collections import deque
from keras.models import Model, load_model
from keras.layers import Dense, concatenate, Input
from keras.optimizers import Adam
import numpy as np
import random
import gym


GAMMA = 0.95
LEARNING_RATE = 0.001

MEMORY_SIZE = 1000000
BATCH_SIZE = 20

EXPLORATION_MAX = 1.0
EXPLORATION_MIN = 0.01
EXPLORATION_DECAY = 0.995


class Agent(object):
    def __init__(self, observation_space, action_space):
        self.exploration_rate = EXPLORATION_MAX
        self.observation_space = observation_space
        self.action_space = action_space
        self.memory = deque(maxlen=MEMORY_SIZE)

        self.inputA = Input(shape=(308,))
        self.inputB = Input(shape=(3,))

        self.x = Dense(4, activation="softmax")(self.inputA)
        self.x = Model(inputs=self.inputA, outputs=self.x)

        self.combined_input = concatenate([self.x.output, self.inputB])

        self.z = Dense(24, activation="relu")(self.combined_input)
        self.z = Dense(24, activation="relu")(self.z)
        self.z = Dense(self.action_space, activation="linear")(self.z)

        self.model = Model(inputs=[self.inputA, self.inputB], outputs=self.z)

#		self.model = Sequential()
#		self.model.add(Dense(24, input_shape=(observation_space,), activation="relu"))
#		self.model.add(Dense(24, activation="relu"))
#		self.model.add(Dense(self.action_space, activation="linear"))
        self.model.compile(loss="mse", optimizer=Adam(lr=LEARNING_RATE))

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() < self.exploration_rate:
            return random.randrange(self.action_space)
        q_values = self.model.predict([state[0], state[1]])
        return np.argmax(q_values[0])

    def experience_replay(self):
        if len(self.memory) < BATCH_SIZE:
            return
        batch = random.sample(self.memory, BATCH_SIZE)
        for state, action, reward, state_next, terminal in batch:
            q_update = reward
            if not terminal:
                q_update = (reward + GAMMA * np.amax(self.model.predict([state_next[0], state_next[1]])[0]))
            q_values = self.model.predict([state[0], state[1]])
            q_values[0][action] = q_update
            self.model.fit([state[0], state[1]], q_values, verbose=0)
        self.exploration_rate *= EXPLORATION_DECAY
        self.exploration_rate = max(EXPLORATION_MIN, self.exploration_rate)
	#
	# def self_print(self):
	#     return '#state_dim: ' + str(self.observation_space) + '\n#action_dim: ' + str(self.action_space) + '\n#memory_size: ' + str(len(self.memory)) + '\n#lr: ' + str(self.lr) + '\n#discount: ' + str(self.discount) + '\n#epsilon: ' + str(self.exploration_rate) + '\n#epsilon_decay: ' + str(self.epsilon_decay) + '\n#epsilon_min: ' + str(self.epsilon_min) + '\n#batch_size: ' + str(self.batch_size)
