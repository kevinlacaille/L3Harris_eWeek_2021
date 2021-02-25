import numpy as np
import pandas as pd
import gym
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')



if __name__ == '__main__':
	env = gym.make('CartPole-v0')
	n_games = 1000
	scores = [] #Empty list for holding each game's score, i.e. scores = [sum(game 1 rewards), sum(game2 reward), ...]
	avg_scores = [] #Empty list for holding the trailing average of the agent's scores, calculated as a function of the scores list



	for i in range(n_games):


		#During the course of each game, build the score in a score variable by summing the reward: "score+=reward"

		
		scores.append(score)
		avg_score = np.mean(scores[-100:])


#Data post-processing________________________________________________________________________________________________________
	bestGame = np.argmax(scores)
	bestScore = scores[bestGame]
	print('\nBest Game: %.0f,' % bestGame)
	print('\nBest Score: %.0f,' % bestScore)
	bestAvgGame = np.argmax(avg_scores)
	bestAvgScore = scores[bestAvgGame]
	print('\nBest Avg Game: %.0f,' % bestAvgGame)
	print('\nBest Avg Score: %.0f,' % bestAvgScore)
	filename = 'LL-Agent-Performance.png'
	game = [i for i in range(len(scores))]
	scores_data = pd.DataFrame({"Game":game, "Score":scores})
	sns.scatterplot(x='Game', y='Score', data=scores_data)
	avg_scores_data = pd.DataFrame({"Game":game, "Average":avg_scores})
	sns.lineplot(x='Game', y='Average', data=avg_scores_data)
	plt.show()