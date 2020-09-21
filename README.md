# frozenlake-v0
Simple reinforcement learning solution to [FrozenLake-v0](https://gym.openai.com/envs/FrozenLake-v0/).

## Synopsis
Simple 16x4 table that is updated via q-learning algorithm.

State Space: 16 states  
Action Space: left, down, right, up  
Q-table: Table mapping 16 states to best action for highest cumulative long-term reward.  

Updated via: Q(state, action) = (1-alpha)Q(state, action) + alpha(reward + gamma(maxQ(next state, all actions))  
alpha = learning rate (0 < alpha < 1)  
gamma = discount factor (0 < gamma < 1), importance of future rewards  
epsilon = rate of divergence from q-table (0 < epsilon < 1)  

NOTE: Due to initializing the table to zeros, if either epsilon or the number of training episodes is set too low, the agent may never reach the goal during training which will lead to the qtable being all zeros even after thousands of training episodes. Tweaking the rewards, epsilon greedy strategies, and many other simple solutions can be incorporated to solve this. However, this is a simple environment, and I kept the solution as simple as possible.

The gui is an unfinished attempt to help my friend understand what was going on in a visual way.
