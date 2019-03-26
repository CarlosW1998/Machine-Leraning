import random


class RLAgent:
	def __init__(self, actions, ER = 0.97	, DR = 0.001):
		self.actions = actions
		self.politc = {}
		self.explorerationRate = ER
		self.decreaseRate = DR
	
	def maxPick(self, state):
		j = str(self.actions[0])
		for i in self.politc[state].keys():
			if self.politc[state][i] > self.politc[state][j]:
				j = i
		return int(j)
	
	def createState(self, key):
		self.politc[key] = {}
		for i in self.actions:
			self.politc[key][str(i)] = 0
		
	def existState(self, state):
		return state in self.politc.keys()
		

	def stateFunc(self, state):
		prob = random.random()
		if not self.existState(state): self.createState(state)

		if prob > self.explorerationRate:
			return self.maxPick(state)

		else:
			self.explorerationRate -= self.decreaseRate
			return random.choice(self.actions)
	
	def pickAction(self):
		
		return random.choice(self.actions)
	
	def stateActionFunc(self, state, action):
		
		if not self.existState(state): self.createState(state)
		return self.politc[state][action]

	def updatePolitc(self, reward, state, action):
		if not self.existState(state): self.createState(state)
		self.politc[state][action] = reward
	
	def getReward(self, state, action):
		
		if state[0] < -0.60 and state[1] < 0 and  action == 0: return 5
		if state[0] < -0.60 and state[1] > 0 and  action == 1: return -5
		if state[0] < -0.60 and state[1] < 0 and  action == 2: return -5

		if state[0] < -0.60 and state[1] > 0 and  action == 0: return -5
		if state[0] < -0.60 and state[1] > 0 and  action == 1: return -5
		if state[0] < -0.60 and state[1] > 0 and  action == 2: return 5

		if state[0] > -0.60 and state[1] > 0 and  action == 2: return 5
		if state[0] > -0.60 and state[1] > 0 and  action == 1: return -5
		if state[0] > -0.60 and state[1] > 0 and  action == 0: return -5

		if state[0] > -0.60 and state[1] < -0.2 and  action == 2: return -5
		if state[0] > -0.60 and state[1] < -0.2 and  action == 1: return -5
		if state[0] > -0.60 and state[1] < -0.2 and  action == 0: return 5
		
		
		return 0
	