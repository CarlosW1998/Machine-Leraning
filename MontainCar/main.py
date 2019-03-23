import gym
from agents import RLAgent


def play_a_random_game_first():
    agent = RLAgent([0, 1, 2])
    acumuledReward = 0.0

    env.render()
    action = agent.pickAction()
    observation, reward, done, info = env.step(action)
    acumuledReward += reward
    for step_index in range(goal_steps):

       # print("Step {}:".format(step_index))
       # print("action: {}".format(action))
       # print("observation: {}".format(observation))
       # print("reward: {}".format(reward))
       # print("done: {}".format(done))
       # print("info: {}".format(info))
       # print()
        
        env.render()
        nextAction = agent.stateFunc(str(observation[0]) + str(observation[1]))
        nexctObservation, nextReward, done, nextInfo = env.step(action)
        

        agent.updatePolitc(agent.stateActionFunc(str(observation[0]) + str(observation[1]), str(action)) + \
            0.1*(reward + 0.9*(agent.stateActionFunc(str(nexctObservation[0]) + str(nexctObservation[1]), str(nextAction)\
            - agent.stateActionFunc(str(observation[0]) + str(observation[1]),str(action))))),\
                str(observation[0]) + str(observation[1]), action)

        acumuledReward += nextReward
        action = nextAction
        observation, reward, done, info = nexctObservation, nextReward, done, nextInfo

        if done:
            break



        
    env.reset()


env = gym.make('MountainCar-v0')
env.reset()
goal_steps = 200
score_requirement = -198
intial_games = 10000

play_a_random_game_first()