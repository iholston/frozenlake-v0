import gym, random 


class qtable:
    def __init__(self, env, alpha, gamma, epsilon):
        self.env = env
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.qtable = [[0] * env.action_space.n for i in range(self.env.observation_space.n)] 

    def train(self, episodes):
        
        # Train for 'episodes' episodes
        print('Training agent over {} episodes...'.format(episodes))
        for i in range(episodes):

            # Run 1 episode
            state = self.env.reset()
            reward = 0
            done = False
            while not done:
                # Choose random action or policy action
                if random.uniform(0,1) < self.epsilon: 
                    action = self.env.action_space.sample()
                else:
                    action = self.qtable[state].index(max(self.qtable[state]))

                # Execute action, observe new state, reward, etc.
                nextstate, reward, done, info = self.env.step(action)
                
                # Update Qtable and move states
                oldvalue = self.qtable[state][action]
                nextmax = max(self.qtable[nextstate])
                self.qtable[state][action] = (1-self.alpha)*oldvalue + self.alpha*(reward + self.gamma*nextmax)
                state = nextstate
        print('Complete.\n')

    def play(self):
        print('Testing Agent over 100 games...')
        totalwins = 0
        for i in range(100):
            state = self.env.reset()
            done = False
            reward = 0
            while not done:
                action = self.qtable[state].index(max(self.qtable[state]))
                state, reward, done, info = self.env.step(action)
                if reward == 1: # Won the game
                    totalwins += 1
        print('Agent successfully reached the goal {} out of 100 attempts.'.format(totalwins))

# Main
env = gym.make('FrozenLake-v0')
alpha = .2
gamma = .9
epsilon = .2 
episodes = 10000

qLearn = qtable(env, alpha, gamma, epsilon)
qLearn.train(episodes)
qLearn.play()


