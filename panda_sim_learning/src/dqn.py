#!/usr/bin/env python

from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import numpy as np
import random
import gym

EPISODES = 1000
TIME_STEPS = 500
STATE_DIM = 5
ACTION_DIM = 5
MEMORY_SIZE = 2000
LR = 0.001
DISCOUNT = 0.95
EPSILON = 1.0
EPSILON_DECAY = 0.995
EPSILON_MIN = 0.001
BATCH_SIZE = 32

class Agent:
	def __init__(self, state_dim = STATE_DIM, action_dim = ACTION_DIM, memory_size = MEMORY_SIZE, lr = LR, discount = DISCOUNT, epsilon = EPSILON, epsilon_decay = EPSILON_DECAY, epsilon_min = EPSILON_MIN):
		self.state_dim = state_dim
		self.action_dim = action_dim
		self.memory = deque(maxlen = memory_size)
		self.lr = lr
		self.discount = discount
		self.epsilon = epsilon
		self.epsilon_decay = epsilon_decay
		self.epsilon_min = epsilon_min
		self.network = self.create_dl_network(input_dim = self.state_dim, output_dim = self.action_dim, optimizer_lr = self.lr)
	
	def create_dl_network(self, input_dim, output_dim, optimizer_lr):
		network = Sequential()
		network.add(Dense(24, input_dim = input_dim, activation = 'relu'))
		network.add(Dense(24, activation = 'relu'))
		network.add(Dense(output_dim, activation = 'linear'))
		network.compile(loss = 'mse', optimizer = Adam(lr = optimizer_lr))
		return network
	
	def save2memory(self, state, action, reward, next_state, done):
		self.memory.append((state, action, reward, next_state, done))
	
	def policy(self, state):
		toss = np.random.rand()
		if toss <= self.epsilon:
			return random.randrange(self.action_dim)
		else:
			q_values = self.network.predict(state)
			return np.argmax(q_values[0])
	
	def experience_replay(self, batch_size = BATCH_SIZE):
		batch = random.sample(self.memory, batch_size)
		for tuple in batch:
			state = tuple[0]
			action = tuple[1]
			reward = tuple[2]
			next_state = tuple[3]
			done = tuple[4]
			target_q_val = reward
			if not done:
				target_q_val = target_q_val + self.discount * np.amax(self.network.predict(next_state)[0])
			target_f = self.network.predict(state)
			target_f[0][action] = target_q_val
			self.network.fit(state, target_f, epochs = 1, verbose = 0)
		if self.epsilon > self.epsilon_min:
			self.epsilon = self.epsilon * self.epsilon_decay
	
	def load_network(self, file_path):
		self.network.load_weights(file_path)
	
	def save_network(self, file_path):
		self.network.save_weights(file_path)

if __name__ == "__main__":
	env = gym.make('CartPole-v1')
	state_dim = env.observation_space.shape[0]
	action_dim = env.action_space.n
	agent = Agent(state_dim = state_dim, action_dim = action_dim)
	done = False
	batch_size = BATCH_SIZE
	
	for e in range(EPISODES):
		state = env.reset()
		state = np.reshape(state, [1, state_dim])
		for t in range(TIME_STEPS):
			env.render()
			action = agent.policy(state)
			next_state, reward, done, info = env.step(int(action))
			reward = reward if not done else -10
			next_state = np.reshape(next_state, [1, state_dim])
			agent.save2memory(state, action, reward, next_state, done)
			state = next_state
			if done:
				print "episode:", e, "/", EPISODES, "score:", t, "epsilon:", agent.epsilon
				break
			if len(agent.memory) > batch_size:
				agent.experience_replay(batch_size = batch_size)




