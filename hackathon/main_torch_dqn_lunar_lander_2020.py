import gym
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from simple_dqn_torch_2020 import Agent
from utils import plotLearning
import numpy as np

if __name__ == '__main__':
    env = gym.make('LunarLander-v2')
    agent = Agent(gamma=0.99, epsilon=1.0, batch_size=64, n_actions=4, eps_end=0.01,
                  input_dims=[8], lr=0.005)
    scores, eps_history = [], []
    avg_scores = []
    n_games = 1000
    
    for i in range(n_games):
        score = 0
        done = False
        observation = env.reset()
        while not done:
            action = agent.choose_action(observation)
            observation_, reward, done, info = env.step(action)
            score += reward
            agent.store_transition(observation, action, reward, 
                                    observation_, done)
            agent.learn()
            observation = observation_

            env.render(mode='human')
        scores.append(score)
        eps_history.append(agent.epsilon)

        avg_score = np.mean(scores[-100:])
        
        avg_scores.append(avg_score)
        
        print('episode ', i, 'score %.2f' % score,
                'average score %.2f' % avg_score,
                'epsilon %.2f' % agent.epsilon)
    best_game = np.argmax(scores)
    best_score = scores[best_game]
    best_avg_game = np.argmax(avg_scores)
    best_avg_score = scores[best_avg_game]
    filename = 'LL-Agent-Performance.png'
    game = [i for i in range(len(scores))]
    scores_data = pd.DataFrame({"Game":game, "Score":scores})
    sns.scatterplot(x='Game', y='Score', data=scores_data)
    avg_scores_data = pd.DataFrame({'Game':game, 'Average':avg_scores})
    sns.lineplot(x='Game', y='Average', data=avg_scores_data)
    plt.show()
    #x = [i+1 for i in range(n_games)]
    #filename = 'lunar_lander.png'
    #plotLearning(x, scores, eps_history, filename)

