import gym
from agents import RLAgent


def play_a_random_game_first():
    agent = RLAgent([0, 1, 2])
    acumuledReward = 0.0

    env.render()
    action = agent.pickAction()
    observation, reward, done, info = env.step(action)
    reward = agent.getReward(observation, action)
    observation  = [round(observation[0], 2), round(observation[1], 3)]
    acumuledReward += reward

    for step_index in range(goal_steps):
        print(step_index)
       # print("Step {}:".format(step_index))
       # print("action: {}".format(action))
       # print("observation: {}".format(observation))
       # print("reward: {}".format(reward))
       # print("done: {}".format(done))
       # print("info: {}".format(info))
       # print()
        env.render()
        nextAction = agent.stateFunc(str(observation[0]) + str(observation[1]))
        nexctObservation, nextReward, done, nextInfo = env.step(nextAction)
        nextReward = agent.getReward(nexctObservation, nextAction)
        

        agent.updatePolitc(agent.stateActionFunc(str(observation[0]) + str(observation[1]), str(action)) + \
            0.1*(reward + 0.9*(agent.stateActionFunc(str(nexctObservation[0]) + str(nexctObservation[1]), str(nextAction))\
            - agent.stateActionFunc(str(observation[0]) + str(observation[1]),str(action)))),\
                str(observation[0]) + str(observation[1]), action)

        acumuledReward += nextReward
        #acumuledReward = nexctObservation[0]        
        action = nextAction
        nexctObservation = [round(nexctObservation[0], 2), round(nexctObservation[1], 3)]
        observation, reward, done, info = nexctObservation, nextReward, done, nextInfo
        print(observation)
        print(agent.explorerationRate)

    
    env.reset()


env = gym.make('MountainCar-v0')
env.reset()
goal_steps = 10000
score_requirement = -500
intial_games = 10000

play_a_random_game_first()